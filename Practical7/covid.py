import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir('/Users/selina/Desktop/a/1/IBI/IBI1_2021-22/Practical7/')
covid_data=pd.read_csv('full_data.csv')
firstandthird=[True,False,True,False,False,False]
print(covid_data.loc[10:20,firstandthird])
location_only=[False,True,False,False,True,False]
print(covid_data.loc[(covid_data['location']=='Afghanistan'),location_only])

#covid china
column1=[True,False,True,True,False,False]
covid_china=covid_data.loc[(covid_data['location']=='China'),column1]
print(covid_china)
new_deaths=list(covid_china['new_deaths'])
print(np.mean(new_deaths))
cases_and_deaths = [(covid_china['new_cases']),(covid_china['new_deaths'])]

# boxplot
fig, ax = plt.subplots()
VP = ax.boxplot(D, positions=[1,2], widths=0.5, patch_artist=True,
                showmeans=False, showfliers=False,
                medianprops={"color": "white", "linewidth": 0.5},
                boxprops={"facecolor": "C0", "edgecolor": "white",
                          },
                whiskerprops={"color": "C0", "linewidth": 0.5},
                capprops={"color": "C0", "linewidth": 0.5})


plt.show()

#plot2
x=(dates)
y1=(new_cases)
y2=(new_deaths)
plt.plot(x,y2)
plt.plot(x,y1,color='red',linewidth=1,linestyle='--')
plt.show()

#question
c2=[True,True,True,False,False,False]
covid314=covid_data.loc[(covid_data['date']=='2020-03-14'),c2]
cases314=list(covid314['new_cases'])
plt.title('cases in 3.14 with outliers',fontsize=20)
plt.boxplot(cases314, notch=True,  vert=False, whis=None, 
                          widths=None, patch_artist=True, 
                          conf_intervals=None, meanline=True, showmeans=True, showcaps=None, showbox=None,
                          showfliers=True,  manage_ticks=True, autorange=False)
plt.show()
plt.boxplot(cases314, notch=True,  vert=False, whis=None, positions=None, 
                          widths=None, patch_artist=True, usermedians=None, 
                          conf_intervals=None, meanline=None, showmeans=None, showcaps=None, showbox=None,
                          showfliers=False,  manage_ticks=True, autorange=False)
plt.title('cases in 3.14 without outliers',fontsize=20)
plt.show()
