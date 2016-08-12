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

class Death(Scene):

		def enter(self):
				print "You died. Tough break kid."
				exit(1)
								
class CentralCorridor(Scene):

		def enter(self):
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
				
				action = raw_input("> ")
				
				if action == "shoot!":
						print "Quick on the draw you yank out your blaster and fire it at the Gothon."
						print "His clown costume is flowing and moving around his body, which throws"
						print "off your aim.  Your laser hits his costume but misses him entirely.  This"
						print "completely ruins his brand new costume his mother bought him, which"
						print "makes him fly into an insane rage and blast you repeatedly in the face until"
						print "you are dead.  Then he eats you."
						return 'death'
						
				elif action == "dodge!":
						print "Like a world class boxer you dodge, weave, slip and slide right"
						print "as the Gothon's blaster cranks a laser past your head."
						print "In the middle of your artful dodge your foot slips and you"
						print "bang your head on the metal wall and pass out."
						print "You wake up shortly after only to die as the Gothon stomps on"
						print "your head and eats you."
						return 'death'
				elif action == "tell a joke":
						print "Lucky for you they made you learn Gothon insults in the academy."
						print "You tell the one Gothon joke you know:"
						print "Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr."
						print "The Gothon stops, tries not to laugh, then busts out laughing and can't move."
						print "While he's laughing you run up and shoot him square in the head"
						print "putting him down, then jump through the Weapon Armory door."
						return 'laser_weapon_armory'
				else:
						print "DOES NOT COMPUTE!"
						return 'central_corridor'

class LaserWeaponArmory(Scene):

		def enter(self):
				print "lasers"

class TheBridge(Scene):

		def enter(self):
				print "bridge"

class EscapePod(Scene):

		def enter(self):
				print "escapepod"
				
class Finished(Scene):
		
		def enter(self):
				print "You won! Good job."
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
				
		def next_scene(self, scene_name):
				# Map.scenes refers to the scene from the dictionary file
				val = Map.scenes.get(scene_name)
				return val
				
		def opening_scene(self):
				return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()

print "Successful"