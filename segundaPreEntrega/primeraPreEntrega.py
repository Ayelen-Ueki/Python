"""
1 Para Ingresar
2 Para Registrase por primera vez
3 Para Salir 
"""

from google.colab import drive
import json
import os

drive.mount("/drive/")

ruta = "/drive/MyDrive/Python/"

"""f = open(ruta + "Usuarios.txt") 

print(f.read())

f.close()"""

f = open(ruta + "Usuarios.txt", "a") 

def Registro(): 
  Nombre = input("Por favor ingrese un Nombre de Usuario: ")
  Contraseña = ""

  while len(Contraseña)<8:
      Contraseña = input("Por favor ingrese una contraseña con un mínimo de 8 caracteres: ")
      
  UsuarioNuevo = {"NOMBRE":Nombre,"PASS":Contraseña}
  Usuarios = []

   
  if  os.stat(ruta + "Usuarios.txt").st_size == 0:
    f = open(ruta + "Usuarios.txt", "a")
    f.write('{"NOMBRE":"mayueki","PASS":"12345678"}')
    f.write(",")
    f.write(str(UsuarioNuevo))
    f.close()
  else: 
    f = open(ruta + "Usuarios.txt", "a")
    f.write(str(UsuarioNuevo))
    f.close()
    
  f = open(ruta + "Usuarios.txt", "r") 
  for lines in f: # Append a new dictionary to my list of dictionaries in the file 
    Usuarios.append(lines)
    #f = open(ruta + "Usuarios.txt", "w") 
    #f.write(str(Usuarios).strip())

def Confirmacion():
  with open(ruta + "Usuarios.txt", "r") as BaseUsuarios:
    for line in BaseUsuarios:
       user = [json.loads(x.replace("'", "")) for x in line]
       for key, value in user.items: 
         print (f"Usuario:{key}, Contraseña:{value}")

def Ingreso(): 
  NombreIngresado = input("Por favor ingrese su Nombre de Usuario: ")
  ContraseñaIngresada = input("Por favor ingrese su Contraseña: ")

  with open(ruta + "Usuarios.txt", "r") as BaseUsuarios:
      for line in BaseUsuarios:  # Read the file line by line
          #user = json.loads(line.strip())  # Parse the line as a JSON object
          user = [json.loads(x.replace("'", "")) for x in line]
          print(user)
          if user["NOMBRE"] == NombreIngresado and user["CONTRASEÑA"] == ContraseñaIngresada:
              print("Has ingresado exitosamente")
              return user # Exit the function
          else:
              print("Usuario o contraseña incorrecto. Por favor vuelve a intentarlo")
def Salir():
  print("Hasta pronto!")

def guardarArchivo(datos): 
  with open(ruta + "Usuarios.txt", "w") as file:
    json.dump(datos, file, indent=4) 

Opcion = 0
while Opcion not in [1, 2, 3]:  # Check if the input is valid
  Opcion=int(input("Por favor seleccione una de las siguientes opciones: \n 1 Para Ingresar\n 2 Para Registrase por primera vez\n 3 Para Salir \n"))
if Opcion == 1: 
  Ingreso()
  Confirmacion()
elif Opcion == 2: 
  Registro()
else:
  Salir()
