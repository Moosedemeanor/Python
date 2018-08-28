#!/usr/bin/env python2.7

# objects are like 'import', but for classes
# what you 'instantiate' a class you 'create' a class.
		# when you instantiate a class, what you get is called an object.
# you instantiate (create) a class by calling the class like it's a function
class MyStuff(object):
		# __init__ is used to initialize a newly created empty object
		# self is the new empty object that Python created; you can set variables on it
		def __init__(self):
				self.tangerine = "And now a thousand years between"
				
		def apple(self):
				print "I AM CLASSY APPLES!"
				
# Python does not give you a class, but instead it uses is as a blueprint -
# for building a copy of that type of thing

# classes are like blueprints or definitions for creating new mini-modules.
# instantiation is how you make one of these mini-modules and import it-
		# at the same time. "Instantiate" just means to create an object from the class.
# The resulting created mini-module is called an object and you then assign it to- 
		# a variable to work with it.			

# class style
thing = MyStuff()
thing.apple()
print thing.tangerine

class Song(object):

		def __init__(self, lyrics):
				self.lyrics = lyrics
		
		def sing_me_a_song(self):
				for line in self.lyrics:
						print line
						
		def yell_me_a_song(self):
				for line in self.lyrics:
						print line.upper()
						
happy_bday = Song(["Happy birthday to you",
									 "I don't want to get sued",
									 "So I'll stop right there"])
									 
bulls_on_parade = Song(["They rally around tha family",
												"With pockets full of shells"])
												
byob_system_of_a_down = Song(["Everybody's going to the party, have a real good time",
															"Dancing in the desert, blowing up the sunshine"])
																	
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

byob_system_of_a_down.yell_me_a_song()