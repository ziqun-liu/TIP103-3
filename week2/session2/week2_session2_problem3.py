"""
You are tasked with organizing a collection of art prints represented by a list of strings collection.
You need to display these prints on a single wall in a 2D array format that meets the following criteria:

    1. The 2D array should contain only the elements of the array collection.
    2. Each row in the 2D array should contain distinct strings.
    3. The number of rows in the 2D array should be minimal.

Return the resulting array. If there are multiple answers, return any of them.
Note that the 2D array can have a different number of elements on each row.
"""


def organize_exhibition(collection):
    """
    U
        - input list of strings
        - output list of lists of strings
    M
        - hashset for occurrences
    P
        - use a counter hashmap
        - loop through each string in map
        - decrement 1 occurrence each iteration, append strings to temp string
        - append temp string to result string each iteration
    """
    cnt = {}
    for one in collection:
        cnt[one] = cnt.get(one, 0) + 1

    res = []
    while cnt:
        temp = []
        to_delete = []
        for string in cnt:
            temp.append(string)
            cnt[string] -= 1
            if cnt[string] == 0:
                to_delete.append(string)
        for string in to_delete:
            del cnt[string]
        res.append(temp)

    return res


if __name__ == "__main__":
    collection1 = ["O'Keefe", "Kahlo", "Picasso", "O'Keefe", "Warhol", "Kahlo", "O'Keefe"]
    collection2 = ["Kusama", "Monet", "Ofili", "Banksy"]

    print(organize_exhibition(collection1))
    # Example 1 Explanation:
    # All elements of collections were used, and each row of the 2D array contains
    # distinct strings, so it is a valid answer.
    # It can be shown that we cannot have less than 3 rows in a valid array.

    print(organize_exhibition(collection2))
    # Example 2 Explanation:
    # All elements of the array are distinct, so we can keep all of them in the first
    # row of the 2D array.
