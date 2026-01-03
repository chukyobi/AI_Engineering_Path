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







# Tuples (Immutable Ordered Collection) - Not popularly used
# ----------------------------------------------------------

empty_tuple = () # or tuple()
list_data = [0,1,2,3,4,5,6,7,8,9]  # List can be modified  (Mutable)
data = (0, 1, 2, 3, 4, 5, 7, 0, 3, 4, 8)  #Tuples can't be modified (Immutable)
data_pts = ((0,0,0), (1,2,3), (2,4,6))   # Nested Tuples

# Get single List Item
print(data[0])
print(data[2])
print(data[5])
print(data_pts[1])

print(sorted(data)) # Sorted on a tuple sorts the tuple and turns it into a list
#if you want to convert the list back to a tuple
print(tuple(sorted(data)))  #converts list into tuple

# Tuple methods (Built-In Functionality)
data = (0, 1, 2, 3, 4, 5, 7, 0, 3, 4, 8)
print(data.count(3))
print(data.index(3))






# SETS (Unique, Mutable Unordered Collection)
# ----------------------------------------------------------

new_set = set()
set_items = { 10, 20, 30, 10, 20, 'AB', 'BA', 'AB', True, True, False}

print(set_items) # P.S: don't always rely on the order of your sets, it will always print at random no mater how many times it ran

# Convert List/Tuples to SETS

data_list = ['amaka', 'joy', 'emeka', 'chukwudi', 'joy', 'oge', 'amaka', 'chioma']
data_set = set(data_list)
data_set_list = list(data_set)

print(data_list)
print(data_set)
print(data_set_list)

# SET Methods (Built-In functionality)

set_items = { 10, 20, 30, 10, 20, 'AB', 'BA', 'AB', True, True, False}

# copy_set = set_items.copy()  #copies the set to have an independent copy
# removed = set_items.pop()  #removes and returns a random element in the set
# set_items.clear() #removes all elements
set_items.remove(10) #removes element but throws an error if it does not exist
set_items.discard(3) #removes element, no error if it does not exist
set_items.add(15)   #add a single element

print(set_items)


# SET Methods: Compare methods
a = {1,2,3,4}
b= {3,4,5,6}

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a.symmetric_difference(b))
print(a.issubset(b))
print(a.issuperset(b))


# Popular Functions with Sets
a = {1,2,3,4,5}

print(len(a)) # Count elements
print(min(a)) #Minimum
print(max(a)) #Maximum
print(sum(a)) #Sum
print(sorted(a)) # sorted list




# DICTIONARIES ---- (Mapped Ordered* Mutable Collection)
# --------------------------------------------------------

empty_dict = {}
dict_example = {
    'key1': 'value1',
    'key2': 'value2'
}

#Get Items
print(dict_example['key1'])
print(dict_example.get('key2'))
print(dict_example.setdefault('key1', 'non-value'))


# Adjust and modify data
#-----------------------
dict_example['key1'] = "my name is chukwudi"
dict_example['key3'] = "value3"
print(dict_example)

print('key1' in dict_example)  #check for keys if they exist in dictionary
print('key4' in dict_example)


#Dict Methods ( Built In Functionality)

print(list(dict_example.keys()))
print(list(dict_example.values()))
print(list(dict_example.items()))
