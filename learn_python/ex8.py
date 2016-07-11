#!/usr/bin/env python2.7

# Establishes how formatting strings should laid out
# Items piped into the variable 'formatter' will be formatted '%r %r %r %r'
formatter = "%s %s %s %s"

# These lines pipe data into the variable 'formatter'
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)

# This line pipes the string from the variable 'formatter' back into the variable 'formatter'
print formatter % (formatter, formatter, formatter, formatter)

# This pipes the four strings, broken up by commas, into the variable 'formatter'
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
	)
	
# I replaced %r with %s to remove the single quotes around string text.