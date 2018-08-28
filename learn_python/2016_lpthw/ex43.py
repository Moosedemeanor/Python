#!/usr/bin/env python2.7
"""
Basic Object-Oriented Analysis and Design
Process:
1. Write or draw about the problem.
		- Make a list of nouns and verbs in the writings or drawing and how they're related
2. Extract key concept from 1 and research them.
3. Create a class hierarchy and object map for the concepts.
4. Code the classes and a test to run them.
5. Repeat and refine.

Adventure Game: Gothons from Planet Percal #25!
Class Hierarchy
* Map
	- next_scene
	- opening_scene
* Engine
	- play
* Scene
	- enter
	* Death
	* Central Corridor
	* Laser Weapon Armory
	* The Bridge
	* Escape Pod
"""
# exits from Python
from sys import exit
# returns a random integer
from random import randint
# create class Scene that is-a object
class Scene(object):
		# defines the common scene action of 'entering' a scene
		def enter(self):
				print "This scene is not yet configured. Subclass it and implement enter()."
				exit(1)
# define the class Engine that is-a object
class Engine(object):
		# initialize the newly created Engine object with parameters self and scene_map
		def __init__(self, scene_map):
				self.scene_map = scene_map
		# define the play function with the parameter self
		def play(self):
				# current_scene = the opening scene of the scene_map that was used to init Engine
				current_scene = self.scene_map.opening_scene()
				# last_scene == when the last scene of current Map is called - runs : Finished()
				last_scene = self.scene_map.next_scene('finished')
				# while the current_scene is not the last_scene, then:
				while current_scene != last_scene:
						# the next_scene_name == entering the current_scene
						next_scene_name = current_scene.enter()
						# the current_scene is updated to the next scene on the list
						current_scene = self.scene_map.next_scene(next_scene_name)
				# print out the last scene
				current_scene.enter()
# define the class Death that is-a Scene
class Death(Scene):
		# define the function 'enter' with the parameter self
		def enter(self):
				# print string
				print "You died. Tough break kid."
				# exit Python gracefully
				exit(1)
# define the class CentralCorridor that is-a Scene								
class CentralCorridor(Scene):
		# define the function 'enter' with the parameter self
		def enter(self):
				# print string
		 		print "The Gothons of Planet Percal #25 have invaded your ship and destroyed"
				print "your entire crew.  You are the last surviving member and your last"
				print "mission is to get the neutron destruct bomb from the Weapons Armory,"
				print "put it in the bridge, and blow the ship up after getting into an "
				print "escape pod."
				print "\n"
				print "You're running down the central corridor to the Weapons Armory when"
				print "a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume"
				print "flowing around his hate filled body.  He's blocking the door to the"
				print "Armory and about to pull a weapon to blast you."
				# ask the user for an input which will be used for the variable 'action'
				action = raw_input("> ")
				# if loop to filter for user input on action - must be 'shoot', 'dodge', 'tell a joke'
				if action == "shoot":
						print "Quick on the draw you yank out your blaster and fire it at the Gothon."
						print "His clown costume is flowing and moving around his body, which throws"
						print "off your aim.  Your laser hits his costume but misses him entirely.  This"
						print "completely ruins his brand new costume his mother bought him, which"
						print "makes him fly into an insane rage and blast you repeatedly in the face until"
						print "you are dead.  Then he eats you."
						# call the 'death' scene
						return 'death'
				elif action == "dodge":
						print "Like a world class boxer you dodge, weave, slip and slide right"
						print "as the Gothon's blaster cranks a laser past your head."
						print "In the middle of your artful dodge your foot slips and you"
						print "bang your head on the metal wall and pass out."
						print "You wake up shortly after only to die as the Gothon stomps on"
						print "your head and eats you."
						# call the 'death' scene
						return 'death'
				elif action == "tell a joke":
						print "Lucky for you they made you learn Gothon insults in the academy."
						print "You tell the one Gothon joke you know:"
						print "Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr."
						print "The Gothon stops, tries not to laugh, then busts out laughing and can't move."
						print "While he's laughing you run up and shoot him square in the head"
						print "putting him down, then jump through the Weapon Armory door."
						# call the 'laser_weapon_armory' scene - [progress the plot]
						return 'laser_weapon_armory'
				# if one of the three choices is not chosen, print string and start scene over
				else:
						print "DOES NOT COMPUTE!"
						# run the central_corridor scene again
						return 'central_corridor'
# define the class LaserWeaponArmory that is-a Scene
class LaserWeaponArmory(Scene):
		# define the function 'enter' with the parameter self
		def enter(self):
				print "You do a dive roll into the Weapon Armory, crouch and scan the room"
				print "for more Gothons that might be hiding.  It's dead quiet, too quiet."
				print "You stand up and run to the far side of the room and find the"
				print "neutron bomb in its container.  There's a keypad lock on the box"
				print "and you need the code to get the bomb out.  If you get the code"
				print "wrong 10 times then the lock closes forever and you can't"
				print "get the bomb.  The code is 3 digits."
				# establish the lock code
				code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9)) or "cheat"
				# ask the user to guess the lock code
				guess = raw_input("[keypad]> ")
				# define the guesses variable as 0
				guesses = 0
				# while guess does not equal the code and the user has guessed less than 9 times
				# if the user enters the cheat code "777" it will unlock the keypad
				while guess != code and guess != "777" and guesses < 10:
						# print string
						print "BZZZZEDDD!"
						# add 1 to the running count of guesses
						guesses += 1
						# ask the user to guess again until the code is undered or 9 guesses
						guess = raw_input("[keypad]> ")
				# if the user guesses the code correctly
				if guess == code or guess == "777":
						# print string
						print "The container clicks open and the seal breaks, letting gas out."
						print "You grab the neutron bomb and run as fast as you can to the"
						print "bridge where you must place it in the right spot."
						# call 'the_bridge' scene - [progress the plot]
						return 'the_bridge'
				# if the user never guesses the code
				else:
						# print string
						print "The lock buzzes one last time and then you hear a sickening"
						print "melting sound as the mechanism is fused together."
						print "You decide to sit there, and finally the Gothons blow up the"
						print "ship from their ship and you die."
						# call the 'death' scene
						return 'death'
