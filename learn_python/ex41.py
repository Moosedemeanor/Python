#!/usr/bin/env python2.7

# Word Drills
"""
class - tells python to make a new type of thing
object - two meanings: the most basic type of thing, and any instance of some thing
instance - what you get when you tell python to create a class
def - how you define a function inside a class
self - inside the functions in a class, self is a varibale for the instance/object being accessed
inheritance - the concept that one class can inherit traits from another class, much like you and your parents
composition - the concept that a class can be composed of other classes as parts, much like how a car has wheels
attribute - a property classes have that are from composition and are usualy variables
is-a - a phrase to say that someting inherits from another, as in a "salmon" is-a "fish"
has-a - a phrase to say that something is composed of other things or has a trait, as in "a salmon has-a mouth"
"""
# Phase Drills
"""
class X(Y)
		"Make a class named X that is-a Y."
class X(object): def __init__(self, J)
		"class X has-a __init__ that takes self and J parameters."
class X(object): def M(self, J)
		"class X has-a function named M that takes self and J parameters."
foo = X()
		"set foo to an instance of class X."
foo.M(J)
		"from foo get the M function, and call it with parameters self, J."
foo.K = Q
		"from foo get the K attribute and set it to Q."
"""
