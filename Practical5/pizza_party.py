n=0 #n is the cutting number
p=0 #p is the number of pizza slices
s1a="if I cut the cake "
s1b=" times, "
s1c=" pieces of pizza can be gotten" 
for n in range(0,30): #30 is a random number which promise p>=64 can be reached
 if n>=1:
  print(s1a+str(n)+s1b+str(p)+s1c)#it starts to print from the first cut 
 n=n+1
 p=((n**2)+n+2)/2
 #print(p)
 if p>=64:
  break#when the pizza slices are enough, it can get out of the loop
print("Whoooo! If I cut "+str(n)+" times, I can get "+str(p)+" slices and it's enough!")
