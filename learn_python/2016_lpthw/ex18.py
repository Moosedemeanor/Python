#!/usr/bin/env python2.7

# functions do three things
	# they name pieces of code the way variables name strings and numbers
	# they take arguments the way your scripts take 'argv'
	# using 1 and 2 they let you make your own "mini-scripts" or "tiny cmds"

# 'def' - defines a function

# defines a function and names it 'print_two'
# We also tell it we want *argv which is a lot like the argv parameter
#			 This HAS to go inside of the ()
# The * in *args tells Python to tak all the arguments to the function and put them in args.
def print_two(*args):
	# Make sure to end the 'def' with a ':' and then being indenting
    arg1, arg2 = args
    print "arg1: %s, arg2: %s" % (arg1, arg2)
	
# *args in the last function was pointless, do:
def print_two_again(arg1, arg2):
		# Make sure to indent four spaces
    print "arg1: %s, arg2: %s" % (arg1, arg2)

# this function takes one argument
def print_one(arg1):
    print "arg1: %s" % arg1
	
# this function takes no argument
def print_none():
    print "I got nothin'."

print_two("Charles","Bouley")
print_two_again("Charles" ,"Bouley")
print_one("First!")
print_none()