# 941. Valid Mountain Array
#
# Given an array of integers arr, return True if and only if it is a valid mountain array.
# arr is a mountain array if and only if:
#   - len(arr) >= 3
#   - There exists some i with 0 < i < len(arr) - 1 such that:
#       arr[0] < arr[1] < ... < arr[i-1] < arr[i]
#       arr[i] > arr[i+1] > ... > arr[len(arr)-1]
#
# Example 1: arr = [2,1]     -> False
# Example 2: arr = [3,5,5]   -> False
# Example 3: arr = [0,3,2,1] -> True


def valid_mountain_array(arr: list[int]) -> bool:
    n = len(arr)
    if n < 3:
        return False

    l, r = 0, n - 1

    while l + 1 < n and arr[l] < arr[l + 1]:
        l += 1
    while r - 1 >= 0 and arr[r] < arr[r - 1]:
        r -= 1

    return l == r and l != 0 and r != n - 1


if __name__ == "__main__":
    test_cases = [
        ([2, 1], False),
        ([3, 5, 5], False),
        ([0, 3, 2, 1], True),
        ([1, 2, 3, 4, 5], False),
        ([5, 4, 3, 2, 1], False),
        ([0, 2, 3, 4, 5, 2, 1, 0], True),
    ]

    for arr, expected in test_cases:
        result = valid_mountain_array(arr)
        status = "PASS" if result == expected else "FAIL"
        print(f"[{status}] arr={arr} -> {result} (expected {expected})")