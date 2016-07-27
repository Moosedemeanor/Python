#!/usr/bin/env python2.7
# define a function called 'add' which takes the arguments 'a' and 'b'
def add(a, b):
		# print string with arguments 'a' and 'b'
		print "ADDING %d + %d" % (a, b)
		# A function can take input and return some output - usually a single value.
		# print() writes, i.e. 'prints' a string in the console.
		# return' causes your function to exit and hand back a value to the caller.
		return a + b
		
def subtract(a, b):
		print "SUBTRACTING %d - %d" % (a, b)
		return a - b
		
def multiply(a, b):
		print "MULTIPLYING %d * %d:" % (a, b)
		return a * b
		
def divide(a, b):
		print "DIVIDING %d / %d" % (a, b)
		return a / b

# print string
print "Let's do some math with just functions!"

# establish variables taking argument inputs
#a, b = [float(x) for x in raw_input("Enter two numbers for age here: ").split()]
#age = add(a, b)
age = add(20, 6)
height = subtract(a, b)
weight = multiply(82, 2)
iq = divide(100, 2)

# print string with arguments 'age', 'height', 'weight', 'iq' which are results -
# - of the add, subtract, multiply, and divide functions
print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)
# example: function 'age' = add(a, b) which returns a + b
# If a = 20 and b = 6 then 'add' returns 26. If 'add' returns '26' then age = '26'

### Extra Credit Puzzle ###
print "Here is a puzzle."
""" start with the most encapsulated equation. 
iq(50) / 2 = 25
multiply weight(164) * 25 = 4100
subtract height(69) - 4100 = -4031
add age(26) + -4031 = -4005
"""
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"