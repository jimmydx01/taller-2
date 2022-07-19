lista= list()
from io  import open

class Profesor:
    def __init__(self):
        self.materia=( )
        self.nombre=(" ")
        self.telefono=( )
        self.cursos=(" ")
        self.cedula=(" ")
def menu():
    seleccion=0
    while  seleccion != 4:
        print("bienvenido: ")
        print("eliga una opcion")
        print("--------------------------------")
        print("1. registar asistencia")
        print("2.mostrar clase que me toca ")
        print("3.revisar_tarea")
        print("4.salir")
        seleccion = int(input("eliga una opcion"))
        if seleccion== 1:
            registar()
        if seleccion == 2:    
            mostrar()
        if seleccion == 3:
            revisar()
        if seleccion == 4:
            salir()        
def registar():
    print("esta es la funcion de registro")
    profesor=Profesor()
    profesor.nombre=input("nombre")
    profesor.cursos=input("ingerse su curso de hoy ")
    profesor.materia=input("ingerse la materia a inpartir ")
    lista.append(profesor)
def mostrar():
    print("esta es la funcion de mostrar clase que le toca dar ")
    for profesor in lista:
        print("el",profesor.nombre,"de la  clase" , profesor.materia,"en el curso de",profesor.cursos)
def revisar():
    print("esta es la funcion revisa las tareas ")
    
            
        
def salir():
    print("gracias por usar nuestra aplicacion ")


    

                


