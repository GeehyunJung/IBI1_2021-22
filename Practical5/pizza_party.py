# n is the number of slices of the pizza
# a is the nubmer of straight cuts
n=1
a=1
# if n does not equals to 64 than increase the nuber of straight cuts
while n!=64:
	n=(a**2+a+2)/2
	print(str(n)+' slices of pizza can be cut with '+str(a)+' straight cuts.')
	a=a+1
# if n becomes larger than 64, stop cutting
	if n>=64:
		break
