"""La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. 
Los ingredientes para cada tipo de pizza aparecen a continuación.
· Ingredientes vegetarianos: Pimiento y tofu.
· Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en
función de su respuesta le muestre un menú con los ingredientes disponibles para que
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


# 2

"""
mensaje = input("Ingrese un año: ")
year = int(mensaje)

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
def verificar(edad, peso, pulso, tension_baja, tension_alta, plaquetas):
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

print(verificar(34, 81, 70, 130, 120, 150000))

"""

#6 
