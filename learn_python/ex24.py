#!/usr/bin/env python2.7
# print string
print "Let's practice everything."
# print string using escapes, newlines, and tabs
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'
# set the value to variable 'poem'
poem = """
\tThe lovel world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n \t \twhere there is none.
"""
# print string
print "-------------"
# print the contents of the variable 'poem'
print poem
# print string
print "-------------"
# defines the variable 'five' using an equation that equals '5'
five = 10 - 2 + 3 - 6
# print a string and call the variable 'five'
print "The should be five: %s" % five
# define the function 'secret_formula' which takes the argument 'started'
def secret_formula(started):
		# define variable jelly_bean as the argument 'started' multiplied 500
		jelly_beans = started * 500
		# define variable jars as the variable jelly_beans divided by 1000
		jars = jelly_beans / 1000
		# define variable crates as the variable jars divided by 100
		crates = jars / 100
		# returns the values of jelly_beans, jars, and crates when the function is called
		return jelly_beans, jars, crates
# establish the starting_point	
start_point = int(raw_input("Enter a starting point for the recipe: "))
# sets beans, jars, and crates as the returned output of secret_formula(start_point)
beans, jars, crates = secret_formula(start_point)
# print string and call the variable start_point
print "With a starting point of: %d" % start_point
# print the values of beans, jars, and crates returned from calling secret_formula 
# with an argument of 10000
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)
# set start_point as the orignal value divided by 10
start_point /= 10
# print string
print "We can also do that this way:"
# print string and call secret_formula with the new reduced start_point value
print "We'd have %d beans, %d jars, and %d crates" % secret_formula(start_point)