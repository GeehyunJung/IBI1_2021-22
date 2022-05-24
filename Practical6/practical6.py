paternal_age=[30,35,40,45,50,55,60,65,70,75]
chd=[1.03,1.07,1.11,1.17,1.23,1.32,1.42,1.55,1.72,1.94]
import matplotlib.pyplot as plt
import numpy as np
# x is the parents' age and y is the children's age
x=np.array(paternal_age)
y=np.array(chd)
# l1 is the dictionary inculding the paternal age and the rate
l1={30:1.03,35:1.07,40:1.11,45:1.17,50:1.23,55:1.32,60:1.42,65:1.55,70:1.72,75:1.94}

#display frequency table
print(l1)

# choose a number from paternal age randomly to simulate the user's input
example=random.choice(paternal_age)
print({example,l1[example]})
print('The risk of congenital heart heart disease in the offspring of a father of a given age from the input is '+str(l1[example]))
# got the code from the matplotlib website
# fit a linear curve an estimate its y-values and their error.
a, b = np.polyfit(x, y, deg=1)
y_est = a * x + b
y_err = x.std() * np.sqrt(1/len(x) +
                          (x - x.mean())**2 / np.sum((x - x.mean())**2))
fig, ax = plt.subplots()
ax.plot(x, y_est, '-')
ax.fill_between(x, y_est - y_err, y_est + y_err, alpha=0.2)
ax.plot(x, y, 'o', color='tab:brown')
plt.show()

# scatter plot
plt.plot(x,y,'ro')
plt.xlabel('paternal_age')
plt.ylabel('chd')
plt.title('the realtionship between the age of parent and chd')
plt.show()

# when user has an input, print the rate
import random
print('please choose the age from the given table.\nPlease input the age here:')
input_age=int(input())
print({input_age,l1[input_age]})
print('The risk of congenital heart heart disease in the offspring of a father of a given age from the input is '+str(l1[input_age]))