n=1
a=1
while n!=64:
	n=(a**2+a+2)/2
	a=a+1
	if n>=64:
		break
print(a)

