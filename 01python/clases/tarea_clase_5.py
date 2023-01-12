"""

Ejercicios con Estructuras de datos:

#1.

palabra = input("Ingrese una palabra para determinar si es un isograma: ")

for i in range(len(palabra)-1):
    if palabra[i] == palabra[i + 1]:
        print("Las letras se repiten, no es un isograma.")
    else: 
        print(palabra + " es un isograma")
    break
  
"""

"""
#2. Transformar esta cadena de texto que representa una fecha 3/30/20 en otra cadena de texto con el siguiente formato 31-12-2020.
from datetime import datetime
fecha_truncada = "Mar 30 2020"
fecha_completa =  datetime.strptime(fecha_truncada, '%b %d %Y')
print(f"La fecha en el formato solicitado es : {fecha_completa}")
print(type(fecha_completa))
"""
"""




Escribir un programa que guarde en un diccionario los precios de las frutas 
de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por 
pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el 
diccionario debe mostrar un mensaje informando de ello.

Fruta       Precio
Banana      1.35
Manzana     0.80
Pera        0.85
Naranja     0.7

"""

verduleria = {'Banana': 1.35, 'Manzana': 0.80, 'Pera': 0.85, 'Naranja': 0.7}
seleccion = input("Ingrese la fruta que desea comprar: \n 0 -> Banana, 1 -> Manzana, 2 -> Pera, 3 -> Naranja ")
eleccion_kilos = input("Cuantos kilos desea pedir? ")
kilos = int(eleccion_kilos)
if seleccion == verduleria['Banana'] :
    precioBanana = 1.35 * kilos
    print(f"Su seleccion es: {kilos} KGS de bananas el total es {precioBanana}")




"""4.Escriba un programa que tenga inicialmente un diccionario con los siguientes datos de 
dos personas:
Nombre
Apellido
Edad
Email

Persona 1: Emilia, Cabrera de 23 años de edad, email ecabrera@curso.com
Persona 2: Gustavo Andrés, Peralta de 26 años de edad, email gperalta@curso.com

El programa debe permitir la carga de una persona más y agregarla al diccionario.
Ingresados los datos de esta persona nueva deben imprimirse los datos de las 3 personas 
cargadas de manera tabular.

"""

persona1 = {'Nombre': "Emilia", 'Apellido': "Cabrera", 'Edad': 23, 'Email': "ecabrera@curso.com"}
persona2 = {'Nombre': "Gustavo Andrés", 'Apellido': "Peralta", 'Edad': 26, 'Email': "gperalta@curso.com"}
ingresos = input("Si desea ingresar un registro de datos nuevo presione Y ") 
if ingresos == "Y" :
    nombre = input("Ingrese su nombre completo: ")
    apellido = input("Ingrese su apellido: ")
    edad = input("Ingrese su edad: ")
    email = input("Ingrese su email: ")

personax = {}

