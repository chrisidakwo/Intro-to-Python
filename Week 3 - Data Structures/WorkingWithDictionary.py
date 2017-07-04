"""Sample and test codes for working with dictionary"""
import copy

table_rows = {"row2": "Student2", "row1": "Student1", "row3": "Student3", "row4": "Student4"}

# Find the length of a dictionary using len()
print(len(table_rows))


# Sort a dictionary
print(sorted(table_rows))


# Retrieve an item
item1 = table_rows['row1']
print(item1, "\n")


# Assign, retrieve, update, and delete using the index operator
print(table_rows)
table_rows['row1'] = "TestStudent"
print(table_rows)
print()


# Delete an item from a dictionary
# del table_rows["row1"]
# print(table_rows)

# Delete an entire dictionary using clear()
# table_rows.clear()
# print(table_rows)


# To extend or include a dict object in an existing dict object
external_table = {"row5": "Student5", "row6": "Student6"}
table_rows.update(external_table)
print(table_rows)

# Copy a dict object
new_table = table_rows.copy()
new_table1 = copy.copy(table_rows)
print(new_table)
print(new_table1)


table_rows.get("row1")
table_rows.pop("row1")


# Test for membership
if "row1" in table_rows:
    print("Got you!")


# Retrieve all keys
print(table_rows.keys())


# Retrieve the par of key/values
print(table_rows.items())


# TODO: Looping through dictionaries. Print each item on a line
# FIXME: This has been done! See what you can do with it!

# table2 = {}
# for k in table_rows:
#     table2[k] = table_rows[k]
#
# print(table2)

for k, v in table_rows.items():
    print(k + ": " + v)


#
# print(len(table_rows))
# print(sorted(table_rows, reverse=True))
# print(table_rows)
#
#
# # Retrieve item
# TABLE_ROWS = {"row1": "Student1", "row2": "Student2"}
# print(TABLE_ROWS["row1"])
#
# # Add new item
# TABLE_ROWS["row3"] = "Student3"
#
# # Modify existing item
# TABLE_ROWS["row2"] = "Teacher2"
#
# print(TABLE_ROWS)
#
#
# # Delete item
# del TABLE_ROWS["row2"]
# print(TABLE_ROWS)
#
#
# # Combining dictionaries
# TABLE1 = {"row1": "Student1", "row2": "Student2"}
# TABLE2 = {"row3": "Student4", "row4": "Student4"}
#
# TABLE1.update(TABLE2)
# print(TABLE1)
#
#
# # Clear a dictionary
# TABLE2.clear()
# print(TABLE2)
#
#
# # Test for Membership
# CHECK = "row1" in TABLE1  # Check using the item's key
# print(CHECK)
#
#
# # Retrieve all keys
# KEYS = TABLE1.keys()
# print(KEYS)
#
#
# # Get key-value pairs
# PAIR = TABLE1.items()
# print(PAIR)
#

