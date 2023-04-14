print("Fundamentos de Python")
print("Nombre: Jennifer Illescas")
print("Fecha: 10 de abril del 2023 \n")

###CURSO DE FUNDAMENTOS DE PYTHON
#1. Crear una lista de numeros del 1 al 5
print("1. Crear una lista de numeros del 1 al 5")
lista=[1,2,3,4,5]
print("Lista de numeros:",lista)
#2. Accede al elemento 3 de la lista:
print("2. Accede al elemento 3 de la lista")
print("Elemento 3 de la lista:",lista[3])
#3. Modifique un elemento de la lista:
print("3. Modifique un elemento de la lista")
lista[3]=100
print("Lista modificada:",lista)
#4. Agrega el elemento 9 al final de la lista
print("5. Agrega el elemento 9 al final de la lista")
lista.append(9)
print("Lista nueva, con el elemento 9:",lista)
#5. Eliminar el elemento 2 de la lista:
print("5. Eliminar el elemento 2 de la lista")
lista.remove(2)
print("Lista nueva, sin el elemento 2",lista)
#6. Recorrer una lista con un bucle for:
print("6. Recorrer una lista con un bucle for")
for e in lista:
    print(e)
#7. Ordenar una lista:
lista.sort()
print(lista)
lista.sort(reverse=True)
print(lista)
#8. Obtener la longitud de una lista:
print(len(lista))
#9. Compruebe si un elemento está en la lista:
a=int(input("Ingrese un numero: "))
if a in lista:
    print("El numero de encuentra en la lista")
else:
    print("El numero no se encuentra en la lista")