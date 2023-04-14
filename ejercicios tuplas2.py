print("Fundamentos de Python")
print("Nombre: Jennifer Illescas")
print("Fecha: 10 de abril del 2023 \n")
#CURSO DE FUNDAMENTOS DE PYTHON 
print("CURSO DE FUNDAMENTOS DE PYTHON")
#EJERCICIOS DE TUPLAS
print("EJERCICIOS DE TUPLAS")
#Crear una tupla de números enteros y calcular su suma y promedio.
print("\n1. Crear una tupla de números enteros y calcular su suma y promedio.")
numeros_enteros=(1,2,3,4,5,6,7,8,9,10)
print("Numeros:",numeros_enteros)
suma=0
for e in numeros_enteros:
    suma+=e
promedio=suma/len(numeros_enteros)
print("La suma es:",suma)
print("El promedio es:",promedio)
#Crear dos tuplas de la misma longitud y crear una nueva tupla que contenga la suma de los elementos correspondientes de ambas tuplas.
print("\n2. Crear dos tuplas de la misma longitud y crear una nueva tupla que contenga la suma de los elementos correspondientes de ambas tuplas.")
tupla1=(5,10,15,20)
print("Tupla 1:",tupla1)
tupla2=(5,10,15,20)
print("Tupla 2:",tupla2)
suma=tuple(map(sum, zip(tupla1, tupla2)))
print("La suma de los elementos es:",suma)
#Crear una tupla de nombres y ordenarla alfabéticamente.
print("\n3. Crear una tupla de nombres y ordenarla alfabéticamente.")
tupla_nombres=("Nayeli","Melanie","Darwin","Stalyn")
print("Nombres:",tupla_nombres)
orden=sorted(tupla_nombres)
print("Tupla de nomobres ordenada",orden)
#Crear una tupla de números y encontrar el valor mínimo y máximo.
print("\n4. Crear una tupla de números y encontrar el valor mínimo y máximo.")
tupla_numeros=(45,70,10,5,14,20,9)
print("Tupla de numeros:",tupla_numeros)
maximo=max(tupla_numeros)
minimo=min(tupla_numeros)
print("Valor maximo:",maximo)
print("Valor minimo:",minimo)
#Crear una tupla de números y convertirla en una lista.
print("\n5. Crear una tupla de números y convertirla en una lista.")
tupla=(1,2,3,4,5,6)
print("Tupla:",tupla)
print("Tupla convertida a lista:",list(tupla))
#Crear una tupla con los días de la semana y mostrar el tercer elemento.
print("\n6. Crear una tupla con los días de la semana y mostrar el tercer elemento.")
dias=("Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo")
print("Días de la semana:",dias)
print("Tercer elemento:",dias[2])
#Crear una tupla con números enteros y mostrar aquellos que son pares.
print("\n7. Crear una tupla con números enteros y mostrar aquellos que son pares.")
numeros=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
lista=[]
print("Numeros enteros:",numeros)
for e in numeros:
    if e%2==0:
        print("Numeros pares:",e)
#Crear una tupla con los meses del año y mostrar aquellos que tienen más de cinco letras.
print("\n8. Crear una tupla con los meses del año y mostrar aquellos que tienen más de cinco letras.")
meses=("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre")
for mes in meses:
    if len(mes) > 5:
       print("Tiene mas de 5 letras:",mes)
#Crear una tupla con las edades de varias personas y mostrar la cantidad de personas mayores de 18 años.
print("\n9. Crear una tupla con las edades de varias personas y mostrar la cantidad de personas mayores de 18 años.")
edades=(15,34,10,7,8,21,45,23)
for e in numeros:
    if e > 18 :
        print("Mayores de edad:",e)
#Crear una tupla de tuplas que contienen información de libros y mostrar el título del tercer libro.
print("\n10. Crear una tupla de tuplas que contienen información de libros y mostrar el título del tercer libro.")
libros=(("Borís Pasternak","Doctor Zhivago", ),
        ("Tennessee Williams", "Un Tranvía Llamado Deseo"),
        ("Homero","La Odisea"))
print("Libros:",libros)
posicion=libros.index(("Homero","La Odisea"))
print(posicion)
print("Titulo del tercer libro:", libros[posicion][1])