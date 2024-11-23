class Usuario:
    def __init__(self, nombre, contrasena, edad):
        self.nombre = nombre
        self.contrasena = contrasena
        self.edad = edad
        self.historial_visualizacion = []
        self.preferencias = []

    def __str__(self):
        return self.nombre