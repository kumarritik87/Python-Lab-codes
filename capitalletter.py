n = str(input('Enter the string'))
m = ""
o=""
for i in range (0,len(n)):
	if (ord(n[i])>=65 and ord (n[i])<=90):
		m = m+n[i]
	else:
		o = o+n[i]

print("capital",m)
print("other",o)
