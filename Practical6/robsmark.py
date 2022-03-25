#input Rob's marks
M=[45,36,86,57,53,92,65,45]
print(sorted(M))#print the sorted list
#make a variable which is the average of the marks in list M
import numpy as np
avr=np.mean(M)#np.mean() is used to gain the average cited from URL:https://blog.csdn.net/qq_45473634/article/details/119820171 22/03/22
#compare the average with 60
print(avr>=6)
#if shows True, than the mean is higher than 60 and Rob passed his ICA;
#if shows False, it means he didn't pass his ICA.

#make a boxplot
import matplotlib.pyplot as plt
plt.boxplot(
M,
sym='D',
whis=1.5,
notch=False,
patch_artist=True
)

plt.ylabel('score')#mark the y label
plt.title("distribution of Rob's mark")#mark the title
plt.grid(linestyle="--",alpha=0.7)#add the grid background
#the above codes were cited from URL:https://zhuanlan.zhihu.com/p/70835617 22/03/22
plt.show()
#the boxplot still needs to improve, like changing its colors and styles.
