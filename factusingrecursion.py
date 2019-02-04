def fact(n):
	if n==1:
		return 1
	return n*fact(n-1)
n = int(input('Enter the number to find factorial :-'))
if n==0:
	print('the factorial of 0 is 1')
elif n<0:
	print('Enter the valid number')
else:
	print('The factorial of',n,'is :-',fact(n))


