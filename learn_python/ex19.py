#!/usr/bin/env python2.7

# defines the function and the two arguments, cheese_count and boxes_of_crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
		# prints the variables and some text out to the user
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"
    
print "We can just give the function numbers directly:"
# calls the function with cheese_count = 20 and boxes_of_crackers = 30
cheese_and_crackers(20, 30)

print "Or, we can use variables from our script:"
# established two new variables with values
amount_of_cheese = 10
amount_of_crackers = 50
# calls the function and inputs the two variables above as the function arguments
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
# calls the function and combines two integers for each argument
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
# calls the function and sets the arguments by combining variables and integers
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

print "Finally, we can also ask the user for input!"
cheese_num = int(raw_input("How much cheese do you have? "))
cracker_num = int(raw_input("How many boxes of crackers do you have? "))
cheese_and_crackers(cheese_num, cracker_num)