# # #1. Calcule la superficie de un triángulo, dada la medida de su base y su altura
lado_a = 10
lado_b = 7
print (lado_a +lado_b / 2)

# # # Calcule las raíces 𝑥1 y 𝑥2 de una expresión cuadrática: 2𝑥2 − 3𝑥 + 4 = 0 Utilice bascara
import math
a = 1
b = -3
c = 2

# # # Calculamos delta

delta = b * b - 4 * a * c

if delta < 0:
    print("Tiene raices reales")
elif delta == 0:
    raiz = (-1 * b + math.sqrt(delta))/ (2 * a)
    print("Posee una sola raiz", raiz)
elif delta > 0:
    raiz1 = (-1 * b + math.sqrt(delta))/ (2 * a)
    raiz2 = (-1 * b - math.sqrt(delta))/ (2 * a)
    print("Las raices de la ecuacion son:", raiz1,"y", raiz2)

# # #. Verifique que las raíces encontradas en el punto anterior resuelven realmente la ecuación dada.

print(a * (raiz1 * raiz1) - (3 * raiz1) +  2 == 0)
print(a * (raiz2 * raiz2) - (3 * raiz2) +  2 == 0)


# # # Cree 3 variables de los siguientes tipos: entero, flotante, booleano e imprima para las 3: a. Su tipo b. Su Identificación en memoria. c. Su valor

entero = 15
type(entero)
id(entero)
print(entero)

flotante = 3.5
type(flotante)
id(flotante)
print(flotante)

booleano = False
type(booleano)
id(booleano)
print(booleano)


# # Partiendo de las variables dadas, cree otras variables derivadas de éstas y del tipo que se pide en la tabla siguiente:
# """
# || Valor original ||  Valor a convertir ||

#     4.2                     INT
#     4.2                     BOOL
#     true                    INT
#     true                    FLOAT
#     6                       FLOAT
#     6                       BOOL

# """

valor1 = 4.2
convertido1 = int(valor1)
print(int(valor1), type(convertido1))

valor2 = 4.2
convertido2 = bool(valor2)
print(bool(valor2), type(convertido2))

valor3 = True
convertido3 = int(valor3)
print(int(valor3), type(convertido3))

valor4 = True
convertido4 = float(valor4)
print(float(valor4), type(convertido4))

valor5 = 6
convertido5 = float(valor5)
print(float(valor5), type(convertido5))

valor6 = 6
convertido6 = bool(valor6)
print(bool(valor2), type(convertido6))

# #  Leer dos números por teclado, realizar las operaciones básicas entre ellos:

valor_a = int(input("Ingrese el primer valor a operar: "))
valor_b = int(input("Ingrese el segundo valor a operar: "))

suma = valor_a + valor_b
print(suma)

resta = valor_a - valor_b
print(resta)

multiplicacion = valor_a * valor_b
print(multiplicacion)

division = valor_a / valor_b
print(division)

division_entera = valor_a // valor_b
print(division_entera)

modulo = valor_a % valor_b
print(modulo)

potencia = valor_a ** valor_b
print(potencia)


# """
# Ejercicios con strings:

# 1. Escriba un programa en Python que acepte el nombre y los apellidos de una persona y los
# imprima en orden inverso separados por una coma. Utilice f-strings para implementarlo.



# """
nombre = input("Por favor ingrese un nombre : ")
apellido = input("Por favor ingrese un apellido : ")

print(f"El nombre ingresado es :  {apellido}, {nombre} ")


# Escriba un programa en Python que acepte una ruta remota de recurso samba, y lo separe
# en nombre(IP) del equipo y ruta
#
#  Entrada: //1.1.1.1/eoi/python
#
#  Salida: host=1.1.1.1; path=/eoi/python

url = '//1.1.1.1/eoi/python'

url = url[2:]
simbolo = url.index('/')
host = url[:simbolo]
ruta = url[simbolo:]
print(f'host={host}  path={ruta}')

# Escriba un programa en Python que acepte un «string» con los 8 dígitos de un NIF, y calcule su dígito de control.


codigo_nif = 'TRWAGMYFPDXBNUZSQVHLCKE'

dni = '12345678'
digitos = codigo_nif[int(dni) % 23]
salida = dni + digitos

print(salida)

# Escriba un programa en Python que acepte un entero n y compute el valor de n + nn + nnn

valor_inicial = 5

valor_inicial = str(valor_inicial)
resultado = int(valor_inicial) + int(valor_inicial * 2) + int(valor_inicial * 3)
print(resultado)


# Escriba un programa en Python que acepte una palabra en castellano y calcule una métrica que sea el número total de caracteres de la palabra multiplicado por el número total de vocales que contiene la palabra

palabra = 'ordenador'

palabra_length = len(palabra)

num_a = palabra.count('a')
num_e = palabra.count('e')
num_i = palabra.count('i')
num_o = palabra.count('o')
num_u = palabra.count('u')

metrica = palabra_length * (num_a + num_e + num_i + num_o + num_u)
print(metrica)

# Escriba un programa en Python que transforme un título HTML <hx>...</hx> en su correspondiente versión de Markdown

HTAG_SIZE = 3
MD_HEADING_SYMBOL = '#'

html = '<h3>Cadenas de texto</h3>'

start_tag_index1 = html.find('<h')
start_tag_index2 = start_tag_index1 + HTAG_SIZE

end_tag_index1 = html.find('</h')
end_tag_index2 = end_tag_index1 + HTAG_SIZE + 1

heading_level = html[start_tag_index2 - 1]
heading_title = html[start_tag_index2 + 1 : end_tag_index1]

heading_rep = '#' * int(heading_level)

markdown = f'{heading_rep} {heading_title}'
print(markdown)







