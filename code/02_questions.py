# Let's take input and format the result.

name=input("What is your name? ")
age=input("What is your age? ")

# It's often more useful to use .format() for greater control.
# The "{}" is the format character
print("{} is {} years old.".format(name, age))
