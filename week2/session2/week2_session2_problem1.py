"""
As the curator of an art gallery, you are organizing a new exhibition. You must ensure the collection of
art pieces are balanced to attract the right range of buyers. A balanced collection is one where the
difference between the maximum and minimum value of the art pieces is exactly 1.

Given an integer array art_pieces representing the value of each art piece, write a function
find_balanced_subsequence() that returns the length of the longest balanced subsequence.

A subsequence is a sequence derived from the array by deleting some or no elements without changing the
order of the remaining elements.
"""

from collections import Counter


def find_balanced_subsequence(art_pieces):
    """
    U — Understand
        Input:  integer array art_pieces
        Output: length of the longest balanced subsequence
        Balanced: max(subsequence) - min(subsequence) == 1
        A valid subsequence can only contain two values: x and x+1.

    M — Match
        Pattern: frequency map
        Key observation: the longest balanced subsequence using x and x+1
        contains all occurrences of both, so length = freq[x] + freq[x+1].
        Time complexity target: O(n)

    P — Plan
        1. Build frequency map: freq = Counter(art_pieces)
        2. Initialize res = 0
        3. For each x in freq:
               if x+1 in freq: res = max(res, freq[x] + freq[x+1])
        4. Return res

    R — Review
        Example 1: [1, 3, 2, 2, 5, 2, 3, 7]
            freq: {1:1, 2:3, 3:2, 5:1, 7:1}
            pairs: 1+2=4, 2+3=5 ← max
            result = 5

        Example 2: [1, 2, 3, 4]
            pairs: 1+2=2, 2+3=2, 3+4=2
            result = 2

        Example 3: [1, 1, 1, 1]
            freq: {1:4}, no x+1 exists
            result = 0

    E — Evaluate
        Time:  O(n)
        Space: O(n)
    """
    freq = Counter(art_pieces)
    res = 0

    for x in freq:
        if x + 1 in freq:
            res = max(res, freq[x] + freq[x + 1])

    return res


    # 2. sort the arr --> sliding window
    # time: O(nlogn) bc sorting
    # space: O(1)
def find_balanced_subsequence2(art_pieces):
    art_pieces.sort()

    left = 0
    res = 0

    for right in range(len(art_pieces)):
        while art_pieces[right] - art_pieces[left] > 1:
            left += 1

        if art_pieces[right] - art_pieces[left] == 1:
            res = max(res, right - left + 1)

    return res

if __name__ == '__main__':
    art_pieces1 = [1, 3, 2, 2, 5, 2, 3, 7]
    art_pieces2 = [1, 2, 3, 4]
    art_pieces3 = [1, 1, 1, 1]

    print(find_balanced_subsequence(
        art_pieces1))  # 5 Example 1 Explanation:  The longest balanced subsequence is [3,2,2,2,3].
    print(find_balanced_subsequence(art_pieces2))  # 2
    print(find_balanced_subsequence(art_pieces3))  # 0
