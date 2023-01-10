"""

Ejercicios con Estructuras de datos:

1.Determine si una cadena de texto dada es un isograma, es decir, no se repite ninguna letra. Ejemplos de isogramas:
•lumberjacks
•background
•downstream
•six-year-old

"""

palabra = input("Ingrese una palabra para determinar si es un isograma: ")
for i in range(len(palabra)-1):
    if palabra[i] == palabra[i + 1]:
        print("la letra se repite")
    else :
        print('La palabra ', {palabra} , 'no se repite')

"""
2. Dada una cadena de texto que representa una fecha (mes/día/año truncado): ‘3/30/20’ 
transfórmela en otra cadena de texto con el siguiente formato: ‘31-12-2020’ (día-mes-año completo)
"""

"""3.Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, 
pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de 
ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un 
mensaje informando de ello.

Fruta       Precio
Banana      1.35
Manzana     0.80
Pera        0.85
Naranja     0.7

"""

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

