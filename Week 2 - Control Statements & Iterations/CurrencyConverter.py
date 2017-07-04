"""Convert currency from USD to Chinese RMB

Rules:
1 USD = 6.81 RMB

Output should look like: $100 is 681.0 yuan

"""

FOREX = float(input("Enter the exchange rate from dollars to RMB: "))
UCOMMAND = eval(input("Enter 0 to convert USD to RMB, and 1 to convert RMB to USD: "))

if UCOMMAND == 0:
    USD = float(input("Enter the dollar amount: "))

    # Do the conversion and output result
    RMBEQ = USD * FOREX
    print("{0} dollars is {1} yuan".format(USD, RMBEQ))

elif UCOMMAND == 1:
    RMB = float(input("Enter the yuan amount: "))

    # Do the conversion and output result
    USDEQ = RMB / FOREX
    print("{0} yuan is {1} dollars".format(RMB, round(USDEQ, 2)))


# Test values
# Exchange rate 6.81, USD: 100, RMB: 10000
