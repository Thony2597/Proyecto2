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
import glob
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

def showImage(image,gray):
    if (gray):
        plt.imshow(image,cmap= 'gray')
    else: 
        plt.imshow(image)   
    plt.show()



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


def initMosaico(source, w:int, h:int, p:int):
    pass





def splitImage(im,scl):
    M = im.shape[0]//scl
    N = im.shape[1]//scl
    bloques=np.array
    bloques = [im[x:x+M,y:y+N] for x in range(0,im.shape[0],M) for y in range(0,im.shape[1],N)]
    print('image was successfully split')
    return bloques




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
def gris(p):
    #Calculamos el promedio
    prom=np.mean([p[0],p[1], p[2]])
    num=int(round(prom))
    #Retornamos el número que nos permitirá convertir
    #a escala de grises
    return np.uint8(num)

gris(pixelBlanco) #Click en "gris" y luego F12 para revisar la función    

"1.2 Imágenes"

#################################### Respuesta 5 #####################################
imagen = img.imread('imagen.jpg')
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


conversion(imagen) #Click en "conversion" y luego F12 para revisar la función


"Parte II: Redimensión de imágenes"

"2.1 Algoritmo de Interpolación por el vecino más cercano"

#################################### Respuesta 6 #####################################
#La interpolación del vecino cercano se basa en seleccionar ciertospixeles de la imagen 
#original y multiplicarlos por un factor de escala para formar una nueva imagen redimensionada
#
#*Teninedo una imagen original de tamaño NxM y queriendo redimencionarla a una imagen de tamaño
#nxm donde 
#                               n=N*Zv -> Zv=n/N            (1)
#                               m=M*Zv -> Zv=m/M            (2)
#
#*Siendo (x,y) los pixeles de la imagen redimensionada y (x0,y0) los pixeles de la imagen original
#                                    x = x0*Zv ; y = y0*Zh   (3)
#
#*Despejo x0 y y0 de (3) para obtener las pixeles que desean extraer de la imagen original
#                                   x0 = x/Zv ; y0 = y/Zh   (4)
#
#
#NOTA: Esta interpolacion es sencilla de implementar pero no es optima por el hecho de que 
#no se usan todos lo pixeles de la imagen original en la conversión por lo que hay perdida de datos 
#en el caso de la reducción

def vecinoProximo(n, m, img):
    #Mediante list comprehenion creo un array con el numero de columnas deseadas
    new_img = [[] for _ in range(n)]
    #defino el factor de escala vertical y el factor de escala horizontal
    Zh = n / int(np.shape(img)[0])
    Zv = m / int(np.shape(img)[1])
    #incrementeo de filas
    for x in range(n):
        #incrementeo de columnas
        for y in range(m):
            x0 = int(x / Zh)
            y0 = int(y / Zv)
            new_img[x].append(list(img[x0][y0])) 
           #agrego los pixeles horizontales de la imagen original a new_img en la posición vertical variable i           
           #es como ir llenando cada fila con los valores de cada columna y al aumentar i se pasa 
           #a la sigueinte filaconvirtiendo la lista original de tamaño n en una matriz de n columnas y m filas
    return new_img

vecinoProximo(imagen, 250, 175) #Click en "vecinoProximo" y luego F12 para revisar la función


"2.2 Algoritmo de reducción pormedias locales"

##################################### Respuesta 7 #####################################


"2.3 Optimizacion de la reducción por medias locales"

##################################### Respuesta 8 #####################################


##################################### Respuesta 9 #####################################


#################################### Respuesta 10 #####################################


"Parte III: Preparando el banco de imágenes"

#################################### Respuesta 11 #####################################
def listaRGBtoGris(A :np.ndarray):
    listaImgGray = []
    for i in range(len(A)):
        listaImgGray.append(conversion(A[i]))
    print('All images were successfully converted to gray escale')
    return listaImgGray

#################################### Respuesta 12 #####################################
def listaRedim(image_list,h,w):
    miniaturas=[]
    for i in range(len(image_list)):
        miniaturas.append(vecinoProximo(h,w,image_list[i]))
    print('Lista de imagenes redimendionadas')
    return miniaturas 

#################################### Respuesta 13 #####################################
# 75x100 cada miniatura y 3750x5000 el mosaico

"Parte IV: Posicionamiento de miniaturas"

#################################### Respuesta 14 #####################################


#################################### Respuesta 15 #####################################
#Se determino la distancia entra dos imagenes mediente dos metodos diferentes, la función L1 
#calculo la distancia entre las imagenes tomando el vector RGB (cuya cada componente son el nivel 
#de rojo, verde y azul de cada imagen) de cada imagen y se determino la distancia 
#mediante la ecuacion de distancia entre dos vectores de 3 dimensiones
#
#*La funcion avarageRGB determina el porcentaje de rojo, de verde y de azul que posee una 
#imagen completa tomando en cuenta el tamaño de la imagen en pixeles
def avarageRGB(imagen):
    imagen=np.array(imagen)
    height,width,rgb = np.shape(imagen)
    pixels= height*width
    rgbMean=[0,0,0]
    for c in range(3):
        for y in range(imagen.shape[0]):
            for x in range(imagen.shape[1]):
                rgbMean[c]+=imagen[y][x][c]
    rgbMean[0]= rgbMean[0]//pixels
    rgbMean[1]= rgbMean[0]//pixels
    rgbMean[2]= rgbMean[0]//pixels
    return rgbMean


