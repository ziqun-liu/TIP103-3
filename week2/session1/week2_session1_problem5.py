"""
Given an array of integers gold_amounts representing the amount of gold at each location and an integer target,
return the indices of the two locations whose gold amounts add up to the target.

Assume that each input has exactly one solution, and you may not use the same location twice. You can return the
answer in any order.
"""


def find_treasure_indices(gold_amounts, target):
    """
    Understand:
        - input list
        - output list of 2 elements
    Match:
        - hashmap
    Plan:
        - use hashmap to keep track of indices {gold: index}
        - if target - gold in map, return
        - if not, insert (gold: index) into map
    """
    loc = {}
    for i, gold in enumerate(gold_amounts):
        if target - gold in loc:
            return [loc[target - gold], i]
        loc[gold] = i

    return


if __name__ == "__main__":
    gold_amounts1 = [2, 7, 11, 15]
    target1 = 9

    gold_amounts2 = [3, 2, 4]
    target2 = 6

    gold_amounts3 = [3, 3]
    target3 = 6

    print(find_treasure_indices(gold_amounts1, target1))  # [0, 1]
    print(find_treasure_indices(gold_amounts2, target2))  # [1, 2]
    print(find_treasure_indices(gold_amounts3, target3))  # [0, 1]
