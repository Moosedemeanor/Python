#!/usr/bin/env python2.7
#imports the argv module from 'sys' - which is a package
from sys import argv
#defines the argv variables as the sript name and filename, which the user inputs
script, filename = argv
#the variable 'txt', when called, will open the file that the user inputs when running the script
txt = open(filename)
#tells the users which filename they input/chose
print "Here's your file %r" % filename
#'txt' is a command - 'read' is an argument to 'txt'.
#this line tells txt to read(print) the contents of the filename the user input/chose
print txt.read()
txt.close()
#asks the user to print the filename again
file_again = raw_input("Type the filename again: >>> ")
#establishes 'file_again' as whatever filename the user inputs
####file_again = raw_input("> ") - replaced with "file_again = raw_input"
#txt_again, when called, will open file_again, which is whatever filename the user input in the last cmd
txt_again = open(file_again)
#the line tells txt_again to read(print) the content of the filename the user input/chose the second time
print txt_again.read()
txt_again.close()