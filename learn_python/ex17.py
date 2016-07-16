#!/usr/bin/env python2.7

from sys import argv
# exists returns 'True' if a file exists and 'False' is not.
from os.path import exists

script, from_file, to_file = argv
# informs the user of the source and destination documents
print "Copying from %s to %s" % (from_file, to_file)
# sets 'in_file' as opening the source file
in_file = open(from_file)
# sets 'indata' as the data being read from 'in_file'/source file
indata = in_file.read()
# 'len' returns the length of an object - in this case, the bytes of indata
print "The input file is %d bytes long" % len(indata)
# this line checks if 'to_file' already exists on the user's system
print "Does the output file exist? %r" % exists(to_file)
# prompts the user to complete the command
print "Ready, hit RETURN to continute, CTRL-C to abort.", raw_input()
# sets out_file as opening the 'to_file' in a writable state
out_file = open(to_file, 'w')
# writes the contents of 'indata' to 'out_file'. 
# indata is read from in_file which is the data opened from from_file
out_file.write(indata)
# neat
print "Alright, all done."
# closes from_file and to_file - closing is important because Python doesn't by default
out_file.close()
in_file.close()

# processing this command in one line
	# indata = open(from_file).read()