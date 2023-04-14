print("Fundamentos de Python")
print("Nombre: Jennifer Illescas")
print("Fecha: 10 de abril del 2023 \n")
#CURSO DE FUNDAMENTOS DE PYTHON 
#EJERCICIOS DE TUPLAS
print("CURSO DE FUNDAMENTOS DE PYTHON")
print("EJERCICIOS DE TUPLAS\n")
#Crear una tupla vacía:
print("\n1. Crear una tupla vacía.")
tupla=()
print("Tupla vacia:",tupla)
#Crear una tupla con algunos elementos:
print("\n2. Crear una tupla con algunos elementos.")
tupla_frutas=("manzana","pera","durazno","uva","fresa","guineo")
print("Tupla creada:",tupla_frutas)
#Acceder a un elemento de la tupla:
print("\n3. Acceder a un elemento de la tupla.")
tupla_frutas=("manzana","pera","durazno","uva","fresa","guineo")
print(tupla_frutas)
print("Elemento 2 de la tupla:",tupla_frutas[-2])
#Intentar modificar un elemento de la tupla (esto producirá un error ya que las tuplas son inmutables):
print("\n4. Intentar modificar un elemento de la tupla (esto producirá un error ya que las tuplas son inmutables)")
print("No se puede, ya que las tuplas son inmutables")
#Concatenar dos tuplas: 
print("\n5. Concatenar dos tuplas")
frutas=("manzana","fresa","naranja")
print("Frutas:",frutas)
colores=("rojo","rosado","anaranjado")
print("Colores:",colores)
union=frutas+colores
print("Tupla concatenada:",union)
#Obtener la longitud de una tupla:
print("\n6. Obtener la longitud de una tupla")
numeros=(1,2,3,4,5,6,7,8,9,10)
print("Numeros:",numeros)
print("Longitug de la tupla:",len(numeros))
#Convertir una tupla en una lista:
print("\n7. Convertir una tupla en una lista")
tupla=(10,20,30,40,50)
print("Tupla:",tupla)
print("Tupla convertida en lista:",list(tupla))
#Convertir una lista en una tupla:
print("\n8. Convertir una lista en una tupla")
lista=[1,2,3,4,5]
print("Lista:",lista)
print("Lista convertida en tupla:",tuple(lista))