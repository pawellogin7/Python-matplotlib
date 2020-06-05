import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Pentagram():
    def __init__(self, xs, ys, h, katPochylenia, vel):
        self.kat = katPochylenia
        self.wys = h
        self.pCenter = [xs, ys]
        self.vel = [vel*np.cos(np.radians(katPochylenia)), vel*np.sin(np.radians(katPochylenia))]
        self.setPoints()

    def setPoints(self):
        self.p1 = [self.pCenter[0] + self.wys * np.cos(np.radians(90 + self.kat)),
                   self.pCenter[1] + self.wys * np.sin(np.radians(90 + self.kat))]
        self.p2 = [self.pCenter[0] + self.wys * np.cos(np.radians(90 + 72 + self.kat)),
                   self.pCenter[1] + self.wys * np.sin(np.radians(90 + 72 + self.kat))]
        self.p3 = [self.pCenter[0] + self.wys * np.cos(np.radians(90 + 72 * 2 + self.kat)),
                   self.pCenter[1] + self.wys * np.sin(np.radians(90 + 72 * 2 + self.kat))]
        self.p4 = [self.pCenter[0] + self.wys * np.cos(np.radians(90 + 72 * 3 + self.kat)),
                   self.pCenter[1] + self.wys * np.sin(np.radians(90 + 72 * 3 + self.kat))]
        self.p5 = [self.pCenter[0] + self.wys * np.cos(np.radians(90 + 72 * 4 + self.kat)),
                   self.pCenter[1] + self.wys * np.sin(np.radians(90 + 72 * 4 + self.kat))]
    def getP1(self):
        return self.p1
    def getP2(self):
        return self.p2
    def getP3(self):
        return self.p3
    def getP4(self):
        return self.p4
    def getP5(self):
        return self.p5
    def getCenter(self):
        return self.pCenter
    def movePoints(self):
        self.pCenter[0] += self.vel[0]
        self.pCenter[1] += self.vel[1]
        self.setPoints()
    def changeVel(self, valueX, valueY):
        self.vel[0] *= valueX
        self.vel[1] *= valueY
    def checkCollision(self, minX, maxX, minY, maxY):
        if self.p1[0] <= minX or self.p1[0] >= maxX:
            return 1
        elif self.p2[0] <= minX or self.p2[0] >= maxX:
            return 1
        elif self.p3[0] <= minX or self.p3[0] >= maxX:
            return 1
        elif self.p4[0] <= minX or self.p4[0] >= maxX:
            return 1
        elif self.p5[0] <= minX or self.p5[0] >= maxX:
            return 1
        if self.p1[1] <= minY or self.p1[1] >= maxY:
            return -1
        elif self.p2[1] <= minY or self.p2[1] >= maxY:
            return -1
        elif self.p3[1] <= minY or self.p3[1] >= maxY:
            return -1
        elif self.p4[1] <= minY or self.p4[1] >= maxY:
            return -1
        elif self.p5[1] <= minY or self.p5[1] >= maxY:
            return -1
        return 0

def get_alpha(x, y, x0, y0):
    xi = x - x0
    yi = y - y0
    di = np.sqrt(pow(xi, 2) + pow(yi, 2))
    if xi >= 0 and yi >= 0:
        return 2 - yi/di
    if xi < 0 and yi >= 0:
        return yi/di
    if xi < 0 and yi < 0:
        return 2 + np.abs(yi)/di
    if xi >= 0 and yi < 0:
        return 4 - np.abs(yi)/di



#Funkcje animacji
def init():
    for line in lines:
        line.set_data([], [])
    return lines

