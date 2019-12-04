"""
List comprehensions are one cool and unique feature of Python.
They essentially act as a terse and concise way of initializing
and populating a list given some expression that specifies how
the list should be populated. 

Take a look at https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
for more info regarding list comprehensions.
"""

# Write a list comprehension to produce the array [1, 2, 3, 4, 5]

y = []
for n in range(5):
    y.append(n+1)

print(y)

# Write a list comprehension to produce the cubes of the numbers 0-9:
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

y = [num**3 for num in range(10)]

# for num in range(10):
#     y.append(num**3)

print('len of y cubes', len(y))
print('cubing y', y)

# list comprehension to double every number in the singles array
singles = [1,2,3,4,5,6,7,8]
doubles = [num**2 for num in singles]
print(doubles)


# Write a list comprehension to produce the uppercase version of all the
# elements in array a. Hint: "foo".upper() is "FOO".

a = ["foo", "bar", "baz"]

y = [word.upper() for word in a]
# for word in a:
#     y.append(word.upper())

print('list comprehension uppercasing', y)

# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.

x = input("Enter comma-separated numbers: ").split(',')

evens = x[::2]  #without using list comprehension, setting all even elements to a new array evens
# print('evens',evens)
# print('evens', evens)

# What do you need between the square brackets to make it work?

for num in x:
    print(type(num))  


y = [inp for inp in x if int(inp) % 2 == 0]  #had to make each input value an integer because python cant do modulo division on a string
#using list comprehension to generate a new array of only the even inputs from x
print('even inputs', y)
