from Empleado import Empleado
from Gerente import Gerente


def imprimir_detalle(objeto):
    # print(objeto)  # De manera indirecta, estamos llamando al __srt__() de la clase referenciada
    print(type(objeto))  # Para saber que dato recibe
    print(objeto.mostrar_detalles())
    if isinstance(objeto, Gerente):
        print(objeto.departamento)


empleado1 = Empleado('Juani', 3000)
gerente1 = Gerente('Maxi', 30000, 'Sistemas')

imprimir_detalle(empleado1)
imprimir_detalle(gerente1)
