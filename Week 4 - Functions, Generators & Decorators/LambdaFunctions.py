"""Writing lambda functions in Python"""


def cap(x):
    if x == "xyz":
        return x.upper() + "!"


def edit_story(words, cap):
    for word in words:
        print(cap(word))

edit_story(["daniel", "chris", "fred"], cap)
print()

names = ["daniel", "chris", "fred"]
# ==> Here is our lambda function that does exactly
# what the combination of both functions above would do
edit_story(names, lambda name: name.upper() + "!" if name == "xyz" else "")

print(type(edit_story))
print()

