#!/usr/bin/env python2.7
# \ backslash character encodes difficult-to-typer characters into a string
# There are various "escape sequences" available
print "I am 5'9\" tall." # escape double-quote inside string
print 'I am 5\'9" tall.' # escape single-quote inside string
print ''
# Another "escape sequence" is the triple-quotes - works like a string
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

# Why would you use ''' instead of """ ?
# If the string itself contains a triple quote.
s1 = '''This string contains """ so use triple-single-quotes.'''
s2 = """This string contains ''' so use triple-double-quotes."""

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

#Infinite loop - Ctrl-C to break
#while True:
#	for i in ["/","-","|","\\","|"]:
#			print "%s\r" % i,

# Using format strings to create a more complex format.
complex = "\vHello \vVerticle \vTabs %s"
print complex % ('\nTabs \tTo \tThe \tRight')

# Study drill code with double/single quotes and %s or %r
print 'Didn\'t you see %r, it\'s %r ' % ("Charlie\'s face", "ugly")
print 'Didn\'t you see %s, it\'s %s ' % ("Charlie\'s face", "ugly")

# Escape - What It Does
# \\				Backslash (\)
# \'				Single-quote (')
# \"				Double-quote (")
# \a				ASCII bell (BEL)
# \b				ASCII backspace (BS)
# \f				ASCII formfeed (FF)
# \n				ASCII linefeed (LF)
# \N{name}  Character named name in the Unicode database (Unicode only)
# \r				Carriage Return (CR)
# \t				Horizontal Tab (TAB)
# \uxxxx		Character with 16-bit hex value xxxx (Unicode only)
# \Uxxxxxxxx	Character with 32-bit hex value xxxxxxxx (Unicode only)
# \v				ASCII vertical tab (VT)
# \ooo			Character with octal value ooo
# \xhh			Character with hex value hh