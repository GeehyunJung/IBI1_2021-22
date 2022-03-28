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
