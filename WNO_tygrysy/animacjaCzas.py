import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation
import numpy as np

class Tiger():
    def __init__(self, ident, x0, y0, v, alpha):
        self.id = ident
        self.p1 = [x0, y0]
        self.alpha = np.radians(alpha)
        self.vel = [v*np.cos(self.alpha), v*np.sin(self.alpha)]

    def point1(self):
        return self.p1
    def movePoints(self):
        self.p1[0] += self.vel[0]
        self.p1[1] += self.vel[1]
    def setPoint1X(self, valX):
        self.p1[0] = valX
    def setPoint1Y(self, valY):
        self.p1[1] = valY
    def getId(self):
        return self.id
    def getVel(self):
        return self.vel
    def setVel(self, valX, valY):
        self.vel[0] *= valX
        self.vel[1] *= valY
    def getAlpha(self):
        return self.alpha

def alfa(x0, y0, xa, ya):
    x = x0
    y = y0
    y = y - ya
    x = x - xa
    d = np.abs(x) + np.abs(y)
    if x >= 0 and y >= 0:
        return y / d
    elif x < 0 and y >= 0:
        return 2 - y / d
    elif x < 0 and y < 0:
        return 2 + np.abs(y) / d
    elif x >= 0 and y < 0:
        return 4 - np.abs(y) / d

#Funkcje animacji
def init():
    for line in lines:
        line.set_data([], [])
    return lines

def animate(i):
    xAnim = []
    yAnim = []
    #Przesuwanie punktow o predkosc
    for j in range(0, len(tigerList), 1):
        x1 = tigerList[j].point1()[0]
        y1 = tigerList[j].point1()[1]
        if x1 <= 0:
            tigerList[j].setPoint1X(0)
            tigerList[j].setVel(-1, 1)
            x1 = 0
        elif x1 >= maxX:
            tigerList[j].setPoint1X(maxX)
            tigerList[j].setVel(-1, 1)
            x1 = maxX

        if y1 <= 0:
            tigerList[j].setPoint1Y(0)
            tigerList[j].setVel(1, -1)
            y1 = 0
        elif y1 >= maxY:
            tigerList[j].setPoint1Y(maxY)
            tigerList[j].setVel(1, -1)
            y1 = maxY

        for k in range(0, len(otoczkaX) - 1, 1):
            otX1 = otoczkaX[k]
            otY1 = otoczkaY[k]
            otX2 = otoczkaX[k+1]
            otY2 = otoczkaY[k+1]
            if x1 >= otX1 and x1 <= otX2:
                if y1 >= otY1 and y1 <= otY2:
                    tigerList[j].setVel(-1, -1)
                elif y1 <= otY1 and y1 >= otY2:
                    tigerList[j].setVel(-1, -1)
            elif x1 <= otX1 and x1 >= otX2:
                if y1 >= otY1 and y1 <= otY2:
                    tigerList[j].setVel(-1, -1)
                elif y1 <= otY1 and y1 >= otY2:
                    tigerList[j].setVel(-1, -1)
        xAnim.append(x1)
        yAnim.append(y1)
        #tigerList[j].movePoints()

    nextPointId = 0
    minLeftDet = 100000000
    maxRightDet = 0
    print("start")
    for j in range(0, len(tigerList), 1):
        x1 = otoczkaX[len(otoczkaX) - 2]
        y1 = otoczkaY[len(otoczkaX) - 2]
        x2 = otoczkaX[len(otoczkaX) - 1]
        y2 = otoczkaY[len(otoczkaX) - 1]
        x3 = tigerList[j].point1()[0]
        y3 = tigerList[j].point1()[1]

        a = np.array([[x1, y1, 1], [x2, y2, 1], [x3, y3, 1]])
        det = np.linalg.det(a)

        # if j == 1 and len(otoczkaX) > 1:
        #     x3 = otoczkaX[0]
        #     y3 = otoczkaY[1]
        #     a = np.array([[x1, y1, 1], [x2, y2, 1], [x3, y3, 1]])
        #     det1 = np.linalg.det(a)
        #     if det1 < det:
        #         nextPointId = -1
        #         continue

        print(x3, y3, det)
        # det macierzy mowi, po ktorej stronie prostej 1-2 lezy punkt 3
        if det <= 0 and det <= maxRightDet:  # punkt po prawej
            maxRightDet = det
            nextPointId = j
        elif det >= 0 and det <= minLeftDet and maxRightDet == 0:
            minLeftDet = det
            nextPointId = j



    lastX = otoczkaX[len(otoczkaX) - 1]
    lastY = otoczkaY[len(otoczkaY) - 1]
    if nextPointId == -1:
        nextX = otoczkaX[0]
        nextY = otoczkaY[0]
    else:
        nextX = tigerList[nextPointId].point1()[0]
        nextY = tigerList[nextPointId].point1()[1]
    angleOtoczka = np.arctan2((nextY - lastY), (nextX - lastX))
    otoczkaX.append(lastX + velocityOtoczka*np.cos(angleOtoczka))
    otoczkaY.append(lastY + velocityOtoczka*np.sin(angleOtoczka))

    lines[1].set_data(otoczkaX, otoczkaY)
    lines[0].set_data(xAnim, yAnim)
    return lines


