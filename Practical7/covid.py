import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#import the full_data.csv
covid_data =pd.read_csv("full_data.csv")

#show the first and third columns from rows 10-20
print(covid_data.iloc[9:20,0:3:2])

#show "total_cases" for all rows corresponding to Afghanistan
a=covid_data.loc[covid_data["location"]=="Afghanistan","total_cases"]#referred to URL:https://blog.csdn.net/weixin_35364187/article/details/113968240
print(a)

#import the china_new_data.csv
china_data=pd.read_csv("china_new_data.csv")

#compute the mean number of new cases and new deaths in China
mean_new_cases=np.mean(china_data.loc[0:,"new_cases"])
print("mean_new_cases:"+str(mean_new_cases))
mean_new_deaths=np.mean(china_data.loc[0:,"new_deaths"])
print("mean_new_deaths:"+str(mean_new_deaths))

#create a boxplot of new cases and new deaths in China
labels=['new cases','new deaths']
plt.boxplot(china_data.loc[0:,["new_cases","new_deaths"]],sym="+",whis=0.5,labels=labels)
plt.title("new cases and new deaths in China in 2020")
plt.ylabel('number')
plt.xlabel('class')
plt.show()

#plot both new cases and new deaths in China over time
#first create two lists for convenience
china_dates=china_data.loc[0:,"date"]
china_new_cases=china_data.loc[0:,"new_cases"]
china_new_deaths=china_data.loc[0:,"new_deaths"]
plt.plot(china_dates,china_new_cases,'b+',china_dates,china_new_deaths,'r+')
plt.xticks(china_dates.iloc[0:len(china_dates):4],rotation=-90)#cited from the practical7 guidance
plt.ylabel('number')
plt.xlabel('date')
plt.title("new cases and new deaths in China over time")
plt.plot(2,3,label="china_new_cases")
plt.plot(2,3* 2,label="china_new_deaths")
plt.legend(loc='best')
plt.show()

#answer the question
spain_data =pd.read_csv("spain_data.csv")
spain_dates=spain_data.loc[0:,"date"]
spain_new_cases=spain_data.loc[0:,"new_cases"]
spain_total_cases=spain_data.loc[0:,"total_cases"]
plt.plot(spain_dates,spain_new_cases,'b+')
plt.plot(spain_dates,spain_total_cases,'r+')
plt.title("new cases and total cases in Spain in 2020 over time")
plt.plot(2,3,label="new cases")
plt.plot(2,3* 2,label="total cases")
plt.xlabel('date')
plt.ylabel('number')
plt.legend(loc='best')#legends are referred from URL:https://zhuanlan.zhihu.com/p/70835617
plt.xticks(china_dates.iloc[0:len(spain_dates):4],rotation=-90)
plt.show()

