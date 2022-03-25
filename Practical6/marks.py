marks=[45,36,86,57,53,92,65,45]
# mark are printed from low to high
print(sorted(marks))
#codes from matplot.org about how to create a boxplot
import numpy as np
import matplotlib.pyplot as plt
plt.boxplot(marks,
vert=True,#vertical or not
showmeans=True,#show the mean or not
meanline=True,#show the mean in line or not
notch = False)
plt.show()
#calculate the mean of the marks
mean=sum(marks)/len(marks)
if mean>=60:
	print('Rob passed IBI!!')
else:
	print('Rob failed IBI. (saaaaaad TOT)')

