# Archivo que inicia el programa y ejecuta el menu principal.1

from plataforma import Plataforma

def main():
    print("\n>> Bienvenidos a la Plataforma de Streaming <<\n")
    plataforma = Plataforma("Disney Plus")
    plataforma.inicio_sesion()
    
if __name__ == "__main__":
    main()

