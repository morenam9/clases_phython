'''
1.	La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. 
Los ingredientes para cada tipo de pizza aparecen a continuación.

* Ingredientes vegetarianos: Pimiento y tofu.
* Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, 
y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. 
Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas las pizzas. 
Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y 
todos los ingredientes que lleva.

'''
#Creo unas constantes con los menúes disponibles

#Tipos de pizzas
TIPO_PIZZA_1 = 'vegetariana'
TIPO_PIZZA_2 = 'no vegetariana'

#Ingredientes
ING_1_PIZZ_TIPO_1 = 'pimiento'
ING_2_PIZZ_TIPO_1 = 'tofu'

ING_1_PIZZ_TIPO_2 = 'peperoni'
ING_2_PIZZ_TIPO_2 = 'jamon'
ING_3_PIZZ_TIPO_2 = 'salmón'

ING_1_PIZZ_COMUN = 'mozzarella'
ING_2_PIZZ_COMUN = 'tomate'

#Menúes
MENU_TIPO_PIZZA = f'Tipos de pizza\n' \
                  + f'\t1- {TIPO_PIZZA_1.capitalize()}\n' \
	              + f'\t2- {TIPO_PIZZA_2.capitalize()}\n' 

MENU_PIZZ_TIPO_1 = f'Ingrediente:\n' \
                  + f'\t1- {ING_1_PIZZ_TIPO_1.capitalize()}\n' \
                  + f'\t2- {ING_2_PIZZ_TIPO_1.capitalize()}\n'

MENU_PIZZ_TIPO_2 = f'Ingrediente:\n' \
                    + f'\t1- {ING_1_PIZZ_TIPO_2.capitalize()}\n' \
                    + f'\t2- {ING_2_PIZZ_TIPO_2.capitalize()}\n' \
                    + f'\t3- {ING_3_PIZZ_TIPO_2.capitalize()}\n'

MSJ_SELECCIONE = f'Su elección? '

MSJ_REINTENTE = f'** No es una opción disponible, reintente **'


#Mientras el pedido no se complete, pidiendo es igual a True
pidiendo = True

#Variable para guardar el pedido
str_pedido = f"Pizza "


print("\nBienvenido a la pizzeria Bella Napoli.\n")

while(pidiendo == True):
    
    #Selección de Tipo

    print(MENU_TIPO_PIZZA)
    
    tipo_pizza_raw = input(MSJ_SELECCIONE)

    #Limpieza de entrada
    str_tipo_pizza = tipo_pizza_raw.strip()
    
    #Prueno si escribió un tipo correctamente lo paso a una opcion numérica
    if str_tipo_pizza.lower() == TIPO_PIZZA_1:
        str_tipo_pizza = '1'

    elif str_tipo_pizza.lower() == TIPO_PIZZA_2:
        str_tipo_pizza = '2'

    #Sólo tomo el primer caracter, debiera ser un 1 o un 2, verifico
    if str_tipo_pizza[0].isnumeric():
            
        tipo_pizza = int(str_tipo_pizza[0])

        if tipo_pizza == 1:
            #Menú Vegetariano
            
            str_pedido += f'{TIPO_PIZZA_1} con {ING_1_PIZZ_COMUN}, {ING_2_PIZZ_COMUN} y '

            while pidiendo:
                
                print(MENU_PIZZ_TIPO_1)
            
                tipo_ingrediente_raw = input(MSJ_SELECCIONE)

                str_tipo_ingrediente = tipo_ingrediente_raw.strip()

                #Prueno si escribió un ingrediente correctamente lo paso a una opcion numérica
                if str_tipo_ingrediente.lower() == ING_1_PIZZ_TIPO_1:
                    str_tipo_ingrediente = '1'

                elif str_tipo_ingrediente.lower() == ING_2_PIZZ_TIPO_1:
                    str_tipo_ingrediente = '2'
                
                #Proceso la opción elegida
                if str_tipo_ingrediente[0].isnumeric():
                    
                    tipo_ingrediente = int(str_tipo_ingrediente[0])

                    if tipo_ingrediente == 1:
                        str_pedido += f'{ING_1_PIZZ_TIPO_1}'
                        pidiendo = False
                    
                    elif tipo_ingrediente == 2:
                        str_pedido += f'{ING_2_PIZZ_TIPO_1}'
                        pidiendo = False

                    else:
                        print(f'{MSJ_REINTENTE}\n')
            
                else:
                    print(f'{MSJ_REINTENTE}\n')
                
        elif tipo_pizza == 2:
            #Menú No Vegetariano
            
            str_pedido += f'{TIPO_PIZZA_2} con {ING_1_PIZZ_COMUN}, {ING_2_PIZZ_COMUN} y '

            while pidiendo:

                print(MENU_PIZZ_TIPO_2)
            
                tipo_ingrediente_raw = input(MSJ_SELECCIONE)

                str_tipo_ingrediente = tipo_ingrediente_raw.strip()
        
                tipo_ingrediente = int(str_tipo_ingrediente[0])
                
                #Prueno si escribió un ingrediente correctamente lo paso a una opcion numérica
                if str_tipo_ingrediente.lower() == ING_1_PIZZ_TIPO_1:
                    str_tipo_ingrediente = '1'

                elif str_tipo_ingrediente.lower() == ING_2_PIZZ_TIPO_2:
                    str_tipo_ingrediente = '2'

                elif str_tipo_ingrediente.lower() == ING_3_PIZZ_TIPO_2:
                    str_tipo_ingrediente = '3'

                #Proceso la opción elegida
                if str_tipo_ingrediente[0].isnumeric():

                    if tipo_ingrediente == 1:                      
                        str_pedido += f'{ING_1_PIZZ_TIPO_2}'
                        pidiendo = False
                    
                    elif tipo_ingrediente == 2:
                        str_pedido += f'{ING_2_PIZZ_TIPO_2}'
                        pidiendo = False

                    elif tipo_ingrediente == 3:
                        str_pedido += f'{ING_3_PIZZ_TIPO_2}'
                        pidiendo = False

                    else:
                        print(f'{MSJ_REINTENTE}\n')
    
                else:
                    print(f'{MSJ_REINTENTE}\n')

        else:
            print(f'{MSJ_REINTENTE}\n')
    
    else:
        print(f'{MSJ_REINTENTE}\n')


# Salida del programa, imprime el pedido
print(f'\nSu pedido:\n\t{str_pedido}\n')