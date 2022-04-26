n=0 #n is the cutting number
p=0 #p is the number of pizza slices
s1a="if I cut the cake "
s1b=" times, "
s1c=" pieces of pizza can be gotten" 

while p<64: #p<64 means the slices are not enough and need another cut
 n=n+1
 p=((n**2)+n+2)/2 
 print(s1a+str(n)+s1b+str(p)+s1c)#it starts to print from the first cut 
 #print(p)
print("Woooo! If I cut "+str(n)+" times, I can get "+str(p)+" slices and it's enough!")
