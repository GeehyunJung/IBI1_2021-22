marks=[45,36,86,57,53,92,65,45]
print(sorted(marks))
import numpy as np
import matplotlib.pyplot as plt
plt.boxplot(marks,vert=True,notch = False)
plt.show()

