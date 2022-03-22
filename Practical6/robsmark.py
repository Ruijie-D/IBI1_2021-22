#input Rob's marksM=[45,36,86,57,53,92,65,45] 
print(sorted(M))#print the sorted list
#make a variable which is the average of the marks in list M
import numpy as np 
avr=np.mean(M)
#compare the average with 60
print(avr>=6)
#if the average is higher than 60, it will show 'True' otherwise show 'False'

#make a boxplot
import matplotlib.pyplot as plt 
plt.boxplot(
M, 
sym='D', 
whis=1.5, 
notch=False, 
patch_artist=True,
medianprops={'color':'orange'},
whiskerprops={'color':'black'}
) 
plt.patch.set_facecolor('pink')
plt.ylabel('score') 
plt.title("distribution of Rob's mark") 
plt.grid(linestyle="--",alpha=0.7) 
plt.show()

