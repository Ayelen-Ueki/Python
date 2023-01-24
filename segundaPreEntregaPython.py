from clases import *
import funciones as fun

Opcion = 0
while Opcion not in [1, 2, 3]:  # Check if the input is valid
    cliente1=Clientes("", 0, 0, "")
    Opcion=int(input("Por favor seleccione una de las siguientes opciones: \n 1 Para Ingresar\n 2 Para Registrase por primera vez\n 3 Para Salir \n"))
if Opcion == 1: 
    nombre = input("Por favor ingrese su Nombre de Usuario: ")
    contra = int(input("Por favor ingrese su Contraseña: "))
    cliente1.ingreso(nombre, contra)
  
elif Opcion == 2: 
  cliente1=cliente1.registro()
  print(cliente1)

else:
  fun.Salir()


