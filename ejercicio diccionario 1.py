print("Fundamentos de Python")
print("Nombre: Jennifer Illescas")
print("Fecha: 10 de abril del 2023 \n")
#Crear un diccionario vacío:
print("\n1. Crear un diccionario vacío")
alumnos={}
alumnos=dict()
print("Diccionario vacio:",alumnos)
#Agregar elementos a un diccionario:
print("\n2. Agregar elementos a un diccionario")
alumnos={
        "0106663792":"Juan Bravo",
         "1105050775":"Veronica Chimbo",
         "0107050270":"Antoni Mejia",
         "1501095408":"Pizango Jhordan",
         "0105410211":"Christian Preciado",
         "0106605017":"Astudullo Carlos",
         "0106767007":"Bruce",
         "0105737365":"Stallin Barbecho",
         "0954337572":"Torres Melanie",
         "0106637150":"Paredes Jennifer",
         "0150564078":"Danny Alex",
         "0105041982":"Adrian Piña",
         "0106399041":"Jacqueline Tenesaca",
         "0150474021":"David Ñauta",
          "0107270282":"Edwin Arroyo",
         "0107416927":"Jose Muñoz",
        "0150578094":"Nayeli Gallegos"
        }
alumnos["010735988"]="Ariel Villa"
print("Diccionario de alumnos:",alumnos)
#Acceder a un valor en un diccionario:
print("\n3. Acceder a un valor en un diccionario:")
print("Valor del diccionario:",alumnos["0954337572"])
#Verificar si una llave existe en un diccionario:
print("\n4. Verificar si una llave existe en un diccionario")
print("Verificación;",alumnos.get("0954337572","no se encuentra en el diccionario"))
#Eliminar un elemento de un diccionario:
print("\n5. Eliminar un elemento de un diccionario")
print("Elemento eliminado:",alumnos.pop("0954337572"))
print("0954337572")
print(alumnos.get("0954337572","no se encuentra en el diccionario"))
#Imprimir las llaves de un diccionario:
print("\n6. Imprimir las llaves de un diccionario")
print("Llaves del diccionario:",alumnos.keys())
#Imprimir los valores de un diccionario:
print("\n7. Imprimir los valores de un diccionario")
print("Valores del diccionario:",alumnos.values())
#Imprimir las llaves y valores de un diccionario:
print("\n8. Imprimir las llaves y valores de un diccionario")
print("Llaves y valores del diccionario:",alumnos.items())