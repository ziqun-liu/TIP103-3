# You are given a string s that consists of lowercase English letters representing animal names or
# slogans and brackets. The goal is to rearrange the animal names or slogans in each pair of matching
# parentheses by reversing them, starting from the innermost pair.

# After processing, your result should not contain any brackets.

def rearrange_animal_names(s):
    """
    (!(love(stac))I)
    stk             temp
    (!(love(stac)
                    cats
    (!(lovecats)
                    stacevol
    (!stacevolI)
                    Ilovecats!
    """
    stk = []

    for ch in s:
        if ch == ')':
            temp = []
            while stk and stk[-1] != '(':
                temp.append(stk.pop())
            stk.pop()
            stk.extend(temp)
        else:
            stk.append(ch)

    return ''.join(stk)


if __name__ == "__main__":
    print(rearrange_animal_names("(dribtacgod)"))  # dogcatbird
    print(rearrange_animal_names("(!(love(stac))I)"))  # Ilovecats!
    print(rearrange_animal_names("adopt(yadot(a(tep)))!"))  # adoptapettoday!

