#String types
# Strings are no more than an organised list/array of characters
# You declare strings using quotes
#Declaring a string
my_string = "I'm an amazing string"
my_string2 = "So am I"
print(my_string)
print(type(my_string))

#Concatenation

print(my_string +"_" + my_string2)
joint_string = my_string +"_" + my_string2
print(joint_string)

#Interpolation -putting something inside a string

age = 21
name = 'Anne'
example_text = f"{name} is {age} years old"
print(example_text)
example_text1 = f"{name} is {age*2} years old"
print(example_text1)


# Useful methods(strip, lower and upper, count, length, capitalize,Split)

example_text3 = "  Hello "
print(example_text3.strip())
print(example_text3.count('H'))
print(len(example_text3.strip()))
# len is a function so it is put outside whereas others are methods so you can directly aattach
print(example_text3.lower().strip().capitalize())


#Casting-Changing things into strings or numbers