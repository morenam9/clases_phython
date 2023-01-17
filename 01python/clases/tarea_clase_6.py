#1 
'''
ingreso = int(input('Ingrese un valor: '))
def factorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * factorial(numero-1)
    
print(f'El factorial del numero ingresado es: {factorial(ingreso)}')
'''

# 2
'''
import math 

ingreso = int(input('Ingrese un valor: '))

def calcular_area_circulo(radio):
    return math.pi * radio * radio ** 2
print(f'El area de un circulo es : {calcular_area_circulo(ingreso)}')

'''

#3
'''
import statistics

def estadisticas_de_muestra(muestra):
    media = statistics.mean(muestra)
    varianza = statistics.variance(muestra)
    desviacion_tipica = statistics.stdev(muestra)
    return {'media': media, 'varianza': varianza, 'desviacion_tipica': desviacion_tipica}

muestra = (12, 23, 34, 45, 56)
print(estadisticas_de_muestra(muestra))
'''

#4
'''
def valores_pares(valores):
    return [valor for valor in valores if valor % 2 == 0]
valores = (1, 3, 4, 8, 9, 10, 11, 13, 15, 18, 22, 27, 32, 35)
pares = valores_pares(valores)
print(pares)
'''

#Utilizar el módulo collections de Python y la función split()
#para dividir la cadena en una lista de palabras.

import collections

def palabras_y_frecuencia(cadena):
    palabras = cadena.split()
    frecuencia = collections.defaultdict(int)
    for palabra in palabras:
        frecuencia[palabra] += 1
    return dict(frecuencia)

cadena = "Tres tristes tigres, tragaban trigo en un trigal, en tres tristes trastos, tragaban trigo tres tristes tigres."
diccionario = palabras_y_frecuencia(cadena)
print(diccionario)

def palabra_mas_repetida(diccionario):
    palabra_mas_repetida = ""
    frecuencia_maxima = 0
    for palabra, frecuencia in diccionario.items():
        if frecuencia > frecuencia_maxima:
            palabra_mas_repetida = palabra
            frecuencia_maxima = frecuencia
    return (palabra_mas_repetida, frecuencia_maxima)

tupla = palabra_mas_repetida(diccionario)
print(tupla)

#6 -- No entendi


#7 Terminar
'''
propiedades = [
        {'nombre': 'casa de campo','año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
        {'nombre': 'departamento con piscina','año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True,'zona': 'B'},
        {'nombre': 'casa en las sierras','año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje':False, 'zona': 'A'},
        {'nombre': 'departamento temporal','año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True,'zona': 'B'},
        {'nombre': 'duplex','año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje':False, 'zona': 'A'}]

def busqueda_inmueble(propiedades):
    presupuesto = float(input("Ingresa tu presupuesto: "))
    lista_propiedades = []
    for propiedad in propiedades:
        if propiedad["zona"] == "A":
            precio = (propiedad["metros"] * 1000 + propiedad["habitaciones"] * 5000 + propiedad["garaje"] * 15000) * (1 - propiedad["año"]/100)
        elif propiedad["zona"] == "B":
            precio = (propiedad["metros"] * 1000 + propiedad["habitaciones"] * 5000 + propiedad["garaje"] * 15000) * (1 - propiedad["año"]/100) * 1.5
        if precio <= presupuesto:
            propiedad["precio"] = precio
            lista_propiedades.append(propiedad)

        if len(lista_propiedades)>0:
            print("Estas son las opciones que se pueden permitir con tu presupuesto: ")
        for propiedad in lista_propiedades:
            print(propiedad["nombre"],"con un precio de", propiedad["precio"])
    else:
        print("Lo siento, no hay opciones disponibles con tu presupuesto.")

busqueda_inmueble(propiedades)
'''