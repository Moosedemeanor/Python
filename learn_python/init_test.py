#!/usr/bin/env python2.7

class Point():
		
		def __init__(self, x=0, y=0):
				self.x = x
				self.y = y
				print "We will now plot x=%d and y=%d" % (x , y)
				
x = int(raw_input("Input Point X >> "))
y = int(raw_input("Input Point Y >> "))
	
point = Point(x, y)

"""
init - Initilization
init is used to create the intial conditions that the object should have - default values

"""
