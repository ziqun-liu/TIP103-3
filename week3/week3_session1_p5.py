"""
You are managing a wildlife sanctuary where animals of the same species need to be grouped together by their habitats.
Given a string habitats representing the sequence of animals, where each character corresponds to a particular species,
you need to partition the string into as many contiguous groups as possible, ensuring that each species appears in at
most one group.

The order of species in the resultant sequence must remain the same as in the input string habitats.

Return a list of integers representing the size of these habitat groups.
"""


def group_animals_by_habitat(habitats):
    """
    - partition the string into as many contiguous groups as possible, ensuring that each species appears in at
most one group
    - input string, output list of integers representing the size of these habitat groups
    - parse the string
    - use a hashmap {'a': 1}
    - "ababcbacadefegdehijhklij
        - first pass: traverse get the last occurrence of each character
        - ababcbaca {'a': 8, 'b': 5, 'c': 7}
        - index     character       fence
          0             a           8
          1             b           max(5,8)=8
          2             a           8
          3             b           8
          4             c           max(7,8)=8
          5             b           8
          6             a           8
          7             c           8
          8             a           8   ==> i = fence, so this is the cutting point
        - second pass
            - check every character if it is its last occurrence
            - if last[habitat[ch]] > fence, fence = last[habitat[ch]]
            - maintain a start var to track window length
            - if i == fence, append i - start + 1 and set start to i + 1
        - r.t. O(N), space O(1)
    """
    last = {}
    for i, ch in enumerate(habitats):
        last[ch] = i

    res = []
    fence = 0
    start = 0
    for i, ch in enumerate(habitats):
        fence = max(fence, last[ch])
        if i == fence:
            res.append(i - start + 1)
            start = i + 1

    return res


if __name__ == '__main__':
    print(group_animals_by_habitat("ababcbacadefegdehijhklij"))  # [9,7,8]
    print(group_animals_by_habitat("eccbbbbdec"))  # [10]
