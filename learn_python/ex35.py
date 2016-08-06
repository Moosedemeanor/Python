#!/usr/bin/env python2.7

from sys import exit

"""			
-----------------------------------------------------------------
|                                      |                        |
|                                      |                        |
|           GOLD ROOM                  |                        |
|                                      |                        |
|                                      |                        |
|                                      |                        |
|-------------______-------------------|                        |
|                                      |                        |
|                                      |      Cthulhu ROOM      |
|                   BEAR ROOM          |                        |
|                                      |                        |
|                                      |                        |
|                   Left Door >        |       < Right Door     |
--------------------------------______---______------------------
|                                                               |
|                                                               |
-----------------------------------------------------------------
                                   Dark Room
"""
# defines the function 'gold_room' with no arguments		  					
def gold_room():
		# print string
    print "This room is full of gold.  How much do you take?"
		# define variable choice with an integer input
    choice = int(raw_input("> "))
    # define variable how_much as the integer entered into the variable choice
    try:
        how_much = int(choice)
    except:
        print "I'm pretty sure that wasn't a number. Maybe you should try again."
        gold_room()
    # if the integer input into how_much is less than or equal to 50
    if how_much <= 50:
        # print string
        print "Nice, you're not greedy, you win!"
        # gracefully end the script
        exit(0)
    # else if the input for how_much is greater than 50
    elif how_much > 50:
    		# call the function 'dead' with the argument string provided
        dead("You greedy bastard!")
    # if neither of those options happen
    else:
    		# call the function 'dead' with the argument string provided
        dead("Man, learn to type a number.")
# define the function 'bear_room' with no argument        
def bear_room():
		# print strings
		print "There is a bear here."
		print "The bear has a bunch of honey."
		print "The fat bear is in front of another door."
		print "How are you going to move the bear?"
		# define the variable bear_moved as False
		bear_moved = False
		# while True will run the while loop until it is broken
		while True:
				# while True, the user will be prompted to enter an input for 'choice'
				choice = raw_input("> ")
				# if the input == "take honey"
				if choice == "take honey":
						# call the function 'dead' with the argument string provided
						dead("The bear looks at you then slaps your face off.")
				# if the input == "taunt bear" and the bear has not already been moved from the door
				elif choice == "taunt bear" and not bear_moved:
						# print string
						print "The bear has moved from the door. You can go through it now."
						# update the variable 'bear_moved' to True
						bear_moved = True
				# if the user enters the input "taunt bear" and the bear has already moved from the door
				elif choice == "taunt bear" and bear_moved:
						# call the function 'dead' with the argument string provided - don't taunt the bear twice
						dead("The bear gets pissed off and chews your leg off.")
				# if the user inputs "open door" and the bear has already moved print string	
				elif choice == "open door" and bear_moved:
						# break the while loop and call the function 'gold_room' with no argument
						gold_room()
				# if the user does not enter one of the above choice options, print string		
				else:
						print "I got no idea what that means."
# define the function 'cthulhu_room' with no arguments
def cthulhu_room():
		# print strings
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"

    choice = raw_input("> ")
		# if the user inputs 'flee' they will start the game at the beginning 
    if "flee" in choice:
        start()
    # if the user inputs head, call the function dead with the argument string provided    
    elif "head" in choice:
        dead("Well that was tasty!")
    # if the user inputs anything else, run call the function 'cthulhu_room' again     
    else:
        cthulhu_room()
# define the function 'dead' with the argument 'why'        
def dead(why):
		# when 'dead' is called if will print the argument provided with 'Good job" amended
		print why, "Good job!"
		# end the script gracefully
		exit(0)
# define the function 'start' with no argument - this launches the game
def start():
		# print strings
		print "You are in a dark room."
		print "There is a door to your right and left."
		print "Which one do you take?"
		
		choice = raw_input("> ")
		# if the user inputs 'left' call the 'bear_room' function with no arguments
		if choice == "left":
				bear_room()
		# if the user inputs 'right' call the 'cthulhu_room' function with no arguments
		elif choice == "right":
				cthulhu_room()
		# if the user inputs anything else, kill them
		else:
				dead("You stumble around the room until you starve.")
# call the function 'start' with no arguments - starts the game			
start()