#a is the totle number of the dots and 
#b is the number of dots in the last line of each triangle
a=1
b=1
print(a)
# let the number of the dots in the last line plus one each time
# add the number of the dots in the last line to the total number of dots in the triangle.
# Then a is the total number of dots.
# Repeat the process for 9 times.
for i in range(1,10):
	b=b+1
	a+=b
	print(a)

