class Persona2:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    def mostrar_detalles(self):
        print(f'Los datos a mostrar son los siguientes: {self._nombre} {self._apellido} {self._edad} \n')

    @property  # Decorador, para crear metodo Getter
    def nombre(self):  # Metodo Getter
        print('Estamos utilizando el metodo Get')
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):  # Metodo Setter
        print('Estamos utilizando el metodo Set')
        self._nombre = nombre

    @property  # Decorador, para crear metodo Getter
    def apellido(self):  # Metodo Getter
        print('Estamos utilizando el metodo Get')
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):  # Metodo Setter
        print('Estamos utilizando el metodo Set')
        self._apellido = apellido

    @property  # Decorador, para crear metodo Getter
    def edad(self):  # Metodo Getter
        print('Estamos utilizando el metodo Get')
        return self._edad

    @edad.setter  # Decorador, para crear metodo Setter
    def edad(self, edad):  # Metodo Setter
        print('Estamos utilizando el metodo Set')
        self._edad = edad

    def __del__(self): # Metodo destructor
        print(f'Eliminando Persona2: {self._nombre} {self._apellido} {self._edad}')

if (__name__ == '__main__'):

    persona1 = Persona2('Maximiliano', 'Chalin', 39)
    print(persona1.nombre)  # llamamos al metodo Getter
    persona1.nombre = 'Max'  # Llamamos al metodo Setter
    print(persona1.apellido)  # llamamos al metodo Getter
    persona1.apellido = 'Chal'  # Llamamos al metodo Setter
    print(persona1.edad)  # llamamos al metodo Getter
    # Es solo lectura, no tiene Setter, la sintaxis de abajo da error
    # persona1.edad = 40 # Llamamos al metodo Setter

    persona1.mostrar_detalles()

    # Tarea: Crear 3 objetos mas, utilizando los metodos getter and setter
    # Para modificar y mostrar los cambios con el metodo mostrar_detalles

    # Objeto 1
    persona2 = Persona2('Juan', 'Chalin', 15)
    print(persona2.nombre)
    print(persona2.apellido)
    print(persona2.edad)
    persona2.nombre = 'Juani'
    persona2.apellido = 'Chalini'
    persona2.edad = 14
    persona2.mostrar_detalles()

    # Objeto 2
    persona3 = Persona2('Lucia', 'Chalin', 13)
    print(persona3.nombre)
    print(persona3.apellido)
    print(persona3.edad)
    persona3.nombre = 'Chula'
    persona3.apellido = 'Chalini'
    persona3.edad = 11
    persona3.mostrar_detalles()

    # Objeto 3
    persona4 = Persona2('Valeria', 'Alvarez', 37)
    print(persona4.nombre)
    print(persona4.apellido)
    print(persona4.edad)
    persona4.nombre = 'MiAmooor'
    persona4.apellido = 'Alvarini'
    persona4.edad = 36
    persona4.mostrar_detalles()
    print(__name__)
