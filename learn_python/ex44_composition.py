#!/usr/bin/env python2.7
# Composition

class Other(object):
		def override(self):
				print "OTHER override() "
				
		def implicit(self):
				print "OTHER implicit() "
				
		def altered(self):	
				print "OTHER altered() "

class Child(object):
		def __init__(self):
				self.other = Other()
				
		def implicit(self):
				self.other.implicit()
				
		def override(self):
				print "CHILD override() "
				
		def altered(self):
				print "CHILD, BEFORE OTHER altered() "
				self.other.altered()
				print "CHILD, AFTER OTHER altered() "
				
son = Child()

son.implicit()
son.override()
son.altered()

""" Inheritance or Composition
- Both attempt to solve the problem of reusable code.
- Inheritance solves this problem by creating a machanism for you to have implied 
	features in base classes
- Composition solves this problem by giving you modules and the ability to call
	call functions in other classes.
	