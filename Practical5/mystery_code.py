# What does this piece of code do?
# Answer:show one random number in the range from 1 to 100

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

progress=0
while progress<10:
	progress+=1#make n enter into the loop in every new operation
	n = randint(1,100)#gain a random number

print(n)
