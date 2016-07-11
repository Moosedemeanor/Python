#!/usr/bin/env python2.7

# The following fields establish variables.
name = 'Charles D. Bouley'
age = 26
height = 69.0 # inches
weight = 165.00 # lbs
eyes = 'Brown'
teeth = 'White'
hair = 'Brown'

# The below performs measurement conversion
#### HEIGHT #### 
inch = height
centimeter = 2.54
height_in_centimeter = inch * centimeter
#### WEIGHT ####
lbs = weight
kilograms = 0.453592
weight_in_kilo = lbs * kilograms

#### PRINT OUT ####
print "Let's talk about %s." % name
print "He's %d inches tall." % height
# '.2' rounds the floating point decimal to the second place. 
# 'f' converts characters to floating point variables.
print "He's %.2f centimeters tall." % height_in_centimeter
print "He's %d pounds heavy." % weight
print "He's %.2f kilograms heavy." % weight_in_kilo
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

print "If I add %d, %d, and %d I get %d." % (age, height, 
	weight, age + height + weight)