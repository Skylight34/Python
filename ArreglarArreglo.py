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
inicio = 0
fin = LongitudArreglo - 1
while inicio < fin:
    Arreglo[inicio], Arreglo[fin] = Arreglo[fin], Arreglo[inicio]
    inicio += 1
    fin -= 1


#Imprime el arreglo al reves
print(Arreglo)
