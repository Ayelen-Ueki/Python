from funciones import *

Opcion = 0
while Opcion not in [1, 2, 3]:  # Check if the input is valid
  Opcion=int(input("Por favor seleccione una de las siguientes opciones: \n 1 Para Ingresar\n 2 Para Registrase por primera vez\n 3 Para Salir \n"))
if Opcion == 1: 
  ingreso()
  confirmacion()
elif Opcion == 2: 
  registro()
else:
  salir()