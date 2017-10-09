import random
import math

def main():
    size = int(input("Introduce el tamaño del arreglo\n"))
    div = int(input("Introduce el numero de divisiones\n"))
    arrayNum = createArray(size)
    print("El arreglo original es: ",arrayNum)
    finalSort = arraySort(arrayNum,div)
    print("El arreglo ordenado es: ",finalSort)

def createArray(size):
    arrayAux = []
    i = 0
    for i in range(size):
        arrayAux.append(random.randint(0,size))
    return arrayAux

def arraySort(arrayNum,div):
    z = 0
    sortArray = []
    helpArray = []
    sizeArray = len(arrayNum)
    numDiv = int(sizeArray/div)
    #print(numDiv)
    if(not(sizeArray<=div)):
        #print("Se puede dividir!")
        if(sizeArray%div == 0):
            for k in range(numDiv):
                helpArray.append(k)
            for i in range(div):
                for j in range(numDiv):
                    helpArray[j] = arrayNum[z]
                    z = z+1
                #print("rama: ", helpArray)
                arraySort(helpArray,div)
                bubbleSort(helpArray)
                for l in range(len(helpArray)):
                    sortArray.append(helpArray[l])
            bubbleSort(sortArray)
        else:
            numDiv = numDiv+1
            for k in range(numDiv):
                helpArray.append(k)
            for i in range(div):
                for j in range(numDiv):
                    if(z<sizeArray):
                        helpArray[j] = arrayNum[z]
                        z = z+1
                    else:
                        helpArray.pop()
                #print("rama: ", helpArray)
                arraySort(helpArray,div)
                bubbleSort(helpArray)
                for l in range(len(helpArray)):
                    sortArray.append(helpArray[l])
            bubbleSort(sortArray)
        finalSort = sortArray
        return finalSort
        #print("rama ordenada: ",finalSort)

def bubbleSort( A ):
    for i in range( len( A ) ):
        for k in range( len( A ) - 1, i, -1 ):
            if ( A[k] < A[k - 1] ):
                swap( A, k, k - 1 )

def swap( A, x, y ):
    tmp = A[x]
    A[x] = A[y]
    A[y] = tmp

main()
input("Pulsa una tecla para continuar...")
