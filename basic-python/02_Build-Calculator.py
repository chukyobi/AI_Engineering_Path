#Learning about Input abd Data Conversion

str_num_a = input('Enter a First Number: ')
str_num_b = input('Enter a Second Number: ')

num_a = int(str_num_a)
num_b = int(str_num_b)

total = num_a + num_b
print(f" the sum of num_a and num_b is: {total}")


# DataTypes Functions

# str()
# float()
# int()
# bool()
#
# list()
# tuple()
# set()
# dict()

# Convert DataTypes
# Numbers --------
x = 10
str_x = str(x)  # converts integer to string: '10'
float_x = float(x) # converts integer to float: 10.0
bool_x = bool(x)  # convert integer to boolean: True (non-zero is true)
bool_neg_x = bool(0) #converts 0 to a boolean: Always false

# Strings --------
s = "123"
int_s = str(s)  # converts string to integer: 123
float_s = float(s) # converts integer to float: 123.0
bool_s = bool(s)  # convert integer to boolean: True (if not empty)
bool_empty = bool("") #convert empty string to boolean: Always false

# Booleans --------
bool_true = bool(1)   # True
bool_false = bool(0)  # False
bool_list = bool([])  # convert empty list to boolean: False
bool_list_of_list = bool([[], [], []]) # convert list of empty lists to boolean : True
bool_dict = bool({}) # convert empty dict to boolean: False
bool_str = bool("Chukwudi")
