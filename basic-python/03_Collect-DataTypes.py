#  Collection Data-Types in Python (List | Tuple | Set | Dictionary )
#  -------------------------------------------------------------
# List   |          | Mutable    | Ordered    | Collection    |  90%+
# Tuple  |          | Immutable  | Ordered    | Collection    |
# Set    | Unique   | Mutable    | Unordered  | Collection    |
# Dict   | Mapped   | Mutable    | Ordered *  | Collection    |
#----------------------------------------------------------------

#LIST (Mutable Ordered Collection) - Used in 90% Use cases
# ----------------------------------------------------------

# Syntax
empty_list = [] # or list()
my_list = ['wall', 'floor', 'roof', 'ceiling']
print(my_list)

# Get Single List Item
print(my_list[0]) # First Item (count starts from 0)
print(my_list[1]) # Second Item (count starts from 0)
print(my_list[-1]) # last Item
print(my_list[-2]) # Second Last Item
# print(my_list[100]) #IndexError: list Index out of range

# Get Multiple Items from the list
# slice --> [start: stop ] stop is the index value of the item after the particular item you want to print--------

my_list = ['wall', 'roof', 'fan', 'block', 'car', 'book']

print(my_list[:3])
print(my_list[1:3])
print(my_list[1:])
print(my_list[0:2])
print(my_list[::2])
print(my_list[1::2])
print(my_list[1:4:2])

