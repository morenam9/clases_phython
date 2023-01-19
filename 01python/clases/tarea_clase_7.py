#Mensaje de bienvenida -- MENU

print("Bienvenido al sistema de consultas de la EPES 50")
mensaje = print(""" M E N U :
1.Cargar Alumno
2.Asignar una libreta
3.Cargar las notas de cada alumno
4.Consultar la libreta
5.Consultar mejor promedio por grado
6.Consultar materias por maestro
7.Consultar cuántos alumnos tiene cada materia.
8.Consultar cuántos alumnos en total tiene cada maestro""")
seleccion = int(input("INGRESE UNA OPCION : "))
    if seleccion == 1:
        cargar_alumno()
    elif seleccion == 2:
        asignar_libreta()
    elif seleccion == 3:
        cargar_notas()
    elif seleccion == 4:
        consultar_libreta()
    elif seleccion == 5:
        mejor_promedio_x_grado()
    elif seleccion == 6:
        materias_x_maestro()
    elif seleccion == 7:
        alumnos_x_materia()
    elif seleccion == 8:
        alumnos_x_profesor()
    else:
        exit


"""
1.Crear una clase "Alumno".
"""

lista_alumnos = []


class Alumno:
    def __init__(self, legajo, nombre, grado):
        self.legajo = legajo
        self.nombre = nombre
        self.grado = grado

    def add_materia(self, materia, nota):
        self.materias.append({"materia": materia, "nota": nota})
    #Para agregar una materia y su nota a un alumno existente:
    #alumno1.add_materia("Matemáticas", 8)

#Crear un nuevo alumno:

alumno1 = lista_alumnos.append(Alumno("Martín Dominguez", 10, 1))
alumno2 = lista_alumnos.append(Alumno("Marcela Morelo", 20, 2))
alumno3 = lista_alumnos.append(Alumno("Eduardo Verti", 30, 1))
alumno4 = lista_alumnos.append(Alumno("Mirta Ledezma", 40, 3))
alumno5 = lista_alumnos.append(Alumno("Jeremías Navarro", 50, 1))
alumno6 = lista_alumnos.append(Alumno("Silvina Saires", 60, 3))
alumno7 = lista_alumnos.append(Alumno("Miguel Carrizo",70, 2))
alumno8 = lista_alumnos.append(Alumno("Nora Morales", 80 , 1))
alumno9 = lista_alumnos.append(Alumno("Virginia López", 90, 3))
alumno10 = lista_alumnos.append(Alumno("Guillermo Brito", 100, 2))
alumno11 = lista_alumnos.append(Alumno("Martina Torres", 110, 1))
alumno12 = lista_alumnos.append(Alumno("Bart Simpson", 120, 3))


"""
2.Crear una clase "Libreta".
"""
class Libreta:
    def __init__(self, grado):
        self.grado = grado

    def promedio(self, materias):
        notas = [materia["nota"] for materia in materias]
        return sum(notas) / len(notas)

# Nueva libreta de un grado específico:
libreta1 = Libreta("1ro")
libreta2 = Libreta("2do")
libreta3 = Libreta("3ro")
#Para calcular el promedio de un alumno:
promedio1 = libreta1.promedio(alumno1.materias)
promedio2 = libreta1.promedio(alumno2.materias)
promedio3 = libreta1.promedio(alumno3.materias)

"""
3.Crear una clase "Materia".
"""
class Materia:
    def __init__(self, nombre):
        self.nombre = nombre
        self.alumnos = []

    def add_alumno(self, alumno):
        self.alumnos.append(alumno)

#Para crear una nueva materia:
artes = Materia("Artes")
matematicas = Materia("Matematicas")
geografia = Materia("Geografia")
educacion_fisica = Materia("Educacion Fisica")
cs_naturales = Materia("Ciencias Naturales")
lengua = Materia("Lengua")
historia = Materia("Historia")
formacion_civica = Materia("Formacion Civica")
ingles = Materia("Ingles")


