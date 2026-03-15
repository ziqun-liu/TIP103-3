"""
You are managing an animal adoption center. You have:

A string available, representing the animals currently available for adoption.
A string preferred, representing a customer's preferred sequence of animals.

You want to make sure the preferred sequence appears as a subsequence of available. A subsequence means the characters
appear in order, but not necessarily consecutively.

To achieve this, you are allowed to append characters to the end of available. You cannot remove characters or insert
them elsewhere.

Return the minimum number of characters you need to append to the end of available so that preferred becomes a subsequence.

"""


def append_animals(available, preferred):
    """
    - input string, output int
    - parse string
    - two pointer p1 -> s1[0], p2 -> s2[0]
        - if they match, then p1++, p2++
        - if they don't match, then p1++
        - if p1 is at string end, return len(s2) - p2
        - if p2 is at string end, return 0, which is also len(s2) - p2
    """
    p1 = p2 = 0
    while p1 < len(available) and p2 < len(preferred):
        if available[p1] == preferred[p2]:
            p2 += 1
        p1 += 1
    return len(preferred) - p2


if __name__ == '__main__':
    print(append_animals("catsdogs", "cows"))  # 2
    print(append_animals("rabbit", "r"))  # 0
    print(append_animals("fish", "bird"))  # 4