# define the class TheBridge that is-a Scene
class TheBridge(Scene):
		# define the function 'enter' with the parameter self
		def enter(self):
				# print string
				print "You burst onto the Bridge with the netron destruct bomb"
				print "under your arm and surprise 5 Gothons who are trying to"	
				print "take control of the ship.  Each of them has an even uglier"
				print "clown costume than the last.  They haven't pulled their"
				print "weapons out yet, as they see the active bomb under your"
				print "arm and don't want to set it off."
				# ask the user for an input which will be used for the variable 'action'
				action = raw_input("> ")
				# if the user inputs "throw the bomb"
				if action == "throw the bomb":
						# print string
						print "In a panic you throw the bomb at the group of Gothons"
						print "and make a leap for the door.  Right as you drop it a"
						print "Gothon shoots you right in the back killing you."
						print "As you die you see another Gothon frantically try to disarm"
						print "the bomb. You die knowing they will probably blow up when"
						print "it goes off."
						# call the 'death' scene
						return 'death'
				# if the user inputs "slowly place the bomb"
				elif action == "slowly place the bomb":
						# print string
						print "You point your blaster at the bomb under your arm"
						print "and the Gothons put their hands up and start to sweat."
						print "You inch backward to the door, open it, and then carefully"
						print "place the bomb on the floor, pointing your blaster at it."
						print "You then jump back through the door, punch the close button"
						print "and blast the lock so the Gothons can't get out."
						print "Now that the bomb is placed you run to the escape pod to"
						print "get off this tin can.\n"
						# call the 'escape_pod' scene - [progress the plot]
						return 'escape_pod'
				# if the user does not input "throw the bomb" or "slowly place the bomb"
				else:
						# print string
						print "DOES NOT COMPUTE!"
						# run the "the_bridge" scene again
						return "the_bridge"

class EscapePod(Scene):
		# define the function 'enter' with the parameter self
		def enter(self):
				# print string
				print "You rush through the ship desperately trying to make it to"
				print "the escape pod before the whole ship explodes.  It seems like"
				print "hardly any Gothons are on the ship, so your run is clear of"
				print "interference.  You get to the chamber with the escape pods, and"
				print "now need to pick one to take.  Some of them could be damaged"
				print "but you don't have time to look.  There's 5 pods, which one"
				print "do you take?"
				# the good_pod is randomly chosen between int 1 - 5 via randinit 
				good_pod = randint(1,5)
				# ask the user to guess which pod is the undamaged pod - random
				guess = raw_input("[pod #]> ")
				# if the user inputs an int that does not matches the int from 'good_pod' then:
				if int(guess) != good_pod:
						# print string
						print "You jump into pod %s and hit the eject button." % guess
						print "The pod escapes out into the void of space, then"
						print "implodes as the hull ruptures, crushing your body"
						print "into jam jelly."
						# call the 'death' scene
						return 'death'
				# if the user inputs an int that matches the int from 'good_pod' then:
				else:
						# print string
						print "You jump into pod %s and hit the eject button." % guess
						print "The pod easily slides out into space heading to"
						print "the planet below.  As it flies to the planet, you look"
						print "back and see your ship implode then explode like a"
						print "bright star, taking out the Gothon ship at the same"
						print "time.\n"
						# cal the 'finished' scene
						return 'finished'
				
class Finished(Scene):
		# define the function 'enter' with the parameter self
		def enter(self):
				# print string
				print "You won! Good job."
				# call the 'finished' scene
				return 'finished'
					
# define the class Map that is-a object
class Map(object):
		# Establish a definition file for the scenes in this game
		scenes = {
		'central_corridor': CentralCorridor(),
		'laser_weapon_armory': LaserWeaponArmory(),
		'the_bridge': TheBridge(),
		'escape_pod': EscapePod(),
		'death': Death(),
		'finished' : Finished(),
		}
		# initialize the newly created Map object with parameters self and start_scene
		def __init__(self, start_scene):
				# which ever scene is chosen will become 'start_scene'
				self.start_scene = start_scene
		# define the function next_scene with the parameters self and scene_name
		def next_scene(self, scene_name):
				# Map.scenes refers to the scene from the dictionary file
				val = Map.scenes.get(scene_name)
				return val
		# define the function opening_scene with the parameter self
		def opening_scene(self):
				# return the piped in scene as the next_scene and then start that scene
				return self.next_scene(self.start_scene)
# define a_map as the central_corridor Scene
a_map = Map('central_corridor')
# define a-game as calling the Engine class with the parameter self and a_map
a_game = Engine(a_map)
# call the a_game variable with the argument 'play' and the parameter self
a_game.play()