def L1(imagenA,imagenB):
    rgbA = avarageRGB(imagenA)
    rgbB = avarageRGB(imagenB)
    d= np.sqrt(np.square(rgbA[0]-rgbB[0]) + np.square(rgbA[1]-rgbB[1]) + np.square(rgbA[2]-rgbB[2]))
    return d

#De forma similar se tomo la distancia entre dos funciones que estan en escala de grises
#midiendo el nivel de gris de cada una de ellas y restandolos entre si

def avarageGray(imagen):
    imagen=np.array(imagen)
    height,width = np.shape(imagen)
    pixels= height*width
    grayMean=0
    for y in range(imagen.shape[0]):
        for x in range(imagen.shape[1]):
            grayMean+=imagen[y][x]
    grayMean=grayMean//pixels
    return grayMean

def L1Gray(imageA,imageB):
    grayMeanA=avarageGray(imageA)
    grayMeanB=avarageGray(imageB)
    distance=grayMeanA-grayMeanB
    return distance
#################################### Respuesta 16 #####################################

def escogerMiniatura1(bloque,listaImg):#anthony
    match= []
    for i in range(len(listaImg)):
        #determina la distancia entre el bloque seleccionado
        #y cada una de las imagenes del banco de imagenes
        match.append(L1(bloque,listaImg[i]))
    match=np.array(match)
    #determina el indice de la miniatura cuya distancia es la mas proxima al bloque seleccionado
    minValueIndex = match.argmin()
    return minValueIndex

def escogerMiniatura2(bloque: np.ndarray, miniaturas ):#Luis
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

#escogerMiniaturaGray: se plantea el mismo procedimiento pero evaluando las imagenes en escala de grises
#y se observo mejores resultados cuando la comparación se hizo a color.
def escogerMiniaturaGray(grayBloq,grayList):
    index=[]
    for i in range(len(grayList)):
        index.append(abs(grayBloq-grayList[i]))
    index=np.array(index)
    minValueIndex = index.argmin()
    return minValueIndex



#################################### Respuesta 17 #####################################
#splitImage(im,scl) Divide una imagen segun el parametro scl. Con scl=50 se dividen tanto 
#las columnas como las filas de la imagen entre 50 

def splitImage(im,scl):
    M = im.shape[0]//scl
    N = im.shape[1]//scl
    bloques=np.array
    bloques = [im[x:x+M,y:y+N] for x in range(0,im.shape[0],M) for y in range(0,im.shape[1],N)]
    print('image was successfully split')
    return bloques
#######

#loadImgFromFolder(): guarda las imagende de una lista todas las imagenes que se encuentren
#en una ruta dada

def loadImgFromFolder():
    ruta='C:/Users/Thonny/Documents/Python/imagenes/*.jpg'
    image_list = []
    for images in glob.glob(ruta): #assuming gif
        im=img.imread(images)
        image_list.append(im)
    print('Images were succesfully loaded')
    return image_list

########

def construirMosaico(sourceImage,scale):
    #1)Reduzco el tamaño de la imagen fuente para acelerar el proceso de procesamiento
    source=vecinoProximo((np.shape(sourceImage)[0])//8,(np.shape(sourceImage)[1])//8,sourceImage)
    
    #2)Cargar banco de imagenes
    image_list= loadImgFromFolder()

    #2)dividir la imagen fuente en bloques 
    bloques = splitImage(source,scale)

    #3)crear miniaturas con las dimensiones de un bloque
    miniaturas=[]
    miniaturas=listaRedim(image_list,np.shape(bloques[0])[0],np.shape(bloques[0])[1])
    print('Mineaturas creadas')

    #4)Asignar una miniatura a cada bloque
    index=[]
    for i in range (len(bloques)):
        index.append(escogerMiniatura(bloques[i],miniaturas))
        if(i%100==0):
            print('i: ',i)
    print('Mineaturas seleccionadas')
    
    #5)sustituir cada bloque por su minuatura equivalente
    mosaico=np.empty((np.shape(fondo)[0],np.shape(fondo)[1],3),np.uint8)
    i=0
    for y in range(49):
        for x in range(49):
            mosaico[y*37 : 37*(y+1), x*50 : 50*(x+1)]=miniaturas[index[i]]
            i=i+1
    print('Photo Mosaic susccefully created')     
    return mosaico 
       
    

#################################### Respuesta 18 #####################################


#################################### Respuesta 19 #####################################
