		Truth Terms
 and
 or
 not
 != (not equal)
 == (equal)
 >= (greater-than-equal)
 <= (less-than-equal)
 True
 False

		Truth Tables
		
NOT							TRUE?			
not False				True			# If not y, then x
not True				False			# If not x, then y

OR							TRUE?			
True or False		True			# If x or y, then x
True or True		True			# If x or x, then x
False or True		True			# If y or x, then x
False or False	False			# If y or y, then y

AND							TRUE?
True and False	False			# If x and y, then y
True and True		True			# If x and x, then x
False and True	False			# If y and x, then y
False and False	False			# If y and y, then y

NOT OR								TRUE?
not (True or False)		False			# If not x or y, then y
not (True or True)		False			# If not x or x, then y
not (False or True)		False			# If not y or x, then y
not (False or False		True			# If not y or y, then x

NOT AND								TRUE?
not (True and False)	True			# If not x and y, then x
not (True and True)		False			# If not x and x, then y
not (False and True)	True			# If not y and x, then x
not (False and False)	True			# If not y and y, then x

!=				TRUE?
1 != 0		True				# 1 does not equal 0 - True
1 != 1		False				# 1 does not equal 1 - False
0 != 1		True				# 0 does not equal 1 - True
0 != 0		False				# 0 does not equal 0 - False

==				TRUE?
1 == 0		False				# 1 does equal 0 - False
1 == 1		True				# 1 does equal 1 - True
0 == 1		False				# 0 does equal 1 - False
0 == 0		True				# 0 does equal 0 - True