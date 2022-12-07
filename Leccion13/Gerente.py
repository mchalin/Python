from Empleado import Empleado


class Gerente(Empleado):
    def __init__(self, nombre, sueldo, departamento):
        super().__init__(nombre, sueldo)
        self.departamento = departamento

    def __str__(self):
        return f'Gerente [Departamento: {self.departamento}] \n{super().__str__()}'


if __name__ == '__main__':
    gerente1 = Gerente('Maxi', 60000, 'Sistemas')
    empleado1 = Empleado('Juani', 2000)

    print(empleado1)
    print()
    print(gerente1)
