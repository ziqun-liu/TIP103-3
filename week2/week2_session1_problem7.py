"""
Return the minimum number of steps to make map2 an anagram of map1.
An Anagram of a string is a string that contains the same characters with
a different (or the same) ordering.
"""


def min_steps_to_match_maps(map1, map2):
    """
    U:
        - input string
        - output int
    M:
        - hashmap
    P:
        - get frequency of every char
        - convert one map to the other, count number of steps
    """
    hmap1 = {}; hmap2 = {};
    for ch in map1:
        hmap1[ch] = hmap1.get(ch, 0) + 1
    for ch in map2:
        hmap2[ch] = hmap2.get(ch, 0) + 1

    res = 0
    for ch in hmap1:
        res += max(0, hmap1[ch] - hmap2.get(ch, 0))

    return res


if __name__ == "__main__":
    map1_1 = "bab"
    map2_1 = "aba"
    map1_2 = "treasure"
    map2_2 = "huntgold"
    map1_3 = "anagram"
    map2_3 = "mangaar"

    print(min_steps_to_match_maps(map1_1, map2_1))  # 1
    print(min_steps_to_match_maps(map1_2, map2_2))  # 6
    print(min_steps_to_match_maps(map1_3, map2_3))  # 0
