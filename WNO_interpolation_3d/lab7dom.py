import scipy.io
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from matplotlib import cm

mat = scipy.io.loadmat('file.mat')
mat = mat['data_map']

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

X = mat[:, 0]
Y = mat[:, 1]
Z = mat[:, 2]
xy = mat[:, :2]
Xmin = np.min(X)
Xmax = np.amax(X)
Ymin = np.min(Y)
Ymax = np.amax(Y)
grid_x = np.linspace(Xmin, Xmax, 30)
grid_y = np.linspace(Ymin, Ymax, 30)
#najblizszy sąsiad
Zout = []
Yout = []
Xout = []
for i in grid_x:
    for j in grid_y:
        buf = xy - [i, j]
        dis = np.sqrt(buf[:, 0]**2 + buf[:, 1]**2)
        index = np.argmin(dis)
        Zout.append(Z[index])
        Xout.append(i)
        Yout.append(j)


ax = plt.axes(projection='3d')
ax.plot_trisurf(Xout, Yout, Zout, cmap=cm.coolwarm)
plt.title(" srednia wartosc z 4 najblizszych sasiadow (prostokat) ")


# zz = []
# Nfrm = 10
# fps = 10
# def generate(x,y,phi):
#     R = 1 - np.sqrt(x**2 + y**2)/2
#     return (np.cos(2*np.pi*x + phi) * R/(np.amax(Zout)/2)) + 15
#
# xx, yy = np.meshgrid(grid_x, grid_y)
# wframe = None
# z = generate(xx,yy,0)
# def update(idx):
#     phi = phis[idx]
#     global wframe
#     if wframe:
#         ax.collections.remove(wframe)
#     z = generate(xx,yy,phi)
#     wframe = ax.plot_wireframe(xx,yy,z,rstride=1,cstride=1,color='k',linewidth=0.5)
# phis = np.linspace(0, 180. / np.pi, 100)
# ani = animation.FuncAnimation(fig, update, Nfrm, interval=1000/fps)
plt.show()


