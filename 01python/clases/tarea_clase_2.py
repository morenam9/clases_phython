"""La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. 
Los ingredientes para cada tipo de pizza aparecen a continuación.
· Ingredientes vegetarianos: Pimiento y tofu.
· Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en
función de su respuesta le muestre un menu con los ingredientes disponibles para que
elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están
en todas las pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana
o no y todos los ingredientes que lleva."""

"""
saludo = print("Bienvenido a la pizzeria Bella Napoli")
opcion = input("¿Quieres una pizza vegetariana? - Y/N ")

ingredientes = ["Tomate", "Mozzarella"]


if opcion == "Y":
    ingredientes.append("Pimiento")
    ingredientes.append("Tofu")
    es_vegetariana = True
elif opcion == "N":
    ingredientes.append("Peperoni")
    ingredientes.append("Jamón")
    ingredientes.append("Salmón")
    es_vegetariana = False
else:
    print("Opción no válida")
    exit()

print("Has elegido una pizza " + ("vegetariana" if es_vegetariana else "no vegetariana"))
print("Los ingredientes de tu pizza son: " + ", ".join(ingredientes))

"""

"""
mensaje = input("Ingrese un año: ")
if (mensaje.isdigit()):
    year = int(mensaje)
else:
    print("Dato invalido")
    exit()


if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
  print(year, "es bisiesto")
else:
  print(year, "no es bisiesto")
"""


# 3
"""
jugador1 = input("Elija una opcion 'piedra', 'papel', o 'tijera'")
jugador2 = input("Elija una opcion 'piedra', 'papel', o 'tijera'")

def piedra_papel_tijera(jugador1, jugador2):
  if jugador1 == jugador2:
    return "EMPATE"
  elif jugador1 == "piedra":
    if jugador2 == "tijera":
      return "Jugador 1 gana!"
    else:
      return "Jugador 2 gana!"
  elif jugador1 == "papel":
    if jugador2 == "piedra":
      return "Jugador 1 gana!"
    else:
      return "Jugador 2 gana!"
  elif jugador1 == "tijera":
    if jugador2 == "papel":
      return "Jugador 1 gana!"
    else:
      return "Jugador 2 gana!"
  else:
    return "Opcion inválida. Por favor escribe 'piedra', 'papel', o 'tijera'"
print(piedra_papel_tijera(jugador1, jugador2))
"""

# 4
"""
uno = input("Ingrese un numero: ")
dos = input("Ingrese otro numero: ")
tres = input("Ingrese un ultimo numero: ")
num1 = int(uno)
num2 = int(dos)
num3 = int(tres)

def calcular_max_min_avg(num1, num2, num3):
  max_num = max(num1, num2, num3)
  min_num = min(num1, num2, num3)
  avg = (num1 + num2 + num3) / 3
  return f"El maximo es: {max_num}, el minimo es : {min_num}, y el promedio es: {avg:.2f}"

print(calcular_max_min_avg(num1, num2, num3))
""" 
# 5 
"""
def verificar_aptitud(edad, peso, pulso, tension_baja, tension_alta, plaquetas):
  if edad >= 18 and edad <= 65:
    if peso >= 50:
      if pulso >= 50 and pulso <= 110:
        if tension_baja >= 50 and tension_alta <= 180:
          if plaquetas >= 150000:
            return "Apto para donar sangre."
          else:
            return "No apto para donar. El recuento de plaquetas es bajo."
        else:
          return "No apto para donar. La presión arterial está fuera de rango."
      else:
        return "No apto para donar. El pulso esta fuera de rango."
    else:
      return "No apto para donar. El peso es demasiado bajo."
  else:
    return "No apto para donar. La edad está fuera de rango."

print(verificar_aptitud(34, 81, 70, 130, 200, 150000))

"""

#6 
"""
Escriba un programa que encuentre todos los multiplos de 5 menores que un valor dado:
Ejemplo
• Entrada: 36
• Salida: 5 10 15 20 25 30 3



while (True):
    calcular_nro_primo = int(input("Ingrese un numero : "))
    avg = range(1,calcular_nro_primo)

    for i in avg :
        if i % 5 == 0:
            print(f"{i}" , end=" ")


"""
"""
Escriba un programa que encuentre la mínima secuencia de multiplos de 3 (distintos) 
cuya suma sea igual o inferior a un valor dado.
Ejemplo
• Entrada: 45
• Salida: 0, 3, 6, 9, 12, 15

#7
entero = int(input("Ingrese un numero entero : "))
operacion = range(1, entero)
i = 0
suma = 0
while suma < entero:
    if i % 3 == 0:
        print(f"{i}" , end=" ")
    i += 1
    suma += i
    
"""

#9
"""
Escriba un programa en Python que realice las siguientes 9 multiplicaciones y muestre el resultado de cada producto
1*1
11*1
111*111
1111*1111
"""
"""
a = 1*1
b = 11*1
c = 111*111
d = 1111*1111
print(a, b, c, d)

"""

#10
"""
Escriba un programa en Python que acepte dos cadenas de texto y compute el producto  cartesiano letra a letra entre ellas.
Ejemplo
• Entrada: str1=abc; str2=123
• Salida: a1 a2 a3 b1 b2 b3 c1 c2 c3
"""
"""
def producto_cartesiano(str1, str2):
    for c1 in str1:
        for c2 in str2:
            print(c1 + c2)

producto_cartesiano("abc", "123")
"""

