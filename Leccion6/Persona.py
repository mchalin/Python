class Persona:  # Creamos una clase
    def __init__(self, nombre, apellido, dni, edad, *args, **kwargs):  # Se lo llama método Init Dunder
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self._dni = dni  # Este atributo esta encapsulado de una manera sugerida
        self.args = args
        self.kwargs = kwargs

    def mostrar_detalle(self):  # Self es igual a this
        print(
            f'La clase Persona tiene los siguientes datos: {self.nombre} {self.apellido} {self._dni} {self.edad}, la direccion es: {self.args}, los datos importantes son: {self.kwargs}')


persona1 = Persona('Maximiliano', 'Chalin', 30564631, 38)
print(f'El objeto 1 de la clase Persona: {persona1.nombre} {persona1.apellido} {persona1.edad}')

print(type(persona1.edad))

persona2 = Persona('Valeria', 'Alvarez', 32999444, 36)
print(f'El objeto 2 de la clase Persona: {persona2.nombre} {persona2.apellido} {persona2.edad}')

persona1.nombre = 'Juani'
persona1.edad = '15'
print(f'El objeto 1 modificado de la clase Persona: {persona1.nombre} {persona1.apellido} {persona1.edad}')

# Los atributos son caracteristicas
# Los metodos son el comportamiento que van a tener los objetos (acciones)
persona1.mostrar_detalle()  # La referencia se pasa de forma automatica
persona2.mostrar_detalle()

# Llamando el metodo desde la clase, no se utiliza..
# Persona.mostrar_detalle(persona1) # Debemos pasar una referencia para el self o dará error

# Creamos un atributo a un objeto (Superficial, no se puede acceder de ningun otro objeto)
persona1.telefono = '12345678'
print(f'Este es el telefono de {persona1.nombre}: {persona1.telefono}')
# persona2.telefono # Arroja error

persona3 = Persona('Lucia', 'Chalin', 12345678, 13, 'Telefono', '2915271717', 'Chacabuco', 2269, 'Manzana', 2, 'Casa',
                   18,
                   Altura=1.83, Peso=59, ColorFav='Rosa', Auto='No tiene', Modelo='No tiene')
persona4 = Persona('Juani', 'Chalin', 98765432, 15, 'Telefono', '2914344434', 'Chacabuco', 1234, 'Manzana', 5, 'Casa',
                   20,
                   Altura=1.88, Peso=80, ColorFav='Verde', Auto='Bici', Modelo='2022')
persona3.mostrar_detalle()
persona4.mostrar_detalle()

print(persona3._dni)  # Funciona pero esta mal, esta encapsulado!!!
# print(persona3.__nombre) # Totalmente encapsulado, no deja modificar desde fuera de la clase
