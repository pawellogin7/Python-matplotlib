import numpy as np
from numpy.random import randint as rand
import matplotlib.pyplot as plt

mat = np.zeros(50)
mat1 = np.ones(10)


plt.hexbin(mat, mat1)
plt.show()
