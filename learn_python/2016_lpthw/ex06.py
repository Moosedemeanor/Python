#!/usr/bin/env python2.7

# A string is usually a bit of text you want to display to someone,
# or 'export' out of the program.
# Python processes string by using " (double-quotes) or
# ' (single quotes) around text.

# Establishes 'x' as a string and allows you to change the amount of people with '%d'
x = "There are %d types of people." % 10
# The variable 'binary' equals the string 'binary'
binary = "binary"
# The variable 'do_not' equals the string 'don't'
do_not = "don't"
# The variable 'y' is made of a string that includes format characters for input
y = "Those who know %s and those who %s." % (binary, do_not)

# Prints the string 'x' to the program
print x
# Prints the string 'y' to the program
print y

# Prints the written string and uses the string 'x' as input
print "I said: %r." % x
# Prints the written string and uses the string 'y' as input
print "I also said: '%s'." % y

# Sets the variable 'hilarious' as 'False'
hilarious = False
# Sets the variable 'joke_evaluation' as a string with input using %r 
# '%r' is used for debugging, it displays the 'raw' data of the variable
joke_evaluation = "Isn't that joke so funny?! %r"

# Prints the results of variable 'joke_evaluation' and 'hilarious'
print joke_evaluation % hilarious

# Establishes the variable 'w' as the shown string
w = "This is the left side of..."
# Establishes the variable 'e' as the shown string
e = "a string with a right side."

# Prints the variables 'w' + 'e'
# This works because this line is concatenating the variables w and e.
print w + e

# %r is for debugging since it displays "raw" data of a variable
# %s is a string formatting syntax
# %d is a integer formatting syntax
