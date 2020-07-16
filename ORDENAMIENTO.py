import math
#Programando algoritmos de ordenamiento.

#MergeSort Recursivo
def mergeSort (lista):
    mitad=int(math.ceil(len(lista)/2))
    if mitad >= 1:
        l1=mergeSort(lista[:mitad])
        l2=mergeSort(lista[mitad:])
        return merge(l1,l2,[])
    else:
        return lista

#Auxiliar de Merge sort recursivo también
def merge (l1, l2, l3):
    if not (l1 and l2):
        return (l3+l1+l2)
    else:
        if l1[0] > l2[0]:
            a=l2.pop(0)
            return merge(l1, l2, l3+[a])
        else:
            a=l1.pop(0)
            return merge(l1, l2, l3+[a])

#quicksort Recursivo
def quicksort(listA):
    if len(listA) < 2:
        return listA
    else:
        piv = listA.pop(len(listA)//2)
        maj=min=[]
        for x in listA:
            if x<piv:
                min=min+[x]
            else:
                maj=maj+[x]
        return (quicksort(min) + [piv] + quicksort(maj))
