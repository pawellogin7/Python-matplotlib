import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation
import numpy as np
from PIL import Image

class Tiger():
    def __init__(self, ident, x0, y0, width, height):
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
ilosc_tygrysow = 30
maxX = 1000.0
maxY = 1000.0
x = (maxX - imageWidth)*np.random.rand(ilosc_tygrysow)
y = (maxY - imageHeight)*np.random.rand(ilosc_tygrysow)

#Tworzenie listy klasy Tiger
tigerList = []
for i in range(0, ilosc_tygrysow, 1):
    tigerList.append(Tiger(i, x[i], y[i], imageWidth, imageHeight))

#Zapis wszystkich punktów na rogach obrazkow tygrysow
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


#Stosowanie algorytmu Jarvisa do wyznaczenia otoczki wypuklej
wierzcholki_id = []
wierzcholki_id.append(minid)
for j in range(0, len(punktyTygrysy), 1):
    next_point_id = 0
    kat_max = 0
    #Szukanie największego kąta między wektorami
    for i in range(0, len(punktyTygrysy), 1):
        if i == wierzcholki_id[len(wierzcholki_id) - 1] or i == wierzcholki_id[len(wierzcholki_id) - 2]:
            continue

        if len(wierzcholki_id) == 1:
            x1 = x0 - 1
            y1 = y0
            x2 = x0
            y2 = y0
        else:
            x1 = punktyTygrysy[wierzcholki_id[len(wierzcholki_id) - 2]][0]
            y1 = punktyTygrysy[wierzcholki_id[len(wierzcholki_id) - 2]][1]
            x2 = punktyTygrysy[wierzcholki_id[len(wierzcholki_id) - 1]][0]
            y2 = punktyTygrysy[wierzcholki_id[len(wierzcholki_id) - 1]][1]
        x3 = punktyTygrysy[i][0]
        y3 = punktyTygrysy[i][1]
        v1x = x2 - x1
        v1y = y2 - y1
        v2x = x3 - x2
        v2y = y3 - y2
        kat = 180 - np.arccos((v1x*v2x + v1y*v2y) / (np.sqrt(v1x*v1x + v1y*v1y) * np.sqrt(v2x*v2x + v2y*v2y)))
        if kat > kat_max:
            next_point_id = i
            kat_max = kat
    if next_point_id == minid:
        break
    else:
        wierzcholki_id.append(next_point_id)


print(wierzcholki_id)

fig, ax = plt.subplots()
DPI = fig.get_dpi()
fig.set_size_inches(maxX/float(DPI), maxY/float(DPI))
ax.set_xlim(0, maxX)
ax.set_ylim(0, maxY)


#Rysowanie tygrysow(jako zielony kwadrat)
for i in range(0, len(tigerList), 1):
    ab = AnnotationBbox(imagebox, (tigerList[i].point1()[0] + imageWidth/2,
                                   tigerList[i].point1()[1] + imageHeight/2))
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

#Rysowanie otoczki wypuklej
for i in range(0, len(wierzcholki_id) - 1, 1):
    id1 = wierzcholki_id[i]
    id2 = wierzcholki_id[i + 1]
    xVal = [punktyTygrysy[id1][0], punktyTygrysy[id2][0]]
    yVal = [punktyTygrysy[id1][1], punktyTygrysy[id2][1]]
    ax.plot(xVal, yVal, 'b-')
ax.plot([punktyTygrysy[wierzcholki_id[0]][0], punktyTygrysy[wierzcholki_id[len(wierzcholki_id) - 1]][0]],
         [punktyTygrysy[wierzcholki_id[0]][1], punktyTygrysy[wierzcholki_id[len(wierzcholki_id) - 1]][1]], 'b-')



plt.show()