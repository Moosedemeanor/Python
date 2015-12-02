#if statements - opertorsi
#going to ask IF somehting is the case, and then do something
#only going to do something IF something is true

x = 2
y = 7
z = 10

if x > y:
    print(x,'is greater than',y)
if x < y:
    print(x,'is less than',y)

#' = ' is an assignment operator ex: x= 10
#' == ' represents 'equals' ex: x == y

if x == y:
    print(x,'is equal to',y)

if x < 2:
    print(x,'is less than 2')

if x <= y:
    print(x,'is less than or equal to',y)

if x >= y:
    print(x,'is greater than or equal to',y)

if z > y > x:
    print(z,'is greater than',y,'which is greater than',x)
