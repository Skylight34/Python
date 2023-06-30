import math

#Definimos la longitud del arreglo
LongitudArreglo = int(input("Dame la longitud del arreglo: "))

#Definimos el arreglo vacio que le agregaremos datos
Arreglo = []

#Hace el arreglo
for i in range(LongitudArreglo):
  ElementoArreglo = input("Dame el elemento " + str(i) + " del Arreglo: ")
  Arreglo += ElementoArreglo

#Imprime el arreglo
print(Arreglo)

#Reversa el arreglo
i = 0

for n in range(math.floor(int(LongitudArreglo)/2)):
    i = i - 1
    Arreglo[n], Arreglo[i] = Arreglo[i], Arreglo[n]
    



#Imprime el arreglo al reves
print(Arreglo)
