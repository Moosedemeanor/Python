#!/usr/bin/env python2.7
break_line = "_" * 10
# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI',
    'Rhode Island': 'RI',
    'Massachusetts': 'MA'
}
# create a basic set of states and some cities in them
cities = {
		'RI': 'Providence',
		'CA': 'San Francisco',
		'MI': 'Detroit',
		'FL': 'Jacksonville'
}
# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'
cities['MA'] = 'Boston'
# print out some cities
print break_line
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

# print some states
print break_line
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is : ", states['Florida']

# do it by using the state then cities dict
print break_line
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states["Florida"]]

# print every state abbreviation
print break_line
for state, abbrev in states.items():
		print "%s is abbreviated %s" % (state, abbrev)

# print every city in state
print break_line
for abbrev, city in cities.items():
		print "%s has the city %s" % (abbrev, city)
		
# now do both at the same time
print break_line
for state, abbrev in states.items():
		print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])
print break_line

# safely get a abbreviation by state that might not be there
state = states.get('Texas')

if not state:
		print "Sorry, no Texas."
		
# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city

# if you need an ordered dictionary - use collections.OrderedDict
		# 	dict subclass that remembers the order entries were added