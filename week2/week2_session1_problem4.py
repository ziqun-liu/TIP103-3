"""
Captain Feathersword has found another pirate's buried treasure, but they suspect it's booby-trapped.
The treasure chest has a secret code written in pirate language, and Captain Feathersword believes the trap can be
disarmed if the code can be balanced. A balanced code is one where the frequency of every letter present in the code
is equal. To disable the trap, Captain Feathersword must remove exactly one letter from the message.
Help Captain Feathersword determine if it's possible to remove one letter to balance the pirate code.

Given a 0-indexed string code consisting of only lowercase English letters, write a function can_make_balanced()
that returns True if it's possible to remove one letter so that the frequency of all remaining letters is equal,
and False otherwise.
"""


def can_make_balanced(code):
    """
    UMPIRE
    Understand:
        - In: string
        - Out: boolean
    Match:
        - parse string
    Plan:
        - Use a hashmap to keep track of the frequency of each letter present in the string
        - Maintain an allowed_remove variable
        - Maintain a prev_cnt variable
        - If curr_cnt != prev_cnt, then decrement allowed remove
    """
    freq = {}
    for ch in code:
        freq[ch] = freq.get(ch, 0) + 1

    # Trey to decrement by 1 all char's frequencies
    for ch in freq:
        # make a copy and delete one char
        new_freq = freq.copy()
        new_freq[ch] -= 1
        # If the frequency of ch becomes 0 after decrement, delete the key `ch`
        if new_freq[ch] == 0:
            del new_freq[ch]

        # Check if all frequencies are equal
        values = list(new_freq.values())
        if (len(set(values)) == 1):  # All frequencies are equal
            return True

    return False


if __name__ == '__main__':
    code1 = "arghh"
    code2 = "haha"
    code3 = "aaaii"
    code4 = "aaabbbii"

    print(can_make_balanced(code1))  # True
    print(can_make_balanced(code2))  # False
    print(can_make_balanced(code3))  # True
    print(can_make_balanced(code4))  # False
