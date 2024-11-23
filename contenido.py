# Ahora maneja listas para peliculas y series.
from peliculas import Pelicula
from series import Serie

class Contenido:
    def __init__(self):
        self.peliculas = []
        self.series = []

    def agregar_pelicula(self, nombre, genero, popularidad, duracion):
        pelicula = Pelicula(nombre, genero, popularidad, duracion)
        self.peliculas.append(pelicula)

    def mostrar_contenido(self):
        print("\n--- Contenido Disponible ---")
        for pelicula in self.peliculas:
            print(f"Pelicula: {pelicula.nombre} | Género: {pelicula.genero} | Popularidad: {pelicula.popularidad}")