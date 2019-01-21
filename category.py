n = int(input('enter the amount'))
if n>25000:
	print('The category is GOld')
	dis = (n*20)/100
	total = n-dis
	print('Total amount = ',total)
elif 10000<n>=25000:
	print('The category is Silver')
	dis = (n*10)/100
	total = n-dis
	print('Total amount = ',total)
else:
	print('The category is Bronze')
	dis = (n*5)/100
	total = n-dis
	print('Total amount = ',total)
	
