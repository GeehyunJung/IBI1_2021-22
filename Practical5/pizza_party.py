# n is the number of slices of the pizza
# a is the nubmer of straight cuts
n=2
a=1
print(str(n)+' slices of pizza can be cut with '+str(a)+' straight cut.')
# if n does not equals to 64 than increase the nuber of straight cuts
while n!=64:
	a=a+1
	n=(a**2+a+2)/2
	print(str(n)+' slices of pizza can be cut with '+str(a)+' straight cuts.')
# if n becomes larger than 64, stop cutting
	if n>=64:
		break
