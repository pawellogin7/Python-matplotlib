import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate
import scipy.io

x = np.linspace(0, 18, num=21, endpoint=True)
y = np.cos(x)


f = interpolate.interp1d(x, y)
f2 = interpolate.interp1d(x, y, kind='cubic')
xnew = np.linspace(np.amin(x), np.amax(x), num=41, endpoint=True)


fig = plt.figure()
ax = fig.add_subplot()
ax.plot(x, y, 'o', xnew, f(xnew), '-', xnew, f2(xnew), '--')
ax.legend(['data', 'linear', 'cubic'], loc='best')

plt.show()
