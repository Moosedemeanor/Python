#This section defines variables in the script
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)
# prints the above variables to the terminal
print x
print y
# prints and pipes in the previous variables
print "I said %r." % x
print "I also said: '%s'." % y
# makes the variable 'hilarious' false
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
# prints the defined variables
print joke_evaluation % hilarious
# defines variables
w = "This is the left side of..."
e = "a string with a right side."
# prints teh variables on the same line
print w + e
