n = str(input('Enter First string:'))
m = str(input('Enter Second String:'))
if(n in m):
	print("string",n, "is  a substring of", n)
elif(m in n):
	print("string",m," is a substring of",n)
else:
	print('string is not a substring')
