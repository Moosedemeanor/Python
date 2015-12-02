#If Elif statements
#The elif will only run if the previous ifs or  elifs do not run.

x = 3
y = 7
z = 10

if x > y:
    print(x,'is greater than',y)
elif x < z:
    print(x,'is less than',z)
elif y < z:
    print(y,'is lessi than',z)
else:
    print('Nothing was the case')

#elif will break after the first true statement.
#If you're trying to check for multiple statements, use multiple if
#statements as elif will only provide the first true statement.

#or statements are similar to if statements.
#and statements are similar to if statements.

if x < y and x < z:
    print(x,'is less than',y,'and',z)
