"""
CI-2125 Computacion I
Proyecto 1: Simulacion de trafico 
Integrante(s)/Carnet(s): Ángel Mujica/1610776, Luis Becerra/1910557
*
*
"""

"""
Benchmark 
"""
#Respuesta 1
#Se define una lista donde True representa las casillas
#ocupadas y False las vacías

#Respuesta 2
A=[True, False, True, True, False, False, False, False, False, False, True]

#Respuesta 3
#L recibe una lista e i recibe la casilla que queremos chuequear
#dentro de la lista
def ocupada(L, i):
    if L[i]==True:
        return True
    else:
        return False

#Respuesta 4
#Pueden existir n cantidad de filas si y solo si son definidas

#Respuesta 5
#el código se explica sólo, sumamente sencillo, L1
#tomará valor de lista e igualmente M2 para posteriormente
#compararlas
def igual(L1, M2):
    if L1==M2:
        return True
    else:
        return False

#Respuesta 6 L1 es la lista y nuevo_carro el booleano que
#determinará si se agrega vehículo en A[0]
#las modificaciones de L se guardarán como B
def avanzar(L1, nuevo_carro):
    #primero hacemos que avance el último puesto
    if L1[-1]==True:
        L1[-1]=False
    #ahora asignamos una variable que determine la posición
    #de la última casilla
    u_c=len(L1)-1
    #len(L1) nos da la longitud de la lista contando desde
    #el 1, por lo tanto, para que no haya error, restaremos
    #uno para que así u_c sea igual al espacio de la última
    #casilla
    #así podemos proceder con un for usando la función range
    for i in range(u_c, -1, -1):
        #acá el inicio se da en u_c, se finaliza en -1
        #debido a que intenté con 0 y excluía la casilla 0
        #update: ya ví por qué, es que se hace como otra
        #lista con orden invertido, épico
        if L1[i]==False:
            if L1[i-1]==True:
                B=L1
                B[i]=True
                B[i-1]=False
    if nuevo_carro==True:
        B[0]=True
        #figura 2(c)
        return B
    else:
        #figura 2(b)
        return B

#Respuesta 7
#definimos r7 como la lista predeterminada para avanzarFin()
r7=[True, False, True, True, False, True, True, False, False, False, False]
#offtopic, estuve trancado en la pregunta 6 por días
#pero ahora aplicaré una lógica parecida para todas las demás B)
def avanzarFin(L, m):
    #esta vez usaremos u_c para última casilla y m 
    #para la casilla desde donde empezará el movimiento
    if L[-1]==True:
        L[-1]=False
    u_c=len(L)-1
    for i in range(u_c, m-u_c, -1):
        #donde m-u_c nos permite obtener el espacio relativo
        #de m con con respecto a L[0]=L'[-1] que fue lo que
        #comenté como update en la línea 60
        if L[i]==False and L[i-1]==True:
            B=L
            B[i]=True
            B[i-1]=False
        else:
            pass
        return B
    
#Respuesta 8
#okay, here we go again
r8=[True, False, True, True, True, False, False, True, True, False, False]
def avanzarComienzo(L, b, m):
    while L[m]==True:
        #inserté esto para un caso hipotético donde L[m]
        #esté ocupado, así buscamos la primera casilla
        #libre de izquierda a derecha
        m=m-1
    else:
        for i in range(m, -1, -1):
            #lógica parecida a la de antes, sólo que ahora
            #empezamos desde m en lugar de u_c
            if L[i]==False and L[i-1]==True:
                B=L
                B[i]=True
                B[i-1]=False
        if b==True:
            B[0]=True
            return B
        else:
            return B

#Respuesta 9
r9=[True, True, False, True, True, False, False, True, True, False, False]
def avanzarComienzoBloque(L, b, m):
    for i in range(m-1, -1, -1):
            #admito que hice copy paste de la pregunta anterior
            #modificando para que ahora empiece en m-1 XD
            if L[i]==False and L[i-1]==True:
                B=L
                B[i]=True
                B[i-1]=False
            if b==True:
                B[0]=True
                print(B)
            else:
                print(B)

#Respuesta 10
#ay Dios mío, ahora es que viene lo bueno
r10x=[True, False, True, True, False, True, True, False, False, False, False]
r10y=[True, False, True, True, True, True, False, False, False, False, False]
def avanzarFilas(L1, b1, L2, b2):
    m=(len(L1)+1)/2
    u_c=len(L1)-1
    #nota: hay que modificar si len(L1)!=len(L2)
    R1=L1
    R2=L2
    for i in range(u_c, -(m)-1, -1):
            if L1[i]==False and L1[i-1]==True:
                R1=L1
                R1[i]=True
                R1[i-1]=False
            if b1==True:
                R1[0]=True
            else:
                pass
    for i in range(u_c, -(m)-1, -1):
            if L2[i]==False and L2[i-1]==True:
                R2[i]=True
                R2[i-1]=False
            else:
                pass
    for i in range(m, -1, -1):
        if i==m:
            if L1[i]==True:
                if L1[i+1]==False:
                    R1[i+1]==True
                    R1[i]==False
                L2[i]=False
            elif L2[i]==True:
                if L2[i+1]==False:
                    R2[i+1]=True
                    R2[i]=False
                L1[i]=False
            elif L1[i]==False and L2[i]==False:
                if L1[i-1]==True:
                    R1[i]=True
                    R1[i-1]==False
                elif L2[i-1]==True and L1[i-1]==False:
                    R2[i]=True
                    R2[i-1]=False
        else:
            if L1[i]==False and L1[i-1]==True:
                R1[i]=True
                R1[i-1]=False
            if L2[i]==False and L2[i-1]==True:
                R2[i]=True
                R2[i-1]=False
    if b1==True:
        R1[0]=True
    if b2==True:
        R2[0]=True
    showtime=[R1, R2]
    return showtime

