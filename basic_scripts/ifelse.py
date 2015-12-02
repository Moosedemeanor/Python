#if else statements
#if something is the case, do that, if it's not, do something else.

x = 13
y = 6

if x < y:
    print(x,'is less than',y)
if x > y:
    print(x,'is greater than',y)

#else will only run if the immediately preceeding if statement is false

else:
    print(x,'is not less than',y)
