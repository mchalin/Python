import os

from catalogo_peliculas.dominio.Pelicula import Pelicula


class CatalogoPeliculas:
    # atributo de clase
    ruta_archivo = 'peliculas.txt'

    # metodo de clase
    @classmethod
    def agregar_pelicula(cls, pelicula: Pelicula):
        with open(cls.ruta_archivo, 'a', encoding='utf8') as archivo:
            archivo.write(f'{pelicula.nombre}\n')

    @classmethod
    def listar_peliculas(cls):
        with open(cls.ruta_archivo, 'r', encoding='utf8') as archivo:
            print(f'Catálogo de películas'.center(50, '-'))
            print(archivo.read())

    @classmethod
    def eliminar_peliculas(cls):
        os.remove(cls.ruta_archivo)
        print(f'Archivo eliminado: {cls.ruta_archivo}')
