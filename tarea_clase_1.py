#1. Calcule la superficie de un triángulo, dada la medida de su base y su altura
lado_a = 10
lado_b = 7
print (lado_a +lado_b / 2)

# Calcule las raíces 𝑥1 y 𝑥2 de una expresión cuadrática: 2𝑥2 − 3𝑥 + 4 = 0 Utilice bascara
import math
termino_cuadratico_a = 1
termino_lineal_b = -3
termino_independiente_c = 2

# Calculamos delta
delta = termino_lineal_b * termino_lineal_b - 4 * termino_cuadratico_a * termino_independiente_c

if delta < 0:
    print("Tiene raices reales")
elif delta == 0:
    raiz = (-1 * termino_lineal_b + math.sqrt(delta))/ (2 * termino_cuadratico_a)
    print("Posee una sola raiz", raiz)
elif delta > 0: 
    raiz1 = (-1 * termino_lineal_b + math.sqrt(delta))/ (2 * termino_cuadratico_a)
    raiz2 = (-1 * termino_lineal_b - math.sqrt(delta))/ (2 * termino_cuadratico_a)
    print("Las raices de la ecuacion son:", raiz1,"y", raiz2)

#. Verifique que las raíces encontradas en el punto anterior resuelven realmente la ecuación dada.
print(termino_cuadratico_a * (raiz1 * raiz1) - (3 * raiz1) +  2 == 0)
print(termino_cuadratico_a * (raiz2 * raiz2) - (3 * raiz2) +  2 == 0)




# Cree 3 variables de los siguientes tipos: entero, flotante, booleano e imprima para las 3: a. Su tipo b. Su Identificación en memoria. c. Su valor
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

#