#Para agregar un alumno a una materia:

#1ro
artes.add_alumno(alumno1, alumno3, alumno5, alumno8, alumno11)
matematicas.add_alumno(alumno1, alumno3, alumno5, alumno8, alumno11)
geografia.add_alumno(alumno1, alumno3, alumno5, alumno8, alumno11)
#2do
educacion_fisica.add_alumno(alumno2, alumno7, alumno10)
cs_naturales.add_alumno(alumno2, alumno7, alumno10)
lengua.add_alumno(alumno2, alumno7, alumno10)
#3ro
historia.add_alumno(alumno4, alumno6, alumno9, alumno12)
formacion_civica.add_alumno(alumno4, alumno6, alumno9, alumno12)
ingles.add_alumno(alumno4, alumno6, alumno9, alumno12)

"""
4.Crear una clase "PROFESOR".
"""
class Profesor:
    def __init__(self, nombre, matricula):
        self.nombre = nombre
        self.matricula = matricula
        self.materias = []

    def add_materia(self, materia):
        self.materias.append(materia)
#Para crear un nuevo profesor:
profesor1 = Profesor("Augusto Gutierres", "M10")
profesor2 = Profesor("Cecilia Peña", "M20")
profesor3 = Profesor("Sandra Almada", "M30")
profesor4 = Profesor("Hugo Carrizo", "M40")
#Para agregar una materia a un profesor existente:
profesor1.add_materia(artes, historia)
profesor2.add_materia(matematicas, cs_naturales)
profesor3.add_materia(geografia, lengua, formacion_civica, ingles)
profesor4.add_materia(educacion_fisica)
"""
5.Crear una función para cargar un alumno, que instancie un objeto de la clase "Alumno" y lo agregue a una lista de alumnos.
"""
def cargar_alumno():
        while True:
            nombre = input("Ingrese el nombre del alumno: ")
            legajo = input("Ingrese el legajo del alumno: ")
            grado = input("Ingrese el grado del alumno: ")
            alumno = Alumno(nombre, legajo, grado)
            lista_alumnos.append(alumno)
            continuar = input("¿Desea agregar otro alumno? (s/n): ")
            if continuar.lower() != "s":
                break

"""
6.Crear una función para asignar una libreta a cada alumno, que instancie un objeto de la clase "Libreta" y lo asigne al alumno correspondiente.
"""
def cargar_notas(legajo):
    alumno = next((alumno for alumno in lista_alumnos if alumno.legajo == legajo), None)
    if alumno:
        while True:
            materia = input("Ingrese el nombre de la materia, al finalizar (ingrese 'terminar'): ")
            if materia.lower() == "terminar":
                break
            nota = input("Ingrese la nota de la materia: ")
            alumno.add_materia(materia, nota)
    else:
        print("No se encontró un alumno con el legajo ingresado.")

"""
7.Crear una función para cargar las notas de cada alumno, que reciba como parámetro el legajo del alumno y las notas de cada materia.
"""
"""
8.Crear una función para consultar la libreta de un alumno dado su legajo, que busque el alumno correspondiente en la lista de alumnos y devuelva su libreta.
"""
"""
9.Crear una función para consultar el alumno con mejor promedio por grado, que recorra la lista de alumnos y busque aquel con el mejor promedio en su grado.
"""
"""
10.Crear una función para consultar qué materias dicta un maestro dado su nombre, que busque al maestro correspondiente en una lista de maestros y devuelva las materias que dicta.
"""
"""
11.Crear una función para consultar cuántos alumnos tiene cada materia, que recorra la lista de materias y devuelva el tamaño de la lista de alumnos matriculados en cada una.
"""
"""
12.Crear una función para consultar cuántos alumnos en total tiene un maestro dado su nombre, que busque al maestro correspondiente en una lista de maestros y sume el tamaño de las listas de alumnos matriculados en las materias que dicta.
"""