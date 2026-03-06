"""
Your art gallery has just been shipped a new collection of numbered art pieces, and you need to verify their authenticity. The collection is considered "authentic" if it is a permutation of an array base[n].

The base[n] array is defined as [1, 2, ..., n - 1, n, n], meaning it is an array of length n + 1 containing the integers from 1 to n - 1 exactly once, and the integer n twice. For example, base[1] is [1, 1] and base[3] is [1, 2, 3, 3].

Write a function is_authentic_collection that accepts an array of integers art_pieces and returns True if the given array is an authentic array, and otherwise returns False.

Note: A permutation of integers represents an arrangement of these numbers. For example [3, 2, 1] and [2, 1, 3] are both permutations of the series of numbers 1, 2, and 3.
"""

from collections import Counter


def is_authentic_collection(art_pieces):
    """
    Understand:
        - input list
        - output boolean
    Match:
        - hashmap
        - traverse list
    Plan:
        - Find the largest integer k := len(art_pieces) - 1, because the last integer is repeated
        - The tricky concept is that k is the integer and we can get k from length of input. k is not an index.
        - Loop through integer 1 to k - 1
            - if the integer if not present in hamp, return False
            - if the num occurrances of the integer is not 1, return False
        - Check integer k
            - if num occurrance of k is not 2, return False
    """
    k = len(art_pieces) - 1
    hmap = Counter(art_pieces)  # {1:1, 2:1, 3:1}

    for key, val in hmap.items():
        print(f"key={key}, val={val}")
    print()

    for i in range(1, k):
        print(f"integer={i}, occurrance={hmap[i]}")
        if hmap[i] != 1:
            return False
    print()

    print(f"k={k}, occurrance={hmap[k]}")
    if hmap[k] != 2:
        return False

    return True


if __name__ == "__main__":
    collection1 = [2, 1, 3]
    collection2 = [1, 3, 3, 2]
    collection3 = [1, 1]
    collection4 = [1, 2, 2, 3, 3]
    collection5 = [1, 2, 3, 11, 11]
    collection6 = [1, 2, 3, 11, 12, 12]

    # print(is_authentic_collection(collection1))
    # print(is_authentic_collection(collection2))
    # print(is_authentic_collection(collection3))
    # print(is_authentic_collection(collection4))
    print(is_authentic_collection(collection5))
    # print(is_authentic_collection(collection6))
