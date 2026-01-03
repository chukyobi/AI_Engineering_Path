from decimal import Decimal
import math

x = 10
y = 11
z = x + y
print(f"the answer is {z}")
print("the correct answer is", z)

mph = 65
totalDistance = 435

time = totalDistance/mph

j = Decimal('0.1')+ Decimal('0.2')

print(time, f"and it can be rounded up to {round(time, 3)}: in 3 decimal places", j)
print(f"{time: .1f}")

if(math.isclose((6-5.7), 0.3)):
    print("true")

text = "chukwudi"

new_text = text[0] + text[3] + text[5]

print(f"the new text is {new_text}")

sentence = "python is a language"

print(sentence[0:8])

address = ''' 43 omoba murphy adetoro street, lekki "county home"
lekki,
lagos,
NG'''
print(address)

items =["bread", "orange", "mango", "salt"]
items.append("tomatoes")

items.insert(2, "avocado")

print(items)