#Respuesta 11
#Devuelve [[False, False, True, False, True], [True, True, False, True, False]]

#Respuesta 12
#Si se introduce avanzarFilas(L1, True, L2, True) o
#avanzarFilas(L1, True, L2, False) indefinidamente, los carros
#en L2 tenderán a estar atrapados infinitamente

#Respuesta 13
#se necesitan mínimo 10 etapas, 5 para que el primer carro de la línea
#horizontal esté a punto de salir y la casilla central quede libre
#en la sexta etapa se empiezan a agregar nuevos carros a la
#lista horizontal y finalmente en la 10 llegamos al caso esperado

#Respuesta 14
#no se puede porque la función saca automáticamente el vehículo
#de la última casilla y para apilar 4 carros al final de cada
#línea se necesitan al menos 5 etapas (eso si ya los 
# tenemos posicionados en las 4 primeras filas), además, si
#los 4 primeros puestos de L1 están llenos, L2 necesita que pasen
#5 etapas para poder avanzar, es decir, cuando L2 empieza a 
#posicionar sus carros en las últimas casillas, ya L1 ha
#perdido 2 carros

#Respuesta 15
P=[1, 1, 1, 2, 2, 3, 4, 5, 6, 7, 7]
def elimDoble(L):
    u_c=len(L)-1
    for i in range(u_c):
        if i<=L[-1] and L[i]==L[i+1]:
            L.remove(L[i+1])
    else:
        pass

#Respuesta 16
#Así como está planteado devuelve la lista tal y como se insertó,
#lo cual es lógico ya que lista[0]==lista[1]
def dobles(lista):
    if len(lista)>1:
        if lista[0]!=lista[1]:
            return [lista[0]]+ dobles(lista[1:])
        del lista[1]
        return dobles(lista)
    else:
        return lista

#Respuesta 17
#la función dobles() que usted definió no hizo nada, 
#pero elimDoble() no puede eliminar números repetidos
#desordenados ya que compara solamente casillas consecutivas

#Respuesta 18
#la función busqueda() toma un valor llamado final que será una lista
#en este caso, también toma un llamado valor inicial con el que se
#operará para verificar si partiendo de esa configuración se
#puede llegar a la configuración final. La variable final puede
#ser cualquier tipo de objeto en python, pero en este caso se
#utilizan las listas debido al planteamiento que se dió.
#La variable espacio es una lista de listas y es donde se
#guarda y opera el valor inicial.
#La función sucesores crea una lista vacía y la llena con otras listas
#que ejecutan la simulación. sucesores(L) regresa una lista de listas
def busqueda(final,inicial):
    espacio = [inicial]
    stop = False
    while not stop:
        anterior = espacio
        espacio = espacio + sucesores(espacio)
        espacio.sort() #ordenar en orden creciente
        espacio = elimDoble(espacio)
        stop = igual(anterior,espacio) #Definida en la pregunta 5
        if final in espacio:
            return True
    return False

def sucesores(L):
    res = []
    for x in L:
        L1 = x[0]
        L2 = x[1]
        res.append( avanzarFilas(L1, False, L2, False))
        res.append( avanzarFilas(L1, False, L2, True))
        res.append( avanzarFilas(L1, True, L2, False))
        res.append( avanzarFilas(L1, True, L2, True))
    return res

#Respuesta 19
#Si el elemento buscado está en las primeras casillas, es más
#eficiente usar in1(), sin embargo, a parte de que el método
#que usa in2() para listas pequeñans es bastante eficiente,
#mientras más larga sea la lista, más eficiente se vuelve in2()
#explicado con ejemplos tenemos dos casos, en el primero necesitamos
#encontrar el elemento L[50] en una lista de 51 elementos con in1()
#y en el segundo necesitamos encontrar el elemento L[0] con in2()
#en el caso de in1() se debe recorrer la lista completa para
#hallar la solución, mientras que en el caso de in2() sólo 
#necesitamos 6 ejecuciones del bloque de código.
#Si bien hay casos bastante particulares donde in1() arroja el
#resultado más rápido, in2() es sin duda alguna más eficiente.
def in1(elemento,lista):
    a = 0
    b = len(lista) - 1
    while a <= b and elemento >= lista[a]:
        if elemento == lista[a]:
            return True
        else:
            a = a + 1
    return False

def in2(elemento,lista):
    a = 0
    b = len(lista) - 1
    while a < b :
        pivote = (a + b) // 2
        if lista[pivote] < elemento :
            a = pivote + 1
        else:
            b = pivote
    if elemento == lista[a]:
        return True
    else:
        return False

#Respuesta 20
#Profe, hice un binario de 32 bits. xD
test=[True, False, True, False, True]
def enEntero(L):
    u_c=len(L)-1
    h=(len(L))*[True]
    result=0
    for n in range(u_c, -1, -1):
        if n==u_c:
            a=1
        else:
            a=2*a
        if L[n]==h[n]:
            result=result+a
        else:
            result=result
    return result

#Respuesta 21
#La condición es i>=0
def enFila(n,talla):
    res = talla * [False]
    i = talla - 1
    while i>=0:
        if (n % 2) != 0:
            res[i] = True
        n = n // 2
        i = i - 1
    return res

#Respuesta 22
def busqueda2(inicial, final):
    espacio = [inicial]
    stop = False
    while not stop:
        a=1
        anterior = espacio
        espacio = espacio + sucesores(espacio)
        espacio.sort() #ordenar en orden creciente
        espacio = elimDoble(espacio)
        stop = igual(anterior,espacio) #Definida en la pregunta 5
        if final in espacio:
            return a
        else:
            a=a+1
    return False