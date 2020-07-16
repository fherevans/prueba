
#-*- coding: utf-8 -*-
import math

#Programa primera tarea Analisis de Algoritmos 2020-1

#ALGORITMO PARA SABER SI UN ELEMENTO SE ENCUENTRA AL MENOS N/3 VECES EN UN ARREGLO
#DE TAMAÑO N Y DEVOLVERLO EN CASO QUE EXISTA

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
