
color1 = input("input first color: ").lower()
print(f"color 1 is: {color1}")

color2 = input("input second color: ").lower()
print(f"color 2 is: {color2} ")

colors = [color1, color2]

if 'yellow' and 'red' in colors:
    print(f"the color mix of {color1} and {color2} is 'Orange'. ")
elif 'blue' and 'green' in colors:
    print(f"the color mix of {color1} and {color2} is 'purple'. ")
else:
    print(f"the color mix of {color1} and {color2} is not a primary color. ")

# if color1 or color2 == 'yellow' or 'red':
#     print(f"the color mix of {color1} and { color2} is 'Orange'. ")
# elif color1 or color2 == 'blue' or 'green':
#     print(f"the color mix of {color1} and { color2} is 'purple'. ")
# else:
#     print(f"the color mix of {color1} and {color2} is not a primary color. ")