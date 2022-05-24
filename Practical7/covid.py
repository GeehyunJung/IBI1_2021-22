#import data
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir('/Users/selina/Desktop/a/1/IBI/IBI1_2021-22/Practical7/')
covid_data=pd.read_csv('full_data.csv')

#covid Afghanistan
firstandthird=[True,False,True,False,False,False]
print(covid_data.loc[10:20,firstandthird])
location_only=[False,True,False,False,True,False]
print(covid_data.loc[(covid_data['location']=='Afghanistan'),location_only])

#covid china
column1=[True,False,True,True,False,False]#choose the coloums contain new deaths and new cases
covid_china=covid_data.loc[(covid_data['location']=='China'),column1]# choose the lines whose location is china
print(covid_china)
new_deaths=list(covid_china['new_deaths'])
new_cases=list(covid_china['new_cases'])
print(np.mean(new_cases))
print(np.mean(new_deaths))



#boxplot1 new causes and new deaths in China
cases_and_deaths = [(covid_china['new_cases']),(covid_china['new_deaths'])]
plt.title('boxplots of new cases and new deaths in china',fontsize=15)
plt.boxplot(cases_and_deaths, positions=[1,2], widths=0.5, patch_artist=True,
                showmeans=False, showfliers=False,labels=('new cases','new deaths'),
                medianprops={"color": "white", "linewidth": 0.5},
                boxprops={"facecolor": "lightpink", "edgecolor": "white"},
                whiskerprops={"color": "hotpink", "linewidth": 0.5},
                capprops={"color": "hotpink", "linewidth": 0.5})
plt.show()

#plot2 a plot with new cases and new deaths in China
dates=list(covid_china['date'])
new_cases=list(covid_china['new_cases'])
new_deaths=list(covid_china['new_deaths'])
plt.title('new cases and new deaths in china',fontsize=15)
x=(dates)
y1=(new_cases)
y2=(new_deaths)
plt.plot(x,y2)
plt.plot(x,y1,color='plum',linewidth=1,linestyle='--')
plt.xticks(covid_china['date'].iloc[0:len(covid_china['date']):4],rotation=-90,fontsize=5)
plt.show()

#question
c2=[True,True,False,False,True,False]
covid314=covid_data.loc[(covid_data['date']=='2020-03-14'),c2] # choose the lines whose date is 2020,3,14
cases314=list(covid314['total_cases']) # choose the total cases column
plt.title('cases in 3.14 with outliers',fontsize=20)
#this is a boxplot with outliers so the box is not easy to recognise
plt.boxplot(cases314, notch=True,  vert=False, whis=None, labels=['total cases'],
                          widths=None, patch_artist=True, 
                          conf_intervals=None, meanline=True, showmeans=True, showcaps=None, showbox=None,
                          showfliers=True,  manage_ticks=True, autorange=False)
plt.show()
#this is a boxplot without outliers. In this way the box can be recognised easily
plt.boxplot(cases314, notch=True,  vert=False, whis=None, positions=None, labels=['total cases'],
                          widths=None, patch_artist=True, usermedians=None, 
                          conf_intervals=None, meanline=None, showmeans=None, showcaps=None, showbox=None,
                          showfliers=False,  manage_ticks=True, autorange=False,
            medianprops={"color": "white", "linewidth": 0.5},
            boxprops={"facecolor": "lightblue", "edgecolor": "white"},
            whiskerprops={"color": "lightskyblue", "linewidth": 0.5},
            capprops={"color": "lightskyblue", "linewidth": 0.5})
plt.title('cases in 3.14 without outliers',fontsize=20)
plt.show()