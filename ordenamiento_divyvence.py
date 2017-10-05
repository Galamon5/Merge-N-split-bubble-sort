import random
import math

def main():
    size = int(input("Introduce el tamaño del arreglo\n"))
    div = int(input("Introduce el numero de divisiones\n"))
    arrayNum = createArray(size)
    print("El arreglo original es",arrayNum)
    arraySort(arrayNum,div)

def createArray(size):
    arrayAux = []
    i = 0
    for i in range(size):
        arrayAux.append(random.randint(0,size))
    return arrayAux

def arraySort(arrayNum,div):
    size = len(arrayNum)
    numDiv = int(size/div)
    if(size<=1):
        print("Ordenado! \n",arrayNum)
    else:
        if(size<=div):
            print("El numero de divisiones es mayor o igual que el tamaño del arreglo\n")
            arraySort(arrayNum,div-1)
        else:
            print("Se puede dividir!\n")
            for i in range(div-1):
                if()


def merge(arrayNum,):
    print("Ordenando")

def bubbleSort():
    print("Ordenando")

main()
input("Pulsa una tecla para continuar...")
