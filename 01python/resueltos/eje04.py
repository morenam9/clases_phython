'''
4.	Escriba un programa que acepte 3 números y calcule el máximo, el mínimo y el promedio.
'''

print("Ingrese 3 números")

total_nums_ingresados = False
cant_num_ingresados = 0

numero1 = None
numero2 = None
numero3 = None


while total_nums_ingresados == False:

    if numero1 is None:
        numero1_raw = input('Nro 1 = ')
        str_numero1 = numero1_raw.strip()
        
        if (str_numero1.count('.') == 1 and str_numero1.replace('.', '').isdigit()) or (str_numero1.isdigit()):
            numero1 = float(numero1_raw.strip())
            cant_num_ingresados += 1
        
    elif numero2 is None:
        numero2_raw = input('Nro 2 = ')
        str_numero2 = numero2_raw.strip()
        
        if (str_numero2.count('.') == 1 and str_numero2.replace('.', '').isdigit()) or (str_numero2.isdigit()):
            numero2 = float(numero2_raw.strip())
            cant_num_ingresados += 1
    
    elif numero3 is None:
        numero3_raw = input('Nro 3 = ')
        str_numero3 = numero3_raw.strip()
        
        if (str_numero3.count('.') == 1 and str_numero3.replace('.', '').isdigit()) or (str_numero3.isdigit()):
            numero3 = float(numero3_raw.strip())
            cant_num_ingresados += 1
    
    if(cant_num_ingresados >= 3):
        total_nums_ingresados = True

#maximo
maximo = numero1
minimo = numero1
promedio = numero1

if numero2 > maximo:
    maximo = numero2

if numero3 > maximo:
    maximo = numero3

if numero2 < minimo:
    minimo = numero2

if numero3 < minimo:
    minimo = numero3

promedio = (numero1 + numero2 + numero3) / cant_num_ingresados


print(f'El máximo es {maximo}\n'
      f'El mínimo es {minimo}\n'
      f'El promedio es {promedio}')