""" Experiment with 'continue' in a while loop """

while True:
    DATA = input("Enter a number [\"q\" quits the program]: ")
    if DATA == "q":
        break
    NUMBER = int(DATA)
    if NUMBER % 2 != 0:
        continue
    print("{0} squared is {1}".format(NUMBER, pow(NUMBER, 2)))
