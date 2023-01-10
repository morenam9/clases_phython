'''
6.	Escriba un programa que encuentre todos los múltiplos de 5 menores que un valor dado:
Ejemplo
•	Entrada: 36
•	Salida: 5 10 15 20 25 30 35
'''

print("Programa para encontrar todos los numeros múltiplos de 5 menores al valor ingresado")

numero = None

ingresando_numero = True

while ingresando_numero:
    str_numero = input("Ingrese un número: ").strip()
    numero = int(str_numero) if str_numero.isdigit() else None
    if numero is not None:
        ingresando_numero = False
    else:
        print(f'Valor ingresado incorrecto. Reintente')

buscando_multiplos = True

multiplo_5 = 5

while buscando_multiplos:
    
    if numero > multiplo_5:
        print(multiplo_5, end= ' ')
        multiplo_5 += 5
    else:
        buscando_multiplos = False