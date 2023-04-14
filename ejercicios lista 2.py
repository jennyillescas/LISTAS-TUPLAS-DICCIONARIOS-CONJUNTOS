print("Fundamentos de Python")
print("Nombre: Jennifer Illescas")
print("Fecha: 10 de abril del 2023 \n")

#CURSO DE FUNDAMENTOS DE PYTHON 
#EJERCICIOS DE LISTAS A RESOLVER
print("CURSOS DE FUNDAMENTOS DE PYTHON")
print("EJERCICIOS DE LISTAS A RESOLVER\n")
#Crea una lista vacía llamada numeros e introduce los números del 1 al 5. Luego, muestra la lista por pantalla.
print("1. Crea una lista vacía llamada numeros e introduce los números del 1 al 5. Luego, muestra la lista por pantalla.")
numeros=[]
for e in range(1,6):
    numeros.append(e)
print("Lista creada del 1 al 5:",numeros)
#Crea una lista con los nombres de tus amigos y muestra por pantalla el primer elemento de la lista.
print("\n2. Crea una lista con los nombres de tus amigos y muestra por pantalla el primer elemento de la lista.")
amigos=["Melanie","Evelyn","Estefania","Nayeli","Alex","Danny"]
print("Lista de amigos:",amigos)
print("Primer elemento de la lista:",amigos[0])
#Crea una lista con los números del 1 al 10 y muestra por pantalla los números pares.
print("\n3. Crea una lista con los números del 1 al 10 y muestra por pantalla los números pares.")
numeros=[1,2,3,4,5,6,7,8,9,10]
for e in numeros:
    if e%2==0:
        print("Numeros pares:",e)
#Crea una lista con los nombres de tus amigos y muestra por pantalla el último elemento de la lista.
print("\n4. Crea una lista con los nombres de tus amigos y muestra por pantalla el último elemento de la lista.")
amigos=["Melanie","Evelyn","Estefania","Danny","Nayeli","Alex"]
print("Lista de amigos:",amigos)
print("Ultimo elemento de la lista:",amigos[-1])
#Crea una lista con los números del 1 al 10 y muestra por pantalla el último elemento de la lista.
print("\n5. Crea una lista con los números del 1 al 10 y muestra por pantalla el último elemento de la lista.")
numeros=[1,2,3,4,5,6,7,8,9,10]
print("Lista de numeros del 1 al 10:",numeros)
print("Ultimo elemento de la lista:",numeros[-1])
#Crea una lista con los números del 1 al 10 y muestra por pantalla los números impares.
print("\n6. Crea una lista con los números del 1 al 10 y muestra por pantalla los números impares.")
numeros=[1,2,3,4,5,6,7,8,9,10]
for e in numeros:
    if e%2==1:
        print("Numeros impares:",e)
#Crea una lista con los nombres de tus amigos y añade un nuevo amigo a la lista. Luego, muestra la lista por pantalla.
print("\n7. Crea una lista con los nombres de tus amigos y añade un nuevo amigo a la lista. Luego, muestra la lista por pantalla.")
amigos=["Melanie","Evelyn","Estefania","Danny","Nayeli","Alex"]
print("Lista de amigos actual:",amigos)
amigos.append("Darwin")
print("Lista nueva, con el nuevo amigo agregado:",amigos)
#Crea una lista con los números del 1 al 10 y muestra por pantalla el primer y el último elemento de la lista.
print("\n8. Crea una lista con los números del 1 al 10 y muestra por pantalla el primer y el último elemento de la lista.")
numeros=[1,2,3,4,5,6,7,8,9,10]
print("Lista de numeros del 1 al 10:",numeros)
print("Primer elemento de la lista:",numeros[0])
print("Ultimo elemento de la lista:",numeros[-1])
#Crea una lista con los nombres de tus amigos y muestra por pantalla el número de elementos de la lista.
print("\n9. Crea una lista con los nombres de tus amigos y muestra por pantalla el número de elementos de la lista.")
amigos=["Melanie","Evelyn","Estefania","Danny","Nayeli","Alex"]
print("Lista de amigos actual:",amigos)
print("Numero de elementos de la lista:",len(amigos))
#Crea una lista con los números del 1 al 10 y muestra por pantalla la suma de todos los elementos de la lista.
print("\n10. Crea una lista con los números del 1 al 10 y muestra por pantalla la suma de todos los elementos de la lista.")
lista=[1,2,3,4,5,6,7,8,9,10]
suma=0
for e in lista:
    suma=suma+e
print(suma)
print("La suma total es:",sum(lista))