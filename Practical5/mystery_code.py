# What does this piece of code do?
# Answer: It selects ten random numbers between 1 and 100 and then print the last one. 

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

progress=0
while progress<10:#so that the loop will be executed 10 times
	progress+=1#so that progress will keep increasing as while loop going
	n = randint(1,100)#gain a random number

print(n)#print out the number from the 10th loop
