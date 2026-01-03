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


# Replace List Items
my_list = ['wall', 'roof', 'fan', 'block', 'car', 'book']

my_list[2] = 'cake' # replaces fan (index 2) with cake in the list
my_list[-1] = 'last' # Replaces last item in the list
my_list[1:3] = ['a', 'b']



# Slicing Use-Case Example
#------ differentiate between a header and its items in a table -------
my_list = ['Categories', 'wall', 'roof', 'fan', 'block', 'car', 'book']

header = my_list[0]
data = my_list[1:]

print(header)
print(data)


# Membership Operators (Necessary for Logic)
check_in = 'wall' in my_list
check_not = 'food' in my_list
check = 'book' not in my_list

print(check_in)
print(check_not)
print(check)


# Popular Functions with Lists

my_list = ['wall', 'floor', 'roof', 'ceiling']
numbers = [10, 20, 30, 40, 50]

print(len(my_list)) # Get Length
print(sorted(my_list)) # Create a new Sorted list in Alphabetical order or ascending/descending order for number lists
print(sum(numbers))  # sum total numbers in a list
print (min(numbers)) # Get Min Value in the List
print (max(numbers)) # Get Max Value in the List


# List Methods (Built-In Functionality)

my_list = ['wall', 'floor', 'roof', 'ceiling']
my_list2 = ['food', 'pot']

my_list.append('door') # Add Single Item
my_list.append('window')

my_list.extend(my_list2) # Joins More than 1 List
my_list += ['car', 'fan', 'floor'] # Joins More than 1 List

my_list.sort()  # Sorts List Alphanumerically
print(my_list.count('floor')) # Counts number of Item instances in a lIst
print(my_list.index('floor')) # finds the index of Item  in a lIst
my_list.insert(3,'gate') # Inserts Item at a certain Index
my_list.remove('window') # Remove Value from List
item = my_list.pop(2) # remove value from list and return it
my_list.reverse()  #reverse list order
my_list.clear()   #clear all items from list # or---
my_list = []
y = my_list.copy()  #Creates an Independent copy of a list!

print(my_list)
print(item)

# Nested List

points = [
    [0,0,0],
    [2,2,0],
    [4,4,0],
    [6,6,0],
]

pt2 = points[1]

print(points[1][1])
print(pt2[0], pt2[1], pt2[2])

# Loops (Introduction)
my_list = ['wall', 'floor', 'roof', 'ceiling']

for i in my_list:
    print(i)
    print(i)
