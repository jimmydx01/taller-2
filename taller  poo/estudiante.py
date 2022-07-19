lista= list()

class Estudiante:
    def __init__(self):
        self.matricula=( )
        self.nombre=(" ")
        self.edad=( )
        self.carrera=(" ")
        self.curso=(" ")
        self.email=(" ")
def menu():
    seleccion=0
    while  seleccion != 6:
        print("bienvenido: ")
        print("eliga una opcion")
        print("--------------------------------")
        print("1. registar alumno")
        print("2.matricular alunmo")
        print("3.mostrar alunmo")
        print("4.buscar alumno")
        print("5.asistencia")
        print("6.salir")
        seleccion = int(input("eliga una opcion"))
        if seleccion== 1:
            registar()
        if seleccion == 2:    
            matricula()
        if seleccion == 3:
            mostrar()
        if seleccion == 4:
            buscar()   
        if asistencia() == 5:
            asistencia()    
        if seleccion == 6:
            salir()        
def registar():
    print("esta es la funcion de registro")
    estudiante=Estudiante()
    estudiante.matricula=input("introduce la matricula ")
    estudiante.nombre=input("introduce el nombre")
    estudiante.edad=input("introduce te edad")
    estudiante.carrera=input("introduce te carrera")
    lista.append(estudiante)
def matricula():
    print("esta es  de  matricula") 
    estudiante=Estudiante
    estudiante.nombre=input("introduce el nombre")
    estudiante.carrera=input("introduce te carrera")
    estudiante.email=input("introduce te email")
def asistencia():
    print("esta es de asistencia")    
    estudiante=Estudiante
    estudiante.nombre=input("introduce el nombre")
    estudiante.curso=input("introduce te curso")
    estudiante.carrera=input("introduce te carrera")
       
def mostrar():
    print("esta es la funcion de mostrar alumno")
    for estudiante in lista:
        print("el",estudiante.nombre,"de la  matricula" , estudiante.matricula,"con la edad",estudiante.edad)
def buscar():
    print("esta es la funcion para buscar alumnos")
    matricula=input("la matricula o el nombre")
    for estudiante in lista:
        if estudiante.matricula == matricula or estudiante.nombre == matricula:
            print(estudiante.nombre,estudiante.matricula,estudiante.edad,estudiante.carrera)

            
        
def salir():
    print("gracias por usar nuestra aplicacion ")


    

                


