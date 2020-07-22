
#-*- coding: utf-8 -*-
import math

#Programa primera tarea Analisis de Algoritmos 2020-1

""" ALGORITMO PARA SABER SI UN ELEMENTO SE ENCUENTRA AL MENOS N/3 VECES EN UN ARREGLO
    DE TAMAÑO N Y DEVOLVERLO EN CASO QUE EXISTA"""

def emperador (arr):
    if len(arr)==0:
        return "empty list"
    else:
        monDict = {} #creamos un nuevo diccionario, hacer consultas toma O(1)
        for x in arr: #recorremos una vez el arreglo esto es O(n)
            if x in monDict:# guardamos el elemento en la llave y las repeticiones en el valor
                monDict[x]+= 1
            else:
                monDict[x] = 1
        varMax=(0,0) #Tupla que nos dirá cuál es el elemento con más repeticiones
        for i,j in monDict.items(): #Buscaremos en todos los elementos, es a lo más O(n)
            if j > varMax[1]:
                varMax = (i,j)
        if varMax[1] >= math.ceil(len(arr)/3): #vemos si el elemento aparece al menos n/3 veces
            return varMax[0]
        else:
            return "the elem doesn't exist"


""" Given n integers between 0-k preprocess the input and answer how many integers
    fall in a range [a..b] in O(1) """

def repetitions(lista, k, a, b): #K es el máximo número, a y b el rango.
    if a<0 or b>k:
        return "error"
    else:
        l1=process(lista,k)
        return (l1[b])-(l1[a-1]) if a!=0 else l1[b]

#Método auxiliar para preprocesar la entrada, esto tomará tiempo O(3n)
def process(lista, k):
    aux=[]
    for x in range(k+1):
        aux.append(0)
    for x in lista:
        aux[x]+=1
    print(aux)
    for x in range(1,k+1):
        elem=aux[x]
        aux[x]=elem+aux[x-1]
    print(aux)
    return aux

"""Dado una lista, hallar el mayor y el menor elemento """

def mayMin(lista):
    l1=separa(lista) #Llamamos a nuestro método auxiliar.
    a=l1[0] # encerramos mayor elemento en una lista y el menor en otra
    b=l1[1]
    #el íltimo elemento que queda en la lista es el mayor/menor
    while len(a)>1: #ambas listas tienen longitudes iguales
        for x in range(len(l1[0])//2):
            if a[x]<a[x+1]:
                del a[x] #comparamos y eliminamos los menores de "a"
            else:
                del a[x+1]
            if b[x]>b[x+1]:
                del b[x] #eliminamos los mayores de b
            else:
                del b[x+1]
    return "El mayor elemento es: " +str(a[0])+ "\nEl mínimo es: " + str(b[0])

"""Método auxiliar de mayMin que toma tuplas de una lista y envía los elementos
   mayores de cada tupla a una lista y los menores a otra, esto causa que el
   elemento máximo siempre se halle en una lista y el mínimo en la otra."""

def separa(lista):
    mayores=[]
    menores=[]
    for x in range(len(lista)//2):
        e1=lista.pop(0)
        e2=lista.pop(0)
        if e1>e2:
            mayores.append(e1)
            menores.append(e2)
        else:
            mayores.append(e2)
            menores.append(e1)
    #en caso que la lista tenga longitud impar, el último elemento se añade a ambas listas
    if len(lista)==1:
        mayores.append(lista[0])
        menores.append(lista[0])
    return (mayores, menores)


"""Implementación de Radix Sort. Ordenaremos en tiempo O(n) n elementos que se
   encuentran entre los valores de 1 y m con "m" cuadrática"""

def radixSort(lista,m):
    d = len(str(m))
    l1=lista.copy()
    for x in range (d):
        l1=ordenaPor(l1,-(x+1))
    return l1

#Algoritmo auxiliar de RadixSort, dada la lista, la ordena por determinado dígito.

def ordenaPor(lista, pos):
    #arreglo con 10 arreglos, corresponde la posición al dígito pos por el que
    #estamos ordenando en cada llamada.
    laux=[[],[],[],[],[],[],[],[],[],[]]
    b=[]
    #al ser un algorítmo estable, necesitamos insertar los elementos ya ordenados
    #en el orden que ya se les asignó. Se llena la lista de 9 listas.
    for x in lista:
        if abs(pos) > len(str(x)):
            b+=[x]
        else:
            a=str(x)[pos]
            laux[int(a)].append(x)
    #al final se concatena todo en una misma lista b
    for x in laux:
        b+=x
    return b

"""Dada una lista de 'n' enteros y un número 'y', encontrar un algoritmo que en
   O(nlogn) encuentre la pareja (i,j) de numeros xi+yi<=y tal que maximice xi+yi"""

def maximiza(lista, y):
    if len(lista)<2:
        raise Exception("Sorry, empty or 1 element list")
    #ordenar la lista toma O(nlogn)
    lista.sort()
    #a y b son índices, comenzamos con a al inicio de la lista y b al final
    a=0
    b=len(lista)-1
    #guardaremos el elemento que más se aproxime a y
    maximo=(lista[a]+lista[b],a,b)
    while(a!=b):
        x=lista[a]+lista[b]
        #si son iguales ya acabamos
        if x==y:
            return (a,b)
        elif x<y:
        #sino, hay que ver si es mayor a nuestro máximo
            if maximo[0]<x:
                maximo=(x,a,b)
            a+=1
        else:
            b-=1
    #devolvemos los índices de máximo
    return (maximo[1],maximo[2])

lista=[40, 1, 2, 113, 5, 3, 3, 66, 4, 4, 5, 87, 5, 5, 6, 7, 7, 108, 8, 9]
print(maximiza([1],1000))

# fibonacci con recursión de cola
def fibcola(n,cb1,cb2):
    if n==0:
        return cb1
    elif n==1:
        return cb1,cb2
    else:
        return fibcola(n-1,cb2,cb1+cb2)
