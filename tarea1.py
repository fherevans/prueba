
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

def repetitions(lista, k, a, b):
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

print(repetitions([1,4,8,9,4,24,77,35,7,5,3,2,2,33,34,8,9,0,11,2],77,4,7))
