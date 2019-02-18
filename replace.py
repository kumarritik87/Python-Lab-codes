n = input("\n")
m =""
o="#"
for i in range (0,len(n)):
	if ord(n[i]) %2 ==0:
		m = m+o
	else:
		m = m+n[i]
print(m)
