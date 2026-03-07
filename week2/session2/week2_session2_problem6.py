"""
You have a list of integers collection_sizes representing the sizes of different art collections in your gallery
and are trying to determine how to group them to best fit in your space. Given an integer k write a function
count_divisible_collections() that returns the number of non-empty subarrays (contiguous parts of the
array) where the sum of the sizes is divisible by k.
"""


def count_divisible_collections(collection_sizes, k):
    """
    - input list, int, output int
    - enumerate subarrays

    - nested for loop, each outer iteration check if sum divisible by k
    - if yes, increment result by 1

    - r.t. O(n^2) space O(1)
    """
    res = 0
    for i in range(len(collection_sizes)):
        tot = 0
        for j in range(i, len(collection_sizes)):
            tot += collection_sizes[j]
            if tot % k == 0:
                res += 1

    return res

def count_divisible_collections2(collection_sizes, k):
    """
    - use a hashmap to store count of remainders
    - traverse the input list, calculate remainder of prefix sum
    - if the remainder has appeared, then there are subarrays in between whose sum is divisible by k
    """
    cnt = {0: 1}
    prefix_sum = 0
    res = 0
    for i in range(len(collection_sizes)):
        prefix_sum += collection_sizes[i]
        remainder = prefix_sum % k
        res += cnt.get(remainder, 0)
        cnt[remainder] = cnt.get(remainder, 0) + 1
    return res


if __name__ == "__main__":
    nums1 = [4, 5, 0, -2, -3, 1]
    k1 = 5
    nums2 = [5]
    k2 = 9

    print(count_divisible_collections2(nums1, k1))
    print(count_divisible_collections2(nums2, k2))
