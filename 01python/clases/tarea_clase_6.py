#1 
'''
ingreso = int(input('Ingrese un valor: '))
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(ingreso))

'''
# 2
'''
import math 

ingreso = int(input('Ingrese un valor: '))

def calcular_area_circulo(radio):
    return math.pi * radio * radio ** 2

print(calcular_area_circulo(ingreso))

'''

#3
'''
import statistics

def estadisticas_de_muestra(muestra):
    media = statistics.mean(muestra)
    varianza = statistics.variance(muestra)
    desviacion_tipica = statistics.stdev(muestra)
    return {'media': media, 'varianza': varianza, 'desviacion_tipica': desviacion_tipica}

muestra = [12, 23, 34, 45, 56]
print(estadisticas_de_muestra(muestra))
'''

#4
'''
def valores_pares(valores):
    return [valor for valor in valores if valor % 2 == 0]
valores = [1, 3, 4, 8, 9, 10, 11, 13, 15, 18, 22, 27, 32, 35]
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

zona_a = [cabania_uno, cabania_2, depto_costa_1, depto_costa_2] 

def buscar_inmuebles_por_presupuesto(lista_inmuebles, presupuesto):
    inmuebles_en_presupuesto = []
    for inmueble in lista_inmuebles:
        if inmueble["zona"] == "A":
            precio = (inmueble["metros"] * 1000 + inmueble["habitaciones"] * 5000 + inmueble["garaje"] * 15000) * (1 - (2021 - inmueble["año"]) / 100)
        else:
            precio = (inmueble["metros"] * 1000 + inmueble["habitaciones"] * 5000 + inmueble["garaje"] * 15000) * (1 - (2021 - inmueble["año"]) / 100) * 1.5
        if precio <= presupuesto:
            inmueble["precio"] = precio
            inmuebles_en_presupuesto.append(inmueble)
    return inmuebles_en_presupuesto






