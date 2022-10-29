class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def __str__(self):  # Override = sobreescribir
        return f'Persona        Nombre: {self._nombre}  Edad: {self._edad}'

    def mostrar_datos(self):
        print(f'''Mostrando datos de {self}
              Nombre: {self.nombre}
              Edad: {self.edad}
          ''')


class Empleado(Persona):  # Clase hija de la clase Persona
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self._sueldo = sueldo

    @property
    def sueldo(self):
        return self._sueldo

    @sueldo.setter
    def sueldo(self, sueldo):
        self._sueldo = sueldo

    def __str__(self): # Override -> Sobreescribe el metodo
        return f'Empleado        Sueldo: {self._sueldo}  {super().__str__()}'

    def mostrar_datos(self):
        print(f'''Mostrando datos de {self}
            Nombre: {self.nombre}
            Edad: {self.edad}
            Sueldo: {self.sueldo}
        ''')


# empleado1 = Empleado("Maxi", 39, 15000)
# print(empleado1.nombre)
persona1 = Persona("Maxi", 39)
print(persona1.edad)
persona1.mostrar_datos()
empleado1 = Empleado("Juan", 30, 20000)
print(empleado1.sueldo)

# Tarea
# Encapsular los atributos y agregar los getters and setters
# Crear otro objeto, pasar los datos para nombre, edad, sueldo
# Mostrar estos datos, luego modificar y mostrar nuevamente

empleadoTarea = Empleado("Vale", 37, 40000)
empleadoTarea.mostrar_datos()

# Modificando datos de empleadoTarea
print("Modificando datos! ...")
empleadoTarea.nombre = "Valeria"
empleadoTarea.edad = 40
empleadoTarea.sueldo = 1000000
print()

# Mostrando datos nuevamente
empleadoTarea.mostrar_datos()
