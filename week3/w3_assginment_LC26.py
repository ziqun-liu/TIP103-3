# 26. Remove Duplicates from Sorted Array

def removeDuplicates(nums):
    """
    - need to fill the first k elements with unique values
    - need a pointer n to indicate the position to update the value
    - loop through the list
        - When current int is not equal to prev, there a new unique value
        - It is time to write to position n
     [1, 1, 2, 3, 4, 4, 4]
      n
      i

    i=0: nums[0]=1, n+=1=1
    i=1: nums[0]=1, n still 1
    i=2: nums[2]=2, 2!=1, write 2 to n, [1, 2, 2, 3, 4, 4, 4], n+=1=2
    i=3: nums[3]=3, 3!=2, write 3 to n, [1, 2, 3, 3, 4, 4, 4], n+=1=3
    i=4: nums[4]=4, 4!=3, write 4 to n, [1, 2, 3, 4, 4, 4, 4], n+=1=4
    i=5,6, n still 4
    return n = 4
    """
    if not nums:
        return 0

    n = 0
    for i in range(len(nums)):
        if i == 0 or nums[i] != nums[i - 1]:
            nums[n] = nums[i]
            n += 1
    return n


def removeDuplicates2(nums):
    pass


if __name__ == '__main__':
    print(removeDuplicates([1, 1, 2, 3, 4, 4, 4]))
    print(removeDuplicates([1, 1, 2, 2, 2, 3, 4, 4, 5]))
