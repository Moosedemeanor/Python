#!/usr/bin/env python2.7

# create a class named Parent that is-a object
class Parent(object):
		# define the implicit function with the parameter self
		def implicit(self):
				print "PARENT implicit()"
		# define the override function with the parameter self
		def override(self):
				print "PARENT override()"
		# define the altered function with the parameter self
		def altered(self):
				print "PARENT altered()"
# create a class named Child that is-a Parent - inherits from Parent class
class Child(Parent):
		# tells Python to create an empty block for Child
		pass
		# defines the override function for Child - overrides the Parent class function
		def override(self):
				print "CHILD override()"
		# defines the altered function for Child - overrides the Parent override function
		def altered(self):
				# print string for the Child function altered
				print "CHILD, BEFORE PARENT altered()"
				# super will call the parent class version of the function and print it here
				super(Child, self).altered()
				# print another string for the Child function altered
				print "CHILD, AFTER PARENT altered()"

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()

""" Inheritance or Composition
- Both attempt to solve the problem of reusable code.
- Inheritance solves this problem by creating a machanism for you to have implied 
	features in base classes
- Composition solves this problem by giving you modules and the ability to call
	call functions in other classes.
	
1. Avoid multiple inheritance at all costs, as it's too complex to be reliable. If 
	 you're stuck with it, then be prepared to know thee class hierarchy and spend time 
	 finding where everything is coming from.
2. Use composition to package code into modules that are used in many different 
	 unrelated places and situations.
3. Use inheritance only when there are clearly related reusable pieces of code that 
   fit under a single common concept or if you have to because of something you're using.
"""