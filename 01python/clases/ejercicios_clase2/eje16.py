'''
16.	Escriba un programa que permita al usuario adivinar un número. 
Indicar si el número buscado es menor o mayor que el que se está preguntando y 
mostrar igualmente el número de intentos hasta encontrar el número objetivo
'''
NUMERO_A_ADIVINAR = 27

numero_adivinado = False

print('Adivine el numero, con cada intento recibirá una pista!')

while not numero_adivinado:
    str_numero = input("Ingrese un número positivo: ").strip()
    numero = int(str_numero) if str_numero.isdigit() else None

    if numero is None:
        print('No ingreso un número posible, intente de nuevo')
    
    else:
        if numero == NUMERO_A_ADIVINAR:
            numero_adivinado = True
            print("Acertó!\n")

        elif numero > NUMERO_A_ADIVINAR:
            print("El número es menor!\n")
        
        else:
            print("El número es mayor!\n")
