# What does this piece of code do?
# Answer:choose a random nuber from 1 to 100 for 10 times and print the tenth result

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

# choose a random number from 1 to 100
# repeat the progress for 10 times
progress=0
while progress<10:
	progress+=1
	n = randint(1,100)

# print the 10th results
print(n)
