import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import scipy.io

mat = scipy.io.loadmat('file.mat')
data = mat['data_map']

x = data[:, 0]
y = data[:, 1]
z = data[:, 2]

grid_length = 30
grid_x = np.linspace(np.amin(x), np.amax(x), grid_length)
grid_y = np.linspace(np.amin(y), np.amax(y), grid_length)
x1 = []
y1 = []
z1 = []
for curr_x in grid_x:
    for curr_y in grid_y:
        buf_x = x - curr_x
        buf_y = y - curr_y
        dist_list = np.sqrt(buf_x**2 + buf_y**2)
        min_dist = np.amin(dist_list) * 1.1
        min_dist = np.amax([min_dist, 0.1])
        neighbours_list = np.where(dist_list <= min_dist, dist_list, 0)
        indexes = np.nonzero(neighbours_list)
        z_neighbours = z[indexes]
        z_curr = np.mean(z_neighbours)
        z1.append(z_curr)
        x1.append(curr_x)
        y1.append(curr_y)

x1 = np.asarray(x1).reshape(grid_length, grid_length)
y1 = np.asarray(y1).reshape(grid_length, grid_length)
z1 = np.asarray(z1).reshape(grid_length, grid_length)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x1, y1, z1, cmap='cividis')

plt.show()
