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
import pixel

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

def gris (p:pixel) -> np.uint8:
    promedio = np.mean(p.shape)
    resultado = np.uint8(promedio)
    if resultado==0:
        return np.uint8(0)
    if resultado<=26:
        return np.uint8(26)
    if resultado<=52:
        return np.uint8(52)
    if resultado<=77:
        return np.uint8(77)
    if resultado<=102:
        return np.uint8(102)
    if resultado<=128:
        return np.uint8(128)
    if resultado<=153:
        return np.uint8(153)
    if resultado<=180:
        return np.uint8(180)
    if resultado<=204:
        return np.uint8(204)
    if resultado<=231:
        return np.uint8(231)
    if resultado==255:
        return np.uint8(255)

def conversion(a):
    

def vecinoProximo(A,w,h):
    pass

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
    pass

def reduccionSumas2(A, S:np.ndarray, w:int, h:int) :
    pass

def listaRGBtoGris(A):
    pass


def listaRedim(A,w,h):
    pass

def initMosaico(source, w:int, h:int, p:int):
    pass

def L1(a,b):
    pass

def escogerMiniatura(bloque: np.ndarray, miniaturas ):
    pass

def construirMosaico(source, vignettes, p):    
    pass

"I. Pixeles e imagenes"


"1.1 Pixeles"

#################################### Respuesta 1 #####################################            
# Un solo pixel de 8 bits cuenta con 256 posibles valores, lo que significa más de 
# 16 millones de combinaciones de colores.


#################################### Respuesta 2 #####################################
pixelBlanco = np.ndarray([255, 255, 255], dtype=np.uint8) #Pixel de color blanco


#################################### Respuesta 3 #####################################       
a = np.uint8(280) #La variable "a" vale 24
b = np.uint8(240) #La variable "b" vale 240
np.add(a,b) #a+b vale 8
np.subtract(a,b) #a-b vale 40
np.floor_divide(a,b) #a//b vale 0
np.divide(a,b) #a/b vale 0.1


#################################### Respuesta 4 #####################################
print(gris(pixelBlanco))  


"1.2 Imágenes"

#################################### Respuesta 5 #####################################

