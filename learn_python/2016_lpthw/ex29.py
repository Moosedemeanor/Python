#!/usr/bin/env python2.7

people = int(raw_input("How many people are there?: "))
cats = int(raw_input("How many cats are there?: "))
dogs = int(raw_input("How many dogs are there?: "))


if people < cats:
		print "Too many cats! The world is doomed!"
		
if people > cats:
		print "Not many cats! The world is saved!"
		
if people < dogs:
		print "The world is drooled on!"
		
if people > dogs:
		print "The world is dry!"
		
#dogs += 5

if people >= dogs:
		print "People are greater than or equal to dogs."

if people <= dogs:
		print "People are less than or equal to dogs."

if people == dogs:
		print "People are dogs"
		
if people >= cats:
		print "People are greater than or equal to cats."

if people <= cats:
		print "People are less than or equal to cats."

if people == cats:
		print "People are cats"
		
if cats > dogs:
		print "There are more cats than dogs!"
		
if dogs > cats:
		print "There are more dogs than cats!"