#Losowanie punktów
ilosc_tygrysow = 5
maxX = 1000.0
maxY = 1000.0
x = (maxX)*np.random.rand(ilosc_tygrysow)
y = (maxY)*np.random.rand(ilosc_tygrysow)
velocity = maxX/400 + (maxX/200)*np.random.rand(ilosc_tygrysow)
alpha = 360*np.random.rand(ilosc_tygrysow)
velocityOtoczka = maxX/20

#Tworzenie listy klasy Tiger
tigerList = []
for i in range(0, ilosc_tygrysow, 1):
    tigerList.append(Tiger(i, x[i], y[i], velocity[i], alpha[i]))

#Zapis wszystkich punktów tygrysow(na rogach obrazkow)
punktyTygrysy = []
for i in range(0, ilosc_tygrysow, 1):
    punktyTygrysy.append(tigerList[i].point1())

#Szukanie punktu o najmniejszym Y oraz X
min = maxY + 1
minid = 0
for i in range(0, len(punktyTygrysy), 1):
    if punktyTygrysy[i][1] < min:
        min = punktyTygrysy[i][1]
        minid = i
    elif punktyTygrysy[i][1] == min:
        if punktyTygrysy[i][0] <= punktyTygrysy[minid][0]:
            min = punktyTygrysy[i][1]
            minid = i

y0 = punktyTygrysy[minid][1]
x0 = punktyTygrysy[minid][0]
print("Ymin = {} dla X = {}".format(y0, x0))
print(minid)


fig, ax = plt.subplots()
ax.set_xlim(0, maxX)
ax.set_ylim(0, maxY)

lines = []
lines.append(ax.plot([], [], 'ro')[0])
lines.append(ax.plot([], [], 'b-', lw=2)[0])
otoczkaX = []
otoczkaY = []
otoczkaX.append(x0)
otoczkaY.append(y0)
otoczkaX.append(x0 - 1)
otoczkaY.append(y0)
anim = animation.FuncAnimation(fig, animate, init_func=init, interval=500, blit=True, repeat=False)

#Rysowanie otoczki wypuklej
# for i in range(0, len(wierzcholki_id) - 1, 1):
#     id1 = wierzcholki_id[i]
#     id2 = wierzcholki_id[i + 1]
#     xVal = [punktyTygrysy[id1][0], punktyTygrysy[id2][0]]
#     yVal = [punktyTygrysy[id1][1], punktyTygrysy[id2][1]]
#     ax.plot(xVal, yVal, 'b-')
# ax.plot([punktyTygrysy[wierzcholki_id[0]][0], punktyTygrysy[wierzcholki_id[len(wierzcholki_id) - 1]][0]],
#          [punktyTygrysy[wierzcholki_id[0]][1], punktyTygrysy[wierzcholki_id[len(wierzcholki_id) - 1]][1]], 'b-')

plt.show()
