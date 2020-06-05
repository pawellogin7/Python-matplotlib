import matplotlib.pyplot as plt
from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation
import numpy as np
from PIL import Image


class Tiger():
    def __init__(self, ident, x0, y0, height, width):
        self.id = ident
        self.p1 = [x0, y0]
        self.p2 = [x0 + width, y0]
        self.p3 = [x0 + width, y0 + height]
        self.p4 = [x0, y0 + height]

    def point1(self):
        return self.p1
    def point2(self):
        return self.p2
    def point3(self):
        return self.p3
    def point4(self):
        return self.p4
    def getId(self):
        return self.id

def alfa(x, y, xa, ya):
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
    line.set_data([], [])
    return line,

def animate(i):
    x = []
    y = []
    for j in range(0, i + 1, 1):
        if (anim_frames[j] >= 0):
            x.append(punktyTygrysy[anim_frames[j]][0])
            y.append(punktyTygrysy[anim_frames[j]][1])
        else:
            x.pop()
            y.pop()
    line.set_data(x, y)
    return line,

#Wczytywanie obrazu
tygrys_obraz = Image.open('tygrysek.png')
imageWidth, imageHeight = tygrys_obraz.size
print(imageWidth)
print(imageHeight)
zoomVal = 1
imagebox = OffsetImage(tygrys_obraz, zoom=zoomVal)
imageWidth *= zoomVal*2
imageHeight *= zoomVal*2

#Losowanie punktów
ilosc_tygrysow = 10
maxX = 1000.0
maxY = 1000.0
x = (maxX - imageWidth)*np.random.rand(ilosc_tygrysow)
y = (maxY - imageHeight)*np.random.rand(ilosc_tygrysow)

#Tworzenie listy klasy Tiger
tigerList = []
for i in range(0, ilosc_tygrysow, 1):
    tigerList.append(Tiger(i, x[i], y[i], imageHeight, imageWidth))

#Zapis wszystkich punktów tygrysow(na rogach obrazkow)
punktyTygrysy = []
for i in range(0, ilosc_tygrysow, 1):
    punktyTygrysy.append(tigerList[i].point1())
    punktyTygrysy.append(tigerList[i].point2())
    punktyTygrysy.append(tigerList[i].point3())
    punktyTygrysy.append(tigerList[i].point4())

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

#Obliczanie katow nachylenia punktow do punktu minimum
alfa_list = np.zeros(len(punktyTygrysy))
for i in range(0, len(punktyTygrysy), 1):
    if i == minid:
        alfa_list[i] = 0
    else:
        alfa_list[i] = alfa(punktyTygrysy[i][0], punktyTygrysy[i][1], x0, y0)

#Sortowanie wzgledem katow nachylenia
alfa_sorted_id = []
alfa_sorted_id.append(minid)
for i in range(0, len(alfa_list) - 1, 1):
    alfa_min = 1000
    alfa_min_id = 0
    for j in range(0, len(alfa_list), 1):
        if alfa_list[j] < alfa_min and alfa_list[j] >= 0 and j != minid:
            alfa_min_id = j
            alfa_min = alfa_list[j]
    alfa_sorted_id.append(alfa_min_id)
    alfa_list[alfa_min_id] = -1

#Stosowanie algorytmu Grahama do wyznaczenia otoczki wypuklej
wierzcholki_id = []  #lista posortowanych wierzcholkow
anim_frames = []  #lista krokow animacji
wierzcholki_id.append(alfa_sorted_id[0])
anim_frames.append(alfa_sorted_id[0])
wierzcholki_id.append(alfa_sorted_id[1])
anim_frames.append(alfa_sorted_id[1])
wierzcholki_id.append(alfa_sorted_id[2])
anim_frames.append(alfa_sorted_id[2])
iter = 3
while iter < len(alfa_sorted_id):
    x1 = punktyTygrysy[wierzcholki_id[len(wierzcholki_id) - 2]][0]
    y1 = punktyTygrysy[wierzcholki_id[len(wierzcholki_id) - 2]][1]
    x2 = punktyTygrysy[wierzcholki_id[len(wierzcholki_id) - 1]][0]
    y2 = punktyTygrysy[wierzcholki_id[len(wierzcholki_id) - 1]][1]
    x3 = punktyTygrysy[alfa_sorted_id[iter]][0]
    y3 = punktyTygrysy[alfa_sorted_id[iter]][1]

    a = np.array([[x1, y1, 1], [x2, y2, 1], [x3, y3, 1]])
    det = np.linalg.det(a)

    #det macierzy mowi, po ktorej stronie prostej 1-2 lezy punkt 3
    if det >= 0:  #punkt po prawej
        wierzcholki_id.append(alfa_sorted_id[iter])
        anim_frames.append(alfa_sorted_id[iter])
        iter += 1
    else:  #punkt po lewej
        wierzcholki_id.pop()
        anim_frames.append(-1)

wierzcholki_id.append(alfa_sorted_id[0])
anim_frames.append(alfa_sorted_id[0])

fig, ax = plt.subplots()
DPI = fig.get_dpi()
fig.set_size_inches(maxX/float(DPI), maxY/float(DPI))
ax.set_xlim(0, maxX + imageWidth)
ax.set_ylim(0, maxY + imageHeight)


#Rysowanie tygrysow(jako zielony kwadrat)
for i in range(0, len(tigerList), 1):
    ab = AnnotationBbox(imagebox, (tigerList[i].point1()[0], tigerList[i].point1()[1]), frameon=False,
                        box_alignment=(0.0, 0.0))
    ax.add_artist(ab)

    xt = [tigerList[i].point1()[0], tigerList[i].point2()[0]]
    yt = [tigerList[i].point1()[1], tigerList[i].point2()[1]]
    ax.plot(xt, yt, 'g-', lw=1)
    xt = [tigerList[i].point2()[0], tigerList[i].point3()[0]]
    yt = [tigerList[i].point2()[1], tigerList[i].point3()[1]]
    ax.plot(xt, yt, 'g-', lw=1)
    xt = [tigerList[i].point3()[0], tigerList[i].point4()[0]]
    yt = [tigerList[i].point3()[1], tigerList[i].point4()[1]]
    ax.plot(xt, yt, 'g-', lw=1)
    xt = [tigerList[i].point4()[0], tigerList[i].point1()[0]]
    yt = [tigerList[i].point4()[1], tigerList[i].point1()[1]]
    ax.plot(xt, yt, 'g-', lw=1)

#Tworzenie animacji rysowania otoczki wypukłej
line, = ax.plot([], [], lw=2)
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=len(anim_frames),
                               interval=50, blit=True, repeat=False)

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
