#!/usr/bin/env python2.7
# imports the 'argv' module from 'sys'
from sys import argv
# sets the argv variables as the script name and a file name the user inputs
script, input_file = argv
# defines a function called 'print_all' with the argument 'f'
def print_all(f):
# reads the contents of the 'f' argument and then prints it
		print f.read()
# defines a function called 'rewind' which takes the argument 'f'
def rewind(f):
# 'f' is the file you're working with
# 0 means your reference point is the beginning of the file
# 1 means your reference point is the current files position
# 2 means your reference point is the end of the file
# I think this line brings the file pointer back to the beginning of the file 
    f.seek(0)
# defines a function called 'print_a_line' which takes two arguments: line_count and f
def print_a_line(line_count, f):
# prints the line count then 1 line from file 'f'
# f.readline() will read one line from f -
# - after that the file pointer will be at the start of the next line
    print line_count, f.readline(),

# set current_file variable to a file pointer to input_file
current_file = open(input_file)
# print string
print "First let's print the whole file:\n"
# call print_all function with current_file as an argument
print_all(current_file)
# print string
print "Now let's rewind, kind of like a tape."
# call rewind function with current_file as an argument
rewind(current_file)
# print string
print "Let's print three lines:"
# set the current_line to 1
current_line = 1
# call print_a_line function with current_line and current_file as arguments
print_a_line(current_line, current_file)

# set current_line to itself + 1
current_line += 1 #current_line + 1 ## updated to += per study drill
# call print_a_line function with current_line and current_file as arguments
print_a_line(current_line, current_file)
# set current_line to itself + 1
current_line += 1 #current_line + 1 ## updated to += per study drill
# call print_a_line function with current_line and current_file as arguments
print_a_line(current_line, current_file)
