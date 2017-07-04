"""String palindrome check using a recursive function"""


def is_palindrome(val):
    """Assumes val is a string
    Returns True if the letters in val for a palindrome; False otherwise.
    Non-letters and capitalization are ignored"""

    def to_chars(val):
        """return only lower case letters"""
        val = val.lower()
        letters = ''
        for ch in val:
            if ch in 'abcdefghijklmnopqrstuvwxyz':
                letters = letters + ch
            return letters

    def is_pal(val):
        """Check for palindrome"""
        if len(val) <= 1:
            return True
        else:
            return val[0] == val[-1] and is_pal(val[1:-1])

    return is_pal(to_chars(val))
