#https://www.youtube.com/watch?v=_p5IH0L63wo
import numpy as np
from numpy.random import randint as rand
import matplotlib.pyplot as pyplot
import math
import random
class Komorka:
    otwarty_LG=0
    otwarty_PG=0
    otwarty_LD=0
    otwarty_PD=0
    otwarty_L=0
    otwarty_P=0
    def __init__(self,x_srodka,y_srodka,odwiedzona,rozmiar):
        self.x_srodka=x_srodka
        self.y_srodka=y_srodka
        self.rozmiar=rozmiar
        self.odwiedzona=odwiedzona
ostry=np.array(
[[0,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,1,1,0,1,1,0,0,0],
 [0,1,1,0,0,0,0,0,1,1,0],
 [1,0,0,0,0,0,0,0,0,0,1],
 [1,0,0,0,0,0,0,0,0,0,1],
 [1,0,0,0,0,0,0,0,0,0,1],
 [1,0,0,0,0,0,0,0,0,0,1],
 [1,0,0,0,0,0,0,0,0,0,1],
 [0,1,1,0,0,0,0,0,1,1,0],
 [0,0,0,1,1,0,1,1,0,0,0],
 [0,0,0,0,0,1,0,0,0,0,0]])
ostry_L=np.array(
 [[0,0,0,0,0,1,0,0,0,0,0],
  [0,0,0,1,1,0,1,1,0,0,0],
  [0,1,1,0,0,0,0,0,1,1,0],
  [0,0,0,0,0,0,0,0,0,0,1],
  [0,0,0,0,0,0,0,0,0,0,1],
  [0,0,0,0,0,0,0,0,0,0,1],
  [0,0,0,0,0,0,0,0,0,0,1],
  [0,0,0,0,0,0,0,0,0,0,1],
  [0,1,1,0,0,0,0,0,1,1,0],
  [0,0,0,1,1,0,1,1,0,0,0],
  [0,0,0,0,0,1,0,0,0,0,0]])
ostry_P=np.array(
  [[0,0,0,0,0,1,0,0,0,0,0],
   [0,0,0,1,1,0,1,1,0,0,0],
   [0,1,1,0,0,0,0,0,1,1,0],
   [1,0,0,0,0,0,0,0,0,0,0],
   [1,0,0,0,0,0,0,0,0,0,0],
   [1,0,0,0,0,0,0,0,0,0,0],
   [1,0,0,0,0,0,0,0,0,0,0],
   [1,0,0,0,0,0,0,0,0,0,0],
   [0,1,1,0,0,0,0,0,1,1,0],
   [0,0,0,1,1,0,1,1,0,0,0],
   [0,0,0,0,0,1,0,0,0,0,0]])
ostry_LG=np.array(
[[0,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,1,1,0,0,0],
 [0,0,0,0,0,0,0,0,1,1,0],
 [1,0,0,0,0,0,0,0,0,0,1],
 [1,0,0,0,0,0,0,0,0,0,1],
 [1,0,0,0,0,0,0,0,0,0,1],
 [1,0,0,0,0,0,0,0,0,0,1],
 [1,0,0,0,0,0,0,0,0,0,1],
 [0,1,1,0,0,0,0,0,1,1,0],
 [0,0,0,1,1,0,1,1,0,0,0],
 [0,0,0,0,0,1,0,0,0,0,0]])
ostry_PG=np.array(
[[0,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,1,1,0,0,0,0,0,0],
 [0,1,1,0,0,0,0,0,0,0,0],
 [1,0,0,0,0,0,0,0,0,0,1],
 [1,0,0,0,0,0,0,0,0,0,1],
 [1,0,0,0,0,0,0,0,0,0,1],
 [1,0,0,0,0,0,0,0,0,0,1],
 [1,0,0,0,0,0,0,0,0,0,1],
 [0,1,1,0,0,0,0,0,1,1,0],
 [0,0,0,1,1,0,1,1,0,0,0],
 [0,0,0,0,0,1,0,0,0,0,0]])
