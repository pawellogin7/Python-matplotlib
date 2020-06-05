import numpy
from numpy.random import randint as rand
import matplotlib.pyplot as pyplot

def generate_maze(width=81, height=51, complexity=.75, density=.75):
    """Generate a maze using a maze generation algorithm."""
    # Only odd shapes
    shape = (((height // 2) * 2 + 1, (width // 2) * 2 + 1))
    # Adjust complexity and density relative to maze size
    complexity = int(complexity * (5 * (shape[0] + shape[1])))  # Number of components
    density = int(density * ((shape[0] // 2) * (shape[1] // 2)))  # Size of components
    # Build actual maze
    Z = numpy.zeros(shape, dtype=int)
    # Fill borders
    Z[-1, :] = Z[0, :] = 1
    #Z[-1*shape[0]:-1, 0:shape[1]//2] = 1
    Z[:, -1] = Z[:, 0] = 1

    #Make aisles
    for i in range(density):
        x, y = rand(0, shape[1] // 2) * 2, rand(0, shape[0] // 2) * 2  # Pick a random position
        Z[y, x] = 1
        for j in range(complexity):
            neighbours = []
            if x > 1:             neighbours.append((y, x - 2))
            if x < shape[1] - 2:  neighbours.append((y, x + 2))
            if y > 1:             neighbours.append((y - 2, x))
            if y < shape[0] - 2:  neighbours.append((y + 2, x))
            if len(neighbours):
                y_, x_ = neighbours[rand(0, len(neighbours) - 1)]
                if Z[y_, x_] == 0:
                    Z[y_, x_] = 1
                    Z[y_ + (y - y_) // 2, x_ + (x - x_) // 2] = 1
                    x, y = x_, y_
            else:
                break

    pointsX = []
    pointsY = []
    pointsX.append(1)
    pointsY.append(1)
    for i in range(0, shape[0]*shape[1], 1):
        neighbours = []
        y = pointsY[len(pointsY) - 1]
        x = pointsX[len(pointsX) - 1]
        if y == shape[0] - 2 and x == shape[1] - 2:
            break

        Z[y, x] = -1
        if Z[y, x - 1] != 1 and Z[y, x - 1] != -1 and Z[y, x - 1] != -2:
            neighbours.append((y, x - 1))
        if Z[y, x + 1] != 1 and Z[y, x + 1] != -1 and Z[y, x + 1] != -2:
            neighbours.append((y, x + 1))
        if Z[y - 1, x] != 1 and Z[y - 1, x] != -1 and Z[y - 1, x] != -2:
            neighbours.append((y - 1, x))
        if Z[y + 1, x] != 1 and Z[y + 1, x] != -1 and Z[y + 1, x] != -2:
            neighbours.append((y + 1, x))

        if len(neighbours) == 1:
            y_, x_ = neighbours[0]
            pointsX.append(x_)
            pointsY.append(y_)
        if len(neighbours) > 1:
            id = rand(0, len(neighbours) - 1)
            y_, x_ = neighbours[id]
            pointsX.append(x_)
            pointsY.append(y_)
        else:
            Z[y, x] = -2
            pointsX.pop()
            pointsY.pop()

    Z_kwadrat = numpy.copy(Z)
    Z_kwadrat[1, 1] = 2  #punkt startowy, lewy gorny rog
    Z_kwadrat[shape[0] - 2, shape[1] - 2] = 3  #punkt koncowy, prawy dolny rog
    for i in range(1, shape[0] - 1, 1):
        for j in range(1, shape[1] - 1, 1):
            if Z[i, j] == -2:
                Z_kwadrat[i, j] = 0
            elif Z[i, j] == -1:
                Z_kwadrat[i, j] = 4


    Z1 = numpy.zeros((shape[0]*3, shape[1]*3 + 1), dtype=int)
    for i in range(1, shape[0] - 1, 1):
        for j in range(1, shape[1] - 1, 1):
            tile = 0

            if Z[i, j] == 1:
                tile = 0
            elif Z[i, j] == 0 or Z[i, j] == -1 or Z[i, j] == -2:
                tile = 4

            if (i+j) % 2 == 0:
                Z1[3 * i, 3 * j + 2] = tile
                Z1[3 * i + 1, 3 * j + 1] = tile
                Z1[3 * i + 1, 3 * j + 2] = tile
                Z1[3 * i + 1, 3 * j + 3] = tile
                Z1[3 * i + 2, 3 * j] = tile
                Z1[3 * i + 2, 3 * j + 1] = tile
                Z1[3 * i + 2, 3 * j + 2] = tile
                Z1[3 * i + 2, 3 * j + 3] = tile
                Z1[3 * i + 2, 3 * j + 4] = tile

            else:
                Z1[3 * i + 2, 3 * j + 2] = tile
                Z1[3 * i + 1, 3 * j + 1] = tile
                Z1[3 * i + 1, 3 * j + 2] = tile
                Z1[3 * i + 1, 3 * j + 3] = tile
                Z1[3 * i, 3 * j] = tile
                Z1[3 * i, 3 * j + 1] = tile
                Z1[3 * i, 3 * j + 2] = tile
                Z1[3 * i, 3 * j + 3] = tile
                Z1[3 * i, 3 * j + 4] = tile


    return Z1

pyplot.figure(figsize=(10, 5))
pyplot.imshow(generate_maze(40, 40), cmap=pyplot.cm.tab10, interpolation='nearest')
pyplot.xticks([]), pyplot.yticks([])
pyplot.show()