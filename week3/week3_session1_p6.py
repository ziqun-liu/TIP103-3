"""
Given two integer arrays admitted and adopted each with distinct values representing animals in an animal shelter,
return True if this could have been the result of a sequence of admitting and adopting animals from the shelter,
or False otherwise.
"""


def validate_shelter_sequence(admitted, adopted):
    """
    - input string, output boolean
    - matching subsequences
    - push admitted to a stack one by one
        - each step check adopted front, if match, pop both stack and adopted
        - if no match, conitnue pushing, if reaches end, return false
        - return true
    - [1,2,3] [3,2,1]
    stack       ptr
    [1]          0   no match
    [1,2]        0   no match
    [1,2,3]      0   match
    [1,2]        1   match
    [1]          2   match
    - [1,2,3] [3,1,2]
    stack       ptr
    [1]          0   no match
    [1,2]        0   no match
    [1,2,3]      0   match
    [1,2]        1   no match
    """
    stack = []
    ptr = 0
    for animal in admitted:
        stack.append(animal)
        while ptr != len(adopted) and stack and adopted[ptr] == stack[-1]:
            stack.pop()
            ptr += 1

    return ptr == len(adopted)


if __name__ == "__main__":
    print(validate_shelter_sequence([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]))
    print(validate_shelter_sequence([1, 2, 3, 4, 5], [4, 3, 5, 1, 2]))
