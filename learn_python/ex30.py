#!/usr/bin/env python2.7
# Ask for variable inputs
people = int(raw_input("How many people do we have? "))
cars = int(raw_input("How many cars are there? "))
trucks = int(raw_input("How many trucks are there? "))
# If there are more cars than people - print "We should take the cars."
if cars > people:
		print "We should take the cars."
# If there are less cars than people - print "We should not take the cars."
elif	cars < people:
		print "We should not take the cars."
# If those two conditions aren't met - print "We can't decide."
else:
		print "We can't decide."

if trucks > cars:
		print "That's too many trucks"
elif trucks < cars:
		print "Maybe we could take the trucks."
else:
		print "We still can't decide."
		
if people > trucks:
		print "Alright, let's just take the trucks."
else:
		print "Fine, let's stay home then."
		
if cars > people or trucks < cars:
		print "There are more cars than people or less trucks than cars."	