#11
"""
Escriba un programa en que acepte dos valores enteros (x e y) que representarán un
punto (objetivo) en el plano. El programa simulará el movimiento de un «caballo» de
ajedrez moviéndose de forma alterna: primero avanzando 2 posiciones en x más 1
posición en y. En el siguiente movimiento que se moverá 1 posición en x más 2
posiciones en y. El programa deberá ir mostrando los puntos por los que va pasando el
«caballo» hasta llegar al punto objetivo. Extra: Agregue las otras posibilidades de
movimiento que tiene el caballo para encontrar otras posiciones del tablero a ingresar
manualmente, dando la posibilidad de modificar además el punto de partida del caballo.
Ejemplo (problema básico)

• Entrada: objetivo_x=7; objetivo_y=8;
• Salida: (0, 0) (1, 2) (3, 3) (4, 5) (6, 6) (7, 8);
"""
"""
objetivo_x = 8
objetivo_y = 7

caballo_x = 1
caballo_y = 1

STR_MOVS = '(+2,+1);(+2,-1);(-2,+1);(-2,-1);(+1,+2);(-1,+2);(+1,-2);(-1,-2)'

NUM_MOVS = STR_MOVS.count('(')

MOV_LEN = STR_MOVS.index(')') + 2

CASILLAS_X_MAX = 8
CASILLAS_Y_MAX = 8

casillas_pisadas = ''

objetivo_no_alcanzado = True

while objetivo_no_alcanzado:

    #Valor para desbordar un cálculo y elegir movimientos distintos cada vez
    for num_desborde in range(1, 10):

        #Extraico y pruebo movimientos
        for mov in range(NUM_MOVS): # 0 ... 7

            #Indice de un movimiento, uso un desborde para que no siempre pruebe los movimientos en el mismo orden
            idx = ((mov ** num_desborde) % NUM_MOVS) * MOV_LEN
            
            #String de cada movimiento ej: (+2,-1)
            str_mov = STR_MOVS[idx: idx + MOV_LEN - 1]
            
            #Movimiento x, ejemplo: -2
            movx = int(str_mov[2]) * (1 if str_mov[1] == '+' else -1)
            
            #Movimiento y, ejemplo: 2
            movy = int(str_mov[5]) * (1 if str_mov[4] == '+' else -1)

            #Nueva coordenada tentativas del caballo
            new_caballo_x = caballo_x + movx
            new_caballo_y = caballo_y + movy

            # Seguir probando otro movimiento si las coordendas dan fuera del tablero
            if new_caballo_x <= 0 or new_caballo_y <= 0:
                continue

            elif new_caballo_x > CASILLAS_X_MAX or new_caballo_y > CASILLAS_Y_MAX:
                continue
            
            #Agregar la coordenada al historial
            str_casilla = f'({new_caballo_x},{new_caballo_y})'
            if str_casilla in casillas_pisadas:
                #Dejo que repita movimientos hechos antes
                pass
                #continue
            else:
                casillas_pisadas += str_casilla
                print(str_casilla)

            #Verificar si llegó al objetivo
            if new_caballo_x == objetivo_x and new_caballo_y == objetivo_y:
                print('Objetivo alcanzado!')
                objetivo_no_alcanzado = False
                break # del for secundario
            else:
                #Actualizar posición del caballo
                caballo_x = new_caballo_x
                caballo_y = new_caballo_y
        
        if objetivo_no_alcanzado == False:
            break # del for principal
        
"""
#12 
"""
Escriba un programa que calcule la distancia hamming entre dos cadenas de texto de la 
misma longitud
Ejemplo
• Entrada: 0001010011101 y 0000110010001
• Salida: 4
"""

#13
"""
Escriba un programa que calcule el máximo comun divisor entre dos numeros enteros. 
No utilice ningun algoritmo existente. Hágalo probando divisores.
Ejemplo
• Entrada: a=12; b=44
• Salida: 4
"""

#14 
"""
. Escriba un programa que calcule el valor de x para el que la función 𝑓(𝑥) = 𝑥
2 − 6𝑥 + 3
obtiene su menor resultado. Centre la busqueda en el rango [−9] a [9] sólo con valores enteros. El resultado es: 𝑥 = 3 y 𝑓(3) = −6
"""

#15
"""
Escriba un programa que muestre (por filas) la Tabla ASCII, empezando con el código 33  y terminando con el 127, Tal como se muestra en la siguiente imagen.

"""
"""
for i in range(33, 128):
    print(f"{i:03d} {chr(i):}", end = "")
"""


#16

"""Escriba un programa que permita al usuario adivinar un numero. Indicar si el numero 
buscado es menor o mayor que el que se está preguntando y mostrar igualmente el 
numero de intentos hasta encontrar el numero objetivo"""

import random

def adivinar_numero():
    rango = random.randint(1, 100)
    numero_de_intento = 0

    while True:
        intento = int(input("Adivina el numero entre 1 y 100: "))
        numero_de_intento += 1

        if intento == rango:
            print(f"¡Felicidades! Adivinaste el numero en {numero_de_intento} intentos.")
            break
        elif intento < rango:
            print("El numero que buscas es mayor.")
        else:
            print("El numero que buscas es menor.")

adivinar_numero()


