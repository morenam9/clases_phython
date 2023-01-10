'''
7.	Determine si un número dado es un número primo.
No es necesario implementar ningún algoritmo en concreto. La idea es probar los números menores al dado e ir viendo si las divisiones tienen resto cero o no.
¿Podría optimizar su código? ¿Realmente es necesario probar con tantos divisores?
Ejemplo
•	Entrada: 11
•	Salida: Es primo
'''

numero = None

ingresando_numero = True

while ingresando_numero:
    str_numero = input("Ingrese un número natural: ").strip()
    numero = int(str_numero) if str_numero.isdigit() else None
    
    if numero is not None:
        ingresando_numero = False
    else:
        print(f'Valor ingresado incorrecto. Reintente')

# Divisor máximo para buscar
divisor_max = numero

#Suponemos en principio que no es primo salvo que cumpla las condiciones
es_primo = False

#Un número primo tiene solamente dos divisores, el primero es la unidad y el segundo es sí mismo
divisor_uno = None
divisor_dos = None

#Pruebo divisores desde el 1 hasta el máximo calculado
for divisor_test in range(1, (divisor_max + 1)):

    # #Para no probar los casos que se saben no darán un valor entero.
    # if (numero // 2) < divisor_test < numero:
    #     continue

    resto = numero % divisor_test

    if resto == 0: 
        if divisor_uno is None:
            divisor_uno = divisor_test
        
        elif divisor_dos is None:
            divisor_dos = divisor_test
            break

if (divisor_dos == numero):
    es_primo = True

print(f'{"Es" if es_primo else "No es"} un número primo'
      f'{"" if es_primo else f" con divisor menor = {divisor_dos if divisor_dos is not None else divisor_uno}"}')