ostry_LD=np.array(
 [[0,0,0,0,0,1,0,0,0,0,0],
  [0,0,0,1,1,0,1,1,0,0,0],
  [0,1,1,0,0,0,0,0,1,1,0],
  [1,0,0,0,0,0,0,0,0,0,1],
  [1,0,0,0,0,0,0,0,0,0,1],
  [1,0,0,0,0,0,0,0,0,0,1],
  [1,0,0,0,0,0,0,0,0,0,1],
  [1,0,0,0,0,0,0,0,0,0,1],
  [0,0,0,0,0,0,0,0,1,1,0],
  [0,0,0,0,0,0,1,1,0,0,0],
  [0,0,0,0,0,1,0,0,0,0,0]])
ostry_PD=np.array(
 [[0,0,0,0,0,1,0,0,0,0,0],
  [0,0,0,1,1,0,1,1,0,0,0],
  [0,1,1,0,0,0,0,0,1,1,0],
  [1,0,0,0,0,0,0,0,0,0,1],
  [1,0,0,0,0,0,0,0,0,0,1],
  [1,0,0,0,0,0,0,0,0,0,1],
  [1,0,0,0,0,0,0,0,0,0,1],
  [1,0,0,0,0,0,0,0,0,0,1],
  [0,1,1,0,0,0,0,0,0,0,0],
  [0,0,0,1,1,0,0,0,0,0,0],
  [0,0,0,0,0,1,0,0,0,0,0]])
#generujemy nasz HEX labirynt
def wyswietl_komorke(hex,mapa):
    szesciokat_lg=ostry
    szesciokat_pg=ostry
    szesciokat_ld=ostry
    szesciokat_pd=ostry
    szesciokat_p=ostry
    szesciokat_l=ostry
    szesciokat=ostry
    if hex.otwarty_LG :
        szesciokat_lg=np.multiply(ostry,ostry_LG)
    if hex.otwarty_PG :
        szesciokat_pg=np.multiply(ostry,ostry_PG)
    if hex.otwarty_LD:
        szesciokat_ld=np.multiply(ostry,ostry_LD)
    if hex.otwarty_PD :
        szesciokat_pd=np.multiply(ostry,ostry_PD)
    if hex.otwarty_P :
        szesciokat_p=np.multiply(ostry,ostry_P)
    if hex.otwarty_L :
        szesciokat_l=np.multiply(ostry,ostry_L)
    szesciokat=szesciokat_lg*szesciokat_pg*szesciokat_ld*szesciokat_pd*szesciokat_p*szesciokat_l

    mapa[hex.y_srodka-math.floor(hex.rozmiar/2):hex.y_srodka+math.ceil(hex.rozmiar/2), hex.x_srodka-math.floor(hex.rozmiar/2):hex.x_srodka+math.ceil(hex.rozmiar/2)] += szesciokat

def wyswietl_mape(lista_komorek,mapa):
    for i in lista_komorek:
        wyswietl_komorke(i,mapa)
def stworz_zbior_komorek(lista,hex_sz,elementy_x,elementy_y):
    offset_x=math.floor(hex_sz/2)
    #sz_y=7
    sz_y=hex_sz-math.floor(hex_sz/2)+1
    for i in range(1,elementy_y):
        for j in range(1,elementy_x):
            #komoreczka=Komorka(j*(hex_sz-1),i*hex_sz,0,hex_sz) #by jedna scianka na siebie nachodzila
            if i%2==1:
                komoreczka=Komorka(j*(hex_sz-1),i*sz_y,0,hex_sz) #by jedna scianka na siebie nachodzila
            if i%2==0:
                komoreczka=Komorka(j*(hex_sz-1)+offset_x,i*sz_y,0,hex_sz) #by jedna scianka na siebie nachodzila
            lista.append(komoreczka)

def dist(p1,p2):
    wynik=math.sqrt((p2.x_srodka-p1.x_srodka)**2+(p2.y_srodka-p1.y_srodka)**2)
    return wynik

def wyznacz_sasiadow(komorka,lista,hex_size_n):
    #zwracamy wspolrzedne sasiadow
    sasiedzi=[]
    for i in lista:
        odleglosc=dist(komorka,i)
        if (i.x_srodka!=komorka.x_srodka or i.y_srodka!=komorka.y_srodka) and odleglosc<hex_size_n+1 and i.odwiedzona==0:
            sasiedzi.append(i)
    return sasiedzi