def animate(j):
    x = []
    y = []


    for i in range(0, ilosc_tygrysow, 1):
        if pentagram_list[i].checkCollision(0, maxX, 0, maxY) == 1:
            pentagram_list[i].changeVel(-1, 1)
        elif pentagram_list[i].checkCollision(0, maxX, 0, maxY) == -1:
            pentagram_list[i].changeVel(1, -1)

        pentagram_list[i].movePoints()

        x.append(pentagram_list[i].getP1()[0])
        y.append(pentagram_list[i].getP1()[1])
        x.append(pentagram_list[i].getP2()[0])
        y.append(pentagram_list[i].getP2()[1])
        x.append(pentagram_list[i].getP3()[0])
        y.append(pentagram_list[i].getP3()[1])
        x.append(pentagram_list[i].getP4()[0])
        y.append(pentagram_list[i].getP4()[1])
        x.append(pentagram_list[i].getP5()[0])
        y.append(pentagram_list[i].getP5()[1])

    min = maxY + 1
    minId = 0
    for i in range(0, len(x), 1):
        if y[i] < min:
            min = y[i]
            minId = i
        elif y[i] == min:
            if x[i] <= x[minId]:
                min = y[i]
                minId = i

    x0 = x[minId]
    y0 = y[minId]

    alpha_list = []
    for i in range(0, len(x), 1):
        if i != minId:
            alpha_list.append(get_alpha(x[i], y[i], x0, y0))
        else:
            alpha_list.append(-1)

    alpha_sorted_list = []
    alpha_sorted_list.append(minId)
    for i in range(0, len(alpha_list), 1):
        maxAlpha = -1
        maxAID = 0
        for j in range(0, len(alpha_list), 1):
            if alpha_list[j] >= maxAlpha and j != minId:
                maxAID = j
                maxAlpha = alpha_list[j]
        alpha_sorted_list.append(maxAID)
        alpha_list[maxAID] = -1

    wierzcholki_id = []
    wierzcholki_id.append(alpha_sorted_list[0])
    wierzcholki_id.append(alpha_sorted_list[1])
    wierzcholki_id.append(alpha_sorted_list[2])
    iter = 3
    while iter < len(x):
        x1 = x[wierzcholki_id[len(wierzcholki_id) - 2]]
        y1 = y[wierzcholki_id[len(wierzcholki_id) - 2]]
        x2 = x[wierzcholki_id[len(wierzcholki_id) - 1]]
        y2 = y[wierzcholki_id[len(wierzcholki_id) - 1]]
        x3 = x[alpha_sorted_list[iter]]
        y3 = y[alpha_sorted_list[iter]]
        a = np.array([[x1, y1, 1], [x2, y2, 1], [x3, y3, 1]])
        det = np.linalg.det(a)
        if det >= 0:
            wierzcholki_id.append(alpha_sorted_list[iter])
            iter += 1
        else:
            wierzcholki_id.pop()
    wierzcholki_id.append(alpha_sorted_list[0])

    otoczkaX = []
    otoczkaY = []
    for i in range(0, len(wierzcholki_id), 1):
        otoczkaX.append(x[wierzcholki_id[i]])
        otoczkaY.append(y[wierzcholki_id[i]])
    lines[0].set_data(otoczkaX, otoczkaY)
    for i in range(0, ilosc_tygrysow, 1):
        pentagramX = []
        pentagramY = []
        pentagramX.append(pentagram_list[i].getCenter()[0])
        pentagramY.append(pentagram_list[i].getCenter()[1])
        pentagramX.append(pentagram_list[i].getP1()[0])
        pentagramY.append(pentagram_list[i].getP1()[1])
        pentagramX.append(pentagram_list[i].getP3()[0])
        pentagramY.append(pentagram_list[i].getP3()[1])
        pentagramX.append(pentagram_list[i].getP5()[0])
        pentagramY.append(pentagram_list[i].getP5()[1])
        pentagramX.append(pentagram_list[i].getP2()[0])
        pentagramY.append(pentagram_list[i].getP2()[1])
        pentagramX.append(pentagram_list[i].getP4()[0])
        pentagramY.append(pentagram_list[i].getP4()[1])
        pentagramX.append(pentagram_list[i].getP1()[0])
        pentagramY.append(pentagram_list[i].getP1()[1])
        lines[i + 1].set_data(pentagramX, pentagramY)

    return lines



#inicjalizacja programu
wysokosc = 20
maxX = 400
maxY = 400

ilosc_tygrysow = 10
x_s = wysokosc + (maxX-wysokosc*2)*np.random.rand(ilosc_tygrysow)
y_s = wysokosc + (maxY-wysokosc*2)*np.random.rand(ilosc_tygrysow)
vel_val = np.sqrt(np.square(maxX) + np.square(maxY))
vel = vel_val/200 + vel_val/100*np.random.rand(ilosc_tygrysow)
katy_pochylenia = 360*np.random.rand(ilosc_tygrysow)


pentagram_list = []
for i in range(0, ilosc_tygrysow, 1):
    pentagram = Pentagram(x_s[i], y_s[i], wysokosc, katy_pochylenia[i], vel[i])
    pentagram_list.append(pentagram)

plt.style.use('dark_background')
fig, ax = plt.subplots()
ax.set_xlim(0, maxX)
ax.set_ylim(0, maxY)
plt.title("Szatańskie tygrysy")

lines = []
lines.append(ax.plot([], [], 'b--', lw=2)[0])
for i in range(0, ilosc_tygrysow, 1):
    lines.append(ax.plot([], [], 'r-')[0])

anim = animation.FuncAnimation(fig, animate, init_func=init, interval=20, blit=True, repeat=False)

plt.show()
