#!/usr/bin/env python2.7
# http://code.tutsplus.com/articles/python-from-scratch-object-oriented-programming--net-21476
# 'methods' are functions contained within a class; they ALWAYS need the argument 'self'
# this passes the current object to that method as the first argument
# inheritance is the process of making a new class based around a parent class and 
		# allowing the new class to inherit the features of the parent "base" class

class pet:
		number_of_legs = 0
		
		def sleep(self):
				print "zzz"
				
		def count_legs(self):
				print "I have %s legs" % self.number_of_legs

class dog(pet):

		def bark(self):
				print "Woof"
				
class fish(pet):

		def swim(self):
				print "I can swim underwater"

doug = dog()
doug.number_of_legs = int(raw_input("How many legs does the pet have? "))
doug.count_legs()
doug.bark()
doug.sleep()

nemo = fish()
nemo.number_of_legs = int(raw_input("How many legs does the pet have? "))
nemo.count_legs()
nemo.swim()