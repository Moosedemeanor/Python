#!/usr/bin/env python2.7
#import adds modules to the Python script
#argv = argument variable - this variable holds the argument you pass to the Python script when you run it.
from sys import argv

#script, first, second, third = argv

#print "The script is called:", script
#print "Your first variable is:", first
#print "Your second variable is:", second
#print "Your third variable is:", third

script = argv

print "The name of this script is:", script
new_name =raw_input("What would you like this script to be called?: ")
print "You've renamed", script, "to", new_name

# argv vs raw_input
# argv requires input at cmdline
# raw_input requires input while the script is running
# you can use int() on argv