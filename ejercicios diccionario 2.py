print("Fundamentos de Python")
print("Nombre: Jennifer Illescas")
print("Fecha: 10 de abril del 2023 \n")
#CURSO DE FUNDAMENTOS DE PYTHON 
print("FUNDAMENTOS DE PYTHON")
#EJERCICIOS DE DICCIONARIOS
print("EJERCICIOS DE DICCIONARIOS")
#1.Crea un diccionario vacío y agrega tres elementos de la siguiente forma: "clave": valor
print("\n1. Crea un diccionario vacío y agrega tres elementos de la siguiente forma: clave: valor")
alumnos={}
print("Diccionario vacío:",alumnos)
#2.Dado el siguiente diccionario:
print("\n2. Dado el siguiente diccionario")
personas = {"Juan": 28, "María": 20, "Pedro": 32, "Ana": 25}
print("Diccionario:",personas)
#a) Imprime la edad de Juan.
print("a) Imprime la edad de Juan")
print("Edad de Juan",personas["Juan"])
#b) Agrega un nuevo elemento al diccionario con la clave "Luis" y la edad 18.
print("b) Agrega un nuevo elemento al diccionario con la clave Luis y la edad 18.")
personas["Luis"]="18"
print("Diccionario con el nuevo elemento:",personas)
#c) Elimina el elemento con la clave "Pedro".
print("c) Elimina el elemento con la clave Pedro")
personas.pop("Pedro")
print("Diccionario sin el elemento:",personas)
#3.Dado el siguiente diccionario:
print("\n3. Dado el siguiente diccionario")
ventas = {"manzanas": 10, "naranjas": 5, "peras": 8}
print("Diccionario:",ventas)
#a) Imprime la cantidad de manzanas vendidas.
print("a) Imprime la cantidad de manzanas vendidas")
print("Manzanas vendidad:",ventas["manzanas"])
#b) Agrega 3 elementos más al diccionario: "limones": 12, "sandías": 3, "melones": 5.
print("b) Agrega 3 elementos más al diccionario: limones: 12, sandías: 3, melones: 5")
ventas["limones"]="12"
ventas["sandias"]="3"
ventas["melones"]="5"
print("Elementos agregados:",ventas)
#c) Imprime las claves del diccionario.
print("c) Imprime las claves del diccionario")
print("Claves del diccionario:",ventas.keys())
#4. Dado el siguiente diccionario:
print("\n4. Dado el siguiente diccionario")
alumnos = {"Juan": {"edad": 22, "promedio": 8.5}, "María": {"edad": 20, "promedio": 9.0}, "Pedro": {"edad": 25, "promedio": 7.5}}
print("Diccionario:",alumnos)
#a) Imprime la edad de Juan.
print("a) Imprime la edad de Juan")
print("Edad de Juan:",alumnos["Juan"]["edad"])
#b) Imprime el promedio de María.
print("b) Imprime el promedio de María")
print("Promedio de María:",alumnos["María"]["promedio"])
#c) Agrega un nuevo elemento al diccionario con la clave "Ana" y los valores "edad": 19 y "promedio": 8.0.
print("c) Agrega un nuevo elemento al diccionario con la clave Ana y los valores edad: 19 y promedio: 8.0.")
alumnos["Ana"]={"edad":19,"promedio":8.0}
print("Nueva lista:",alumnos)
#5. Dado el siguiente diccionario:
print("\n5. 5. Dado el siguiente diccionario")
empleados = {"Juan": {"departamento": "Ventas", "sueldo": 1500}, "María": {"departamento": "Contabilidad", "sueldo": 1800}, "Pedro": {"departamento": "Ventas", "sueldo": 1700}, "Ana": {"departamento": "Recursos Humanos", "sueldo": 1900}}
print("Diccionario:",empleados)
#a) Imprime el sueldo de Pedro.
print("a) Imprime el sueldo de Pedro")
print("Sueldo de Pedro:",empleados["Pedro"]["sueldo"])
#b) Cambia el sueldo de Ana a 2000.
print("b) Cambia el sueldo de Ana a 2000")
empleados["Ana"]["sueldo"]=2000
print("Nuevo sueldo de Ana:",empleados)
#c) Crea un nuevo diccionario con los empleados del departamento de Ventas.
print("c) Crea un nuevo diccionario con los empleados del departamento de Ventas")
empelados_ventas={"Juan"}
print("Empleados del departamento de ventas:",empelados_ventas)
#6.Dado el siguiente diccionario:
print("\n6. 6.Dado el siguiente diccionario")
cursos = {"Pedro": ["Matemáticas", "Biología", "Historia"],
        "María": ["Física", "Química", "Literatura"]}
print("Cursos:",cursos)
#a) Imprime las materias en las que está inscrito Pedro.
print("a) Imprime las materias en las que está inscrito Pedro")
print("Materias en las que esta inscrito pedro:",cursos["Pedro"])
#b) Agrega una materia más a la lista de materias de María: "Programación".
print("b) Agrega una materia más a la lista de materias de María: Programación")
cursos["Maria"]="Programacion"
print("Materia agregada:",cursos)
#c) Crea un nuevo diccionario con los estudiantes que están inscritos en la materia de Biología.
print("c) Crea un nuevo diccionario con los estudiantes que están inscritos en la materia de Biología.")
cursos={"Pedro"}
print("Estudiantes inscritos en la materia de Biología:",cursos)
#7. Dado el siguiente diccionario:
print("\n7. Dado el siguiente diccionario")
productos = {'manzanas': 2.99, 'naranjas': 1.99, 'peras': 3.99, 'uvas': 4.99, 'kiwis': 0.99, 'duraznos': 2.49}
stock = {'manzanas': 100, 'naranjas': 50, 'peras': 25, 'uvas': 75, 'kiwis': 200, 'duraznos': 60}
print("Productos:",productos)
print("Stock:",stock)
#a) Imprime el precio de las naranjas.
print("a) Imprime el precio de las naranja")
print("Precio de las naranjas:",productos["naranjas"])
#b) Cambia el stock de peras a 12.
print("b) Cambia el stock de peras a 12")
stock["peras"]="12"
print("Cambio:",stock)
#c) Crea una función que calcule el valor total de los productos en el diccionario.
print("c) Crea una función que calcule el valor total de los productos en el diccionario")
total=sum(productos.values())
print("Total de productos:",total)
