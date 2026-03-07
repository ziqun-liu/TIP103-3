"""
Your gallery has entered a competition for the most beautiful collection. Your collection is represented by a string
collection where each artist in your gallery is represented by a character. The beauty of a collection is defined as
the difference in frequencies between the most frequent and least frequent characters.

For example, the beauty of "abaacc" is 3 - 1 = 2.
Given a string collection, write a function beauty_sum() that returns the sum of beauty of all of its
substrings (subcollections), not just of the collection itself.
"""


def beauty_sum(collection):
    """
    - input one string, output integer

    - generate subsequence

    - use a hastemp to store count of each letter
    {a: 3, b:1, c: 2}
    - generate all substrings
    - map for every substring
    - get "beauty"

    - r.t. O(26 n^2)=O(n^2) brute force substring, each iteration do max/min, which takes O(26)
    """
    
    beauty = 0
    for i in range(len(collection)):
        hmap = {}
        for j in range(i, len(collection)):
            hmap[collection[j]] = hmap.get(collection[j], 0) + 1
            diff = max(hmap.values()) - min(hmap.values())
            beauty += diff

    return beauty


if __name__ == '__main__':
    """
    a 1-1
    aa 2-2
    aab 2-1=1   1
    aabc 2-1=1  2
    aabcb 2-1=1  3
    
    a
    ab
    abc
    abcb 2-1=1  4
    
    b
    bc
    bcb 2-1=1  5
    
    c
    cb
    
    b
    """
    print(beauty_sum("aabcb"))
    # 5
    # Example 1 Explanation: The substrings with non-zero beauty are
    # ["aab","aabc","aabcb","abcb","bcb"], each with beauty equal to 1.

    print(beauty_sum("aabcbaa"))
    # 17
