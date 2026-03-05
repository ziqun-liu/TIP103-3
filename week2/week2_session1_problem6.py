"""
You are given an integer array group_sizes, where group_sizes[i] is the size of the
group that pirate i should be in. For example, if group_sizes[1] = 3, then pirate 1
must be in a group of size 3.

Return a list of groups such that each pirate i is in a group of size group_sizes[i].

Each pirate should appear in exactly one group, and every pirate must be in a group.
If there are multiple answers, return any of them. It is guaranteed that there will
be at least one valid solution for the given input.
"""

from collections import defaultdict


def organize_pirate_crew(group_sizes):
    """
    Understand:
        - input list
        - output list of lists
    Match:
        - traverse list
    Plan:
        - use a hashmap, {group_size: []}
        - if group_size[1] == 3, check if a list of size 3 exists, and if not, create a list of size 3 and insert 3
        - cut lists into groups of size `group_size`
    """
    cnt = defaultdict(list)

    for i, size in enumerate(group_sizes):
        cnt[size].append(i)

    res = []
    for size, pirates in cnt.items():
        for i in range(0, len(pirates), size):
            res.append(pirates[i:i + size])

    return res


if __name__ == "__main__":
    group_sizes1 = [3, 3, 3, 3, 3, 1, 3]
    group_sizes2 = [2, 1, 3, 3, 3, 2]

    print(organize_pirate_crew(group_sizes1))  # [[5], [0, 1, 2], [3, 4, 6]]
    print(organize_pirate_crew(group_sizes2))  # [[1], [0, 5], [2, 3, 4]]
