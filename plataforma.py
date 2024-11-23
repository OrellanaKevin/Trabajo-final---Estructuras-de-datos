from arbol_binario import ArbolBinario
from contenido import Contenido
from usuario import Usuario

class Plataforma:
    def __init__(self, nombre):
        self.nombre = nombre
        self.contenido = Contenido()
        self.usuarios = ArbolBinario()

    def inicio_sesion(self):
        while True:
            print("\n1. Crear Usuario\n2. Iniciar Sesión\n3. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.crear_usuario()
            elif opcion == "2":
                usuario = input("Usuario: ")
                contrasena = input("Contraseña: ")
                if self.usuarios.buscar(usuario, contrasena):
                    self.menu_principal()
                else:
                    print("Usuario o contraseña incorrectos.")
            elif opcion == "3":
                print("¡Gracias por usar la plataforma!")
                break
            else:
                print("Opción no válida.")

    def crear_usuario(self):
        nombre = input("Nombre: ")
        contrasena = input("Contraseña: ")
        edad = int(input("Edad: "))
        usuario = Usuario(nombre, contrasena, edad)
        self.usuarios.insertar(usuario.nombre, usuario.contrasena)
        print(f"Usuario {nombre} creado con éxito.")

    def agregar_pelicula(self):
        print("\n--- Agregar Película ---")
        nombre = input("Nombre de la película: ")
        genero = input("Género: ")
        popularidad = int(input("Popularidad (número de visualizaciones): "))
        duracion = int(input("Duración (en minutos): "))
        self.contenido.agregar_pelicula(nombre, genero, popularidad, duracion)
        print(f"La película '{nombre}' fue agregada con éxito al catálogo.")

    def menu_principal(self):
        while True:
            print("\n--- Menú Principal ---")
            print("1. Ver contenido")
            print("2. Agregar película")  # Nueva opción
            print("3. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.contenido.mostrar_contenido()
            elif opcion == "2":  # Nueva funcionalidad agregar película
                self.agregar_pelicula()
            elif opcion == "3":
                break
            else:
                print("Opción no válida.")