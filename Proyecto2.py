# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 00:14:57 2021

@author: Juan Diego OCANDO RUIZ

Participantes: Luis Becerra (19-10557), Anthony Hernandez (18-10035) y Lorena Rojas (19-10469)
"""

import math
import os
import random
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

def cargar_imagenes(route):
    """
    carga imagenes en una carpeta, la cual transformara en matrices numpy
    y los devolvera en una lista 
    route -> direccion absoluta donde se encuentran las imagenes
    images -> lista de matrices de numpy ndarray
    """
    imagenes = []
    directory = os.fsencode(route)
    os.chdir(route)
    for file in os.listdir(directory): 
        filename  = os.fsdecode(file)
        if filename.endswith(".jpg"): 
            img = Image.open(filename)
            img.load()
            data = np.asarray(img,dtype="uint8")
            print(data.shape)
            imagenes.append(data)
            continue
        else:
            continue
    print("Se cargaron ", len(imagenes), "imagenes")
    return imagenes

def gris(p):
    #Calculamos el promedio
    prom=np.mean([p[0],p[1], p[2]])
    num=int(round(prom))
    #Retornamos el número que nos permitirá convertir
    #a escala de grises
    return np.uint8(num)

def conversion(a):
    #creo una matriz de ceros para convertirla en mi imagen en escala de grises
    img_to_Gray= np.zeros([int(np.shape(a)[0]),int(np.shape(a)[1])], dtype=np.uint8)
    #recorro la filas
    for i in range(np.shape(a)[0]):
        #recorro columnas
        for e in range(np.shape(a)[1]):
            #tomo el pixel a modificar
            px=np.array([a[i][e][0], a[i][e][1], a[i][e][2]], np.uint8)
            #convierto a gris
            gray=gris(px)
            #guardo el pixel modificado en la matriz de salida
            img_to_Gray[i][e]=np.uint8(gray)
    #retorno la imagen con elementos enteros de 8 bits
    return img_to_Gray.astype(np.uint8)

def vecinoProximo(A: np.ndarray, w: int, h: int):
    new_img = [[] for _ in range(h)]
    Zh = h / int(np.shape(A)[0])
    Zv = w / int(np.shape(A)[1])
    for x in range(h):
        for y in range(w):
            x0 = int(x / Zh)
            y0 = int(y / Zv)
            new_img[x].append(list(A[x0][y0])) 
    return new_img

def mediaLocal(A : np.ndarray, w : int, h :int):
    a = np.empty((h,w), np.uint8)
    H,W = A.shape
    ph,pw = H//h, W//w
    for I in range(0,H,ph):
        print(I)
        for J in range(0,W,pw):
            a[I//ph,J//pw]=round(np.mean(A[I:I+ph, J:J+pw]))
    return a

def TablaSuma(A):
    pass

def reduccionSumas1(A, S:np.ndarray, w:int, h:int) :
    a = np.empty((h,w), np.uint8)
    H, W = A.shape
    ph, pw = H // h, W // w
    nbp = ph * pw
    for I in range(0, H, ph):
        for J in range(0, W, pw):
            X = (S[I+ph, J+pw] -  S[I+ph, J]) - (S[I, J+pw] - S[I, J])
            a[I // ph, J // pw] = round(X / nbp)
    return a

def reduccionSumas2(A, S:np.ndarray, w:int, h:int) :
    H, W = A.shape
    ph, pw = H // h, W // w
    sred = S[0:H+1:ph, 0:W+1:pw]
    dc = sred[:, 1:] - sred[:,:-1]
    dl = dc[1:, :] - dc[:-1, :]
    d = dl / (ph * pw)
    return np.uint8(d.round())

def listaRGBtoGris(A):
    pass


def listaRedim(A,w,h):
    pass

def initMosaico(source, w:int, h:int, p:int):
    pass

def L1(a,b):
    pass

def escogerMiniatura(bloque: np.ndarray, miniaturas ):
    lista_comp=[]
    for l in range(len(miniaturas)):
        lista_comp=lista_comp.append(L1(bloque, miniaturas[l]))
    num_selec=lista_comp[-1]
    ind=-1
    for p in range(len(lista_comp)):
        if lista_comp[p]<num_selec:
            num_selec=lista_comp[p]
            ind=p
        else:
            continue
    min_selec=miniaturas[ind]
    return min_selec

def construirMosaico(source, vignettes, p):    
    pass

"Parte I: Pixeles e imagenes"


"1.1 Pixeles"

#################################### Respuesta 1 #####################################            
# Un solo pixel de 8 bits cuenta con 256 posibles valores, lo que significa más de 
# 16 millones de combinaciones de colores.


#################################### Respuesta 2 #####################################
pixelBlanco = np.array([255, 255, 255], dtype=np.uint8) #Pixel de color blanco


#################################### Respuesta 3 #####################################       
a = np.uint8(280) #La variable "a" vale 24
b = np.uint8(240) #La variable "b" vale 240
np.add(a,b) #a+b vale 8
np.subtract(a,b) #a-b vale 40
np.floor_divide(a,b) #a//b vale 0
np.divide(a,b) #a/b vale 0.1


#################################### Respuesta 4 #####################################
gris(pixelBlanco) #Click en "gris" y luego F12 para revisar la función    


"1.2 Imágenes"

#################################### Respuesta 5 #####################################
imagen = img.imread('imagen.jpg')
conversion(imagen) #Click en "conversion" y luego F12 para revisar la función


"Parte II: Redimensión de imágenes"

"2.1 Algoritmo de Interpolación por el vecino más cercano"

#################################### Respuesta 6 #####################################
vecinoProximo(imagen, 250, 175) #Click en "vecinoProximo" y luego F12 para revisar la función


"2.2 Algoritmo de reducción pormedias locales"

##################################### Respuesta 7 #####################################


"2.3 Optimizacion de la reducción por medias locales"

##################################### Respuesta 8 #####################################


##################################### Respuesta 9 #####################################


#################################### Respuesta 10 #####################################


"Parte III: Preparando el banco de imágenes"

#################################### Respuesta 11 #####################################


#################################### Respuesta 12 #####################################


#################################### Respuesta 13 #####################################


"Parte IV: Posicionamiento de miniaturas"

#################################### Respuesta 14 #####################################


#################################### Respuesta 15 #####################################


#################################### Respuesta 16 #####################################


#################################### Respuesta 17 #####################################


#################################### Respuesta 18 #####################################


#################################### Respuesta 19 #####################################
