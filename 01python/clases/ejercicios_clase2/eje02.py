'''
2.	Dada una variable year con un valor entero, compruebe si dicho año es bisiesto o no lo es. 
Un año es bisiesto en el calendario Gregoriano, si es divisible entre 4 y no divisible entre 100, 
o bien si es divisible entre 400.
'''
ANIO_INI_CAL_GREGORIANO = 1582

str_resultado = ''

print(f"\nPrograma para comprobar si un año es bisiesto\n")

anio_raw = input("\tIntese año: ")

#Limpieza
str_anio = anio_raw.strip()

#Control de año válido
if(str_anio.isnumeric()):
    anio = int(str_anio)

    if (anio >= ANIO_INI_CAL_GREGORIANO):
        bisiesto = False

        if (anio % 4) == 0:
            
            if (anio % 100) != 0:
                bisiesto = True
            
            elif (anio % 400) == True:
                bisiesto = True

        #Asignar resultado
        if bisiesto:
            str_resultado = f'Es un año bisiesto'

        else:
            str_resultado = f'No es un año bisiesto'
    else:
        str_resultado = f'Para este año no existía el calendario Gregoriano, debe ser mayor a {ANIO_INI_CAL_GREGORIANO}'
else:
    str_resultado = f'El valor ingresado no es un año válido'

#Salida
print(f'\n{str_resultado}\n')