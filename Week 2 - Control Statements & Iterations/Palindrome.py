""" Determine if a text or number is palindrome """
# MAX = 5
# COUNT = 0
# while COUNT < MAX:
#
#
#     COUNT += 1

UINPUT = str(input("Enter a text or a number: "))
isPalindrome = True if str(UINPUT) == str(UINPUT)[::-1] else False
# isPalindrome = True if list(UINPUT) == list(reversed(UINPUT)) else False
if isPalindrome:
    print("{0} is a palindrome".format(UINPUT))
else:
    print("{0} is not a palindrome".format(UINPUT))

# Visit links for further examples of implementation
# https://codescracker.com/python/program/python-program-check-palindrome.htm
# https://shankaraman.wordpress.com/2011/05/29/program-to-find-the-given-string-is-palindrome-or-not-in-python/
# http://stackoverflow.com/questions/17331290/how-to-check-for-palindrome-using-python-logic


