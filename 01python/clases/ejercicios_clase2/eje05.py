'''
5.	Escriba un programa que acepte edad, peso, pulso, tensión y plaquetas, 
y determine si una persona cumple con estos requisitos para donar sangre.
'''

EDAD_MIN = 18
EDAD_MAX = 65

PESO_KG_MIN = 50
PESO_KG_MAX = 500

TENSION_DIAST_MMHG_MIN = 50
TENSION_DIAST_MMHG_MAX = 100

TENSION_SIST_MMHG_MIN = 90
TENSION_SIS_MMHG_MAX = 180

PULSO_PPM_MIN = 50
PULSO_PPM_MAX = 110

PLAQUETAS_CC_MIN = 150_000

NUM_TOTAL_VALS_PEDIDOS = 5



ingresando_datos = True

#Número de valores ingresados, hasta alcanzar el total NUM_TOTAL_VALS_PEDIDOS
n_val_ingresados = 0

#Supongo que es apta para donar salvo que alguno de los datos que se ingrese no sea adecuado
es_apto_donacion = True

#Valores a cargar
edad = None
peso = None
tension_sist = None 
tension_diast = None 
pulso = None
plaquetas = None

print("Registro de donacion de sangre\n")

while ingresando_datos:
    
    #Edad
    if edad == None:
        str_edad = input('Ingrese edad = ').strip()
        edad = int(str_edad) if str_edad.isdigit() else None
        n_val_ingresados += 1 if edad is not None else 0

    #Peso
    if peso == None:
        str_peso = input('Ingrese peso [Kg] = ').strip()
        peso = int(str_peso) if str_peso.isdigit() else None
        n_val_ingresados += 1 if peso is not None else 0
    
    #Tensión
    if tension_sist == None:
        str_tension = input('Ingrese tension [mmHg] (alta-baja) = ').replace(' ', '')
        
        #Verifico si respetó el formato, tiene que estar al menos el guión central

        if '-' in str_tension:
            
            idx_guion = str_tension.index('-')
            
            idx_ini = str_tension.find('(') #si no lo encuentra, vale -1

            idx_fin = str_tension.find(')') #si no lo encuentra, vale -1 

            if idx_ini == -1:
                idx_ini = 0
            else:
                #adelanto uno para que inicie el corte luego del paréntesis
                idx_ini += 1
            
            if idx_fin == -1:
                idx_fin = len(str_tension)
            
            str_tension_sist = str_tension[idx_ini: idx_guion]
            tension_sist = int(str_tension_sist) if str_tension_sist.isdigit() else None
        
            str_tension_diast = str_tension[idx_guion+1: idx_fin]
            tension_diast = int(str_tension_diast) if str_tension_diast.isdigit() else None
        
            n_val_ingresados += 1 if (tension_sist is not None) and (tension_diast is not None) else 0
    
    #Pulso
    if pulso == None:
        str_pulso = input('Ingrese pulso [ppm] = ').strip()
        pulso = int(str_pulso) if str_pulso.isdigit() else None
        n_val_ingresados += 1 if pulso is not None else 0

    #Plaquetas
    if plaquetas == None:
        str_plaquetas = input('Ingrese plaquetas [cc] = ').strip()
        plaquetas = int(str_plaquetas) if str_plaquetas.isdigit() else None
        n_val_ingresados += 1 if plaquetas is not None else 0


    #Condición de finalización de entrada de datos
    if n_val_ingresados == NUM_TOTAL_VALS_PEDIDOS:
        ingresando_datos = False


str_motivos = ''

#Verificación de rangos y explicación de motivos de rechazo si los hay
if not (EDAD_MIN <= edad <= EDAD_MAX):
    es_apto_donacion = False
    str_motivos += '\n\t- edad fuera de rango, '

if not (PESO_KG_MIN <= peso <= PESO_KG_MAX):
    es_apto_donacion = False
    str_motivos += '\n\t- peso fuera de rango, '

if not (TENSION_DIAST_MMHG_MIN <= tension_diast <= TENSION_DIAST_MMHG_MAX):
    es_apto_donacion = False
    str_motivos += '\n\t- tensión diastólica fuera de rango, '

if not (TENSION_SIST_MMHG_MIN <= tension_sist <= TENSION_SIS_MMHG_MAX):
    es_apto_donacion = False
    str_motivos += '\n\t- tensión sistólica fuera de rango, '

if not (PULSO_PPM_MIN <= pulso <= PULSO_PPM_MAX):
    es_apto_donacion = False
    str_motivos += '\n\t- pulso fuera de rango, '

if not (PLAQUETAS_CC_MIN <= plaquetas):
    es_apto_donacion = False
    str_motivos += '\n\t- plaquetas fuera de rango, '

str_motivos = str_motivos[:-2] if len(str_motivos) > 0 else ''

print(f'\nDatos ingresados:\n'
      f'\tedad = {edad}\n'
      f'\tpeso = {peso}\n'
      f'\ttension diastólica = {tension_sist}\n'
      f'\ttension sistólica = {tension_diast}\n'
      f'\tpulso = {pulso}\n'
      f'\tplaquetas = {plaquetas}\n')

print(f'{"Es" if es_apto_donacion else "No es"} Apto para donación'
      f'{"" if len(str_motivos) == 0 else " por los siguientes motivos: " + str_motivos}')
