'''
3.	Escriba un programa en Python que acepte la opción de dos jugadoras en Piedra-Papel-Tijera y
 decida el resultado
'''
#Constantes

PIEDRA = 'piedra'
PAPEL = 'papel'
TIJERA = 'tijera'

PIEDRA_VS_PAPEL = 'papel'
TIJERA_VS_PAPEL = 'tijera'
PIEDRA_VS_TIJERA = 'piedra'

MOTIVO_GAN_PIEDRA_VS_PAPEL = 'el papel envuelve a la piedra'
MOTIVO_GAN_TIJERA_VS_PAPEL = 'la tijera corta el papel'
MOTIVO_GAN_PIEDRA_VS_TIJERA = 'la piedra desafila la tijera'
MOTIVO_EMPATE = 'ambos objetos son iguales'

MSJ_REINTENTE = f'\n** Alguna o ambas de las opciones son incorrectas, reintente **\n'

#Menúes
MENU_OPCIONES = f'Seleccione un objeto\n' \
                  + f'\t1- {PIEDRA.capitalize()}\n' \
	              + f'\t2- {PAPEL.capitalize()}\n' \
                  + f'\t3- {TIJERA.capitalize()}\n'

#Variables globales
ganador = 0 # 0: empate | 1: ganador jugador 1 | 2: ganador jugador 2

#Bandera para controlar que las opciones elegidas por los jugadores sean válidas
opciones_validas = False

print(f"\nJuego de Piedra - Papel - Tijera\n")

while opciones_validas == False:

    print(f'{MENU_OPCIONES}')

    opcion_jugador1_raw = input('Opcion Jugador 1?: ')
    opcion_jugador2_raw = input('Opcion Jugador 2?: ')

    opcion_jugador1 = opcion_jugador1_raw.lower().strip()
    opcion_jugador2 = opcion_jugador2_raw.lower().strip()

    if opcion_jugador1[0] == '1':
        opcion_jugador1 = PIEDRA

    elif opcion_jugador1[0] == '2':
        opcion_jugador1 = PAPEL

    elif  opcion_jugador1[0] == '3':
        opcion_jugador1 = TIJERA

    if opcion_jugador2[0] == '1':
        opcion_jugador2 = PIEDRA
    
    elif opcion_jugador2[0] == '2':
        opcion_jugador2 = PAPEL
    
    elif  opcion_jugador2[0] == '3':
        opcion_jugador2 = TIJERA


    if opcion_jugador1 == opcion_jugador2:
        #Empate
        
        #Verifico que sean objetos del juego
        if opcion_jugador1 == PIEDRA or opcion_jugador1 == PAPEL or opcion_jugador1 == TIJERA: 
            ganador = 0
            opciones_validas = True

    else:

        if opcion_jugador1 == PIEDRA:
            
            if opcion_jugador2 == TIJERA:
                ganador = 1 if opcion_jugador1 == PIEDRA_VS_TIJERA else 2
                opciones_validas = True
            
            elif opcion_jugador2 == PAPEL:
                ganador = 1 if opcion_jugador1 == PIEDRA_VS_PAPEL else 2
                opciones_validas = True

        elif opcion_jugador1 == PAPEL:
            
            if opcion_jugador2 == TIJERA:
                ganador = 1 if opcion_jugador1 == TIJERA_VS_PAPEL else 2
                opciones_validas = True
            
            elif opcion_jugador2 == PIEDRA:
                ganador = 1 if opcion_jugador1 == PIEDRA_VS_PAPEL else 2
                opciones_validas = True
        
        elif opcion_jugador1 == TIJERA:
            
            if opcion_jugador2 == PAPEL:
                ganador = 1 if opcion_jugador1 == TIJERA_VS_PAPEL else 2
                opciones_validas = True
            
            elif opcion_jugador2 == PIEDRA:
                ganador = 1 if opcion_jugador1 == PIEDRA_VS_TIJERA else 2
                opciones_validas = True

    if not(opciones_validas):
        print(MSJ_REINTENTE)

#Supongo al inicio que fue un empate
str_ganador = 'ninguno'
opcion_ganador = 'misma'

#Según quién haya ganado se cargan las variables
if ganador == 1:
    str_ganador = 'jugador 1'
    opcion_ganador = opcion_jugador1
elif ganador == 2:
    str_ganador = 'jugador 2'
    opcion_ganador = opcion_jugador2    

#Motivo del ganador
str_motivo_ganador = MOTIVO_EMPATE

if 0 < MOTIVO_GAN_PIEDRA_VS_PAPEL.find(opcion_ganador) <= 10:
    str_motivo_ganador = MOTIVO_GAN_PIEDRA_VS_PAPEL

elif 0 < MOTIVO_GAN_PIEDRA_VS_TIJERA.find(opcion_ganador) <= 10:
    str_motivo_ganador = MOTIVO_GAN_PIEDRA_VS_TIJERA

elif 0 < MOTIVO_GAN_TIJERA_VS_PAPEL.find(opcion_ganador) <= 10:
    str_motivo_ganador = MOTIVO_GAN_TIJERA_VS_PAPEL

#Salida
print(f'\nEl ganador es {str_ganador} porque {str_motivo_ganador}\n')