# definicja pozycji od prawej do konca

def sprawdz_pozycje(aktualna,sasiad,hex_s):
    pozycja=0
    if dist(aktualna,sasiad)==hex_s-1: # jest na lewo albo na prawo
        if(aktualna.x_srodka<sasiad.x_srodka): #czyli ze sasiad jest po prawej
            pozycja=0
        else:
            pozycja=3#czyli ze sasiad jest po lewej
    else :# teraz jestesmy na skosie
        if (aktualna.x_srodka<sasiad.x_srodka) and (aktualna.y_srodka<sasiad.y_srodka): # jest po prawej i na gorze PG
            pozycja=5
        elif (aktualna.x_srodka<sasiad.x_srodka) and (aktualna.y_srodka>sasiad.y_srodka): # jest po prawej i na dole PD
            pozycja=1
        elif (aktualna.x_srodka>sasiad.x_srodka) and (aktualna.y_srodka>sasiad.y_srodka): # jest po lewej i na dole LD
            pozycja=2
        elif (aktualna.x_srodka>sasiad.x_srodka) and (aktualna.y_srodka<sasiad.y_srodka): # jest po lewej i na gorze LG
            pozycja=4
    return pozycja
def otworz_sciany(aktualna,sasiad,pozycja):
        if pozycja==0: #P
            aktualna.otwarty_P=1
            sasiad.otwarty_L=1
        if pozycja==1: #PG
            aktualna.otwarty_PG=1
            sasiad.otwarty_LD=1
        if pozycja==2: #LG
            aktualna.otwarty_LG=1
            sasiad.otwarty_PD=1
        if pozycja==3: #L
            aktualna.otwarty_L=1
            sasiad.otwarty_P=1
        if pozycja==4: #LD
            aktualna.otwarty_LD=1
            sasiad.otwarty_PG=1
        if pozycja==5: #PD
            aktualna.otwarty_PD=1
            sasiad.otwarty_LG=1

stos=[]
def wyznacz_sciany(lista,hx_size):
    sasiedzi_lokalni=[]

    while len(stos)!=0:
        terazniejsza=stos.pop()
        if len(wyznacz_sasiadow(terazniejsza,lista,hx_size))!=0:
            stos.append(terazniejsza)
            sasiedzi_lokalni=wyznacz_sasiadow(terazniejsza,lista,hx_size) # wyznaczamy sasiadow
            indeks_random_sasiad=random.randint(0,len(sasiedzi_lokalni)-1)
            sasiad=sasiedzi_lokalni[indeks_random_sasiad]

            poz=sprawdz_pozycje(terazniejsza,sasiad,hx_size)
            otworz_sciany(terazniejsza,sasiad,poz) #ustawiamy sciany dla sasiednich kratek

            sasiad.odwiedzona=1 #bysmy tutaj pozniej nie weszli
            stos.append(sasiad)
            wyznacz_sciany(lista,hx_size)



lista_komorek=[]
hex_size=np.shape(ostry)[0]
elementy_na_x=20
elementy_na_y=20
stworz_zbior_komorek(lista_komorek,hex_size,elementy_na_x,elementy_na_y)
mapa=np.zeros((elementy_na_y*hex_size,hex_size*elementy_na_x)) #sluzy do wyswietlania naszego pola
#glowny algorytm ustawienia scian w szescianach
wybrana_komorka=lista_komorek[0]
wyjscie=lista_komorek[len(lista_komorek)-1] #bierzemy w prawym dolnym rogu
wyjscie.otwarty_PD=1
wybrana_komorka.otwarty_LG=1 # nasze wejscie
wybrana_komorka.odwiedzona=1 ##ustawiamy ze bylismy i lecimy dalej
stos.append(wybrana_komorka) #dodajemy do stosu

wyznacz_sciany(lista_komorek,hex_size)


wyswietl_mape(lista_komorek,mapa)


pyplot.figure(figsize=(8, 8))
pyplot.imshow(mapa, cmap=pyplot.cm.binary, interpolation='nearest')
pyplot.show()
