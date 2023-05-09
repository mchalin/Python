from dominio.Pelicula import Pelicula
from servicio.CatalogoPeliculas import CatalogoPeliculas as cp


def menu():
    opcion = None

    while opcion != 4:
        try:
            print('Opciones:')
            print('1. Agregar película')
            print('2. Listar películas')
            print('3. Borrar películas')
            print('4. Salir')

            opcion = int(input('Seleccione la opción [1-4]: '))
            if opcion == 1:
                nombre_pelicula = input('Ingrese el nombre de la película: ')
                pelicula = Pelicula(nombre_pelicula)
                cp.agregar_pelicula(pelicula)
            elif opcion == 2:
                cp.listar_peliculas()
            elif opcion == 3:
                cp.eliminar_peliculas()

        except Exception as e:
            print(f'Ocurrió un error de tipo: {e}')
            opcion = None

        else:
            print('Salimos del programa')


if __name__ == '__main__':
    menu()
