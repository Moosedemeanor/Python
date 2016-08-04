#!/usr/bin/env python2.7

print "This program will increment any number from 0 in any increment defined"
end_num = int(raw_input("Which number would you like to increment to? "))
increment_num = int(raw_input("Which number would you like to increment with? ")) 

def increment_function(end_num, increment_num):
		i = 0
		numbers = []
		while i < end_num:
				print "At the top i is %d" % i
				numbers.append(i)
				
				i += increment_num
				print "Numbers now: ", numbers
				print "At the bottom i is %d" % i
		
		print "The numbers: "
		
		for num in numbers:
				print num
				
increment_function(end_num, increment_num)