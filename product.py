class Product:

    def __init__(self, Nombre, Email, Contraseña):
        self.Nombre = Nombre
        self.Email = Email
        self.Contraseña = Contraseña

#crea una estructura de la colección
    def toDBCollection(self):
        return{
        'Nombre': self.Nombre,
        'Email': self.Email,
        'Contraseña': self.Contraseña
        }