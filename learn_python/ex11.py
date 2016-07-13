#!/usr/bin/env python2.7

# Ending each print line with a , (comma) stops print from ending the line with a newline character
# raw_input() returns a string and input() tries to run the input as a Python expression
print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)
		
# Getting numbers
# x = int(raw_input()) - This will get the number as a string form raw_input() 
# then convert it to an integer using int()

# Python lines should be less than 80 characters long.