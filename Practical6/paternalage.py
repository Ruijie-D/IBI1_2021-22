#make two lists of paternal_age and chd
paternal_age=[30,35,40,45,50,55,60,65,70,75]
chd=[1.03,1.07,1.11,1.17,1.23,1.32,1.42,1.55,1.72,1.94]
#make a directory of the paternal_age and chd 
rlsp={}
ss=0
for ss in range (len(chd)):
 rlsp[paternal_age[ss]]=chd[ss]
print(rlsp)#print the directory
#make a variable (i) of the paternal_age, and it can be modified
i=40
print(rlsp[i])#evaluates to 1.11 if i=40
#draw a scatter plot describing the data:
import numpy as np
import matplotlib.pyplot as plt
N=10
x=paternal_age
y=chd
plt.scatter(x,y,marker='D',color='c')
plt.title("the effect of paternal age on offspring health")
plt.xlabel('paternal age')
plt.ylabel('relative risk of congenitial heart disease')
#the above codes are cited from URL: https://zhuanlan.zhihu.com/p/70835617 22/03/22
plt.show()#show the scatter plot of paternal_age and chd


