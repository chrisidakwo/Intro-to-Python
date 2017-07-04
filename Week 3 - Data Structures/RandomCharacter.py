from random import randint

# Generate a random character between ch1 and ch2
def getRandomCharacter(ch1, ch2):
    return chr(randint(ord(ch1), ord(ch2)))

# Generate a random lowercase letter
def getRandomLowerCaseLeter():
    return getRandomCharacter('a', 'z')

# Generate a random uppercase letter
def getRandomUpperCaseLetter():
    return getRandomCharacter('A', 'z')

# Generate a random digit character
def getRandomDigitCharacter():
    return getRandomCharacter('0', '9')

# Generate a random character
def getRandomASCIICharacter():
    return chr(randint(0, 127))

