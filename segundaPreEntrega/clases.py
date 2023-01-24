class Clientes : 
    def __init__ (self, nombre, contra, edad, email): 
        self.nombre=nombre
        self.contra=contra
        self.edad=edad
        self.email= email
    
    def __str__(self):
        mensajeUsuario= f"Su usuario: {self.nombre} ha sido exitosamente creado"
        return mensajeUsuario
    
    def registro(self): 
        self.nombre = input("Por favor ingrese un Nombre de Usuario: ")
        self.edad = input("Qué edad tenés? ")
        self.email = input("Por favor ingrese su correo electrónico: ")
        self.contra=""
        while len(self.contra)<8:
            self.contra = input("Por favor ingrese una contraseña con un mínimo de 8 caracteres: ")

    def ingreso(self, nombre, contra): 
        if nombre == self.nombre and contra == self.contra: 
            return print(f"Bienvenido, {self.nombre}!")
        else: 
            return print(f"Usuario o contraseña incorrectos. Por favor vuelva a intentarlo.")