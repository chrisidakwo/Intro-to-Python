""" Develop a program to play a lottery """
import random

# Generate a random number
LOTTERY = random.randint(0, 99)

# Prompt the user to enter a guess
GUESS = int(input("Enter your lottery pick (two digits): "))

# Get the digits from LOTTERY
LOTTERYDIGIT1 = LOTTERY // 10
LOTTERYDIGIT2 = LOTTERY % 10

# Get the user's digits from GUESS
GUESSDIGIT1 = GUESS // 10
GUESSDIGIT2 = GUESS % 10

print("The lottery number is", LOTTERY)


# Check the user's guess
if GUESS == LOTTERY:
    print("Exact match. You win MWK 7,500,000!")
elif GUESSDIGIT2 == LOTTERYDIGIT2 and GUESSDIGIT1 == LOTTERYDIGIT2:
    print("Match all digits. You win MWK 2,250,000")
elif (GUESSDIGIT1 == LOTTERYDIGIT1
      or GUESSDIGIT1 == LOTTERYDIGIT2
      or GUESSDIGIT2 == LOTTERYDIGIT1
      or GUESSDIGIT2 == LOTTERYDIGIT2):
    print("Match one digit, You win MWK 750,000")
else:
    print("Sorry, no match")
