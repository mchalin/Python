from Leccion14.mundo_pc.computadora import *


class Orden:
    contador_ordenes = 0

    def __init__(self, lista):
        Orden.contador_ordenes += 1
        self._id_orden = Orden.contador_ordenes
        self._computadoras = list(lista)

    @property
    def computadoras(self):
        return self._computadoras

    @computadoras.setter
    def computadoras(self, computadoras):
        self._computadoras = computadoras

    @property
    def id_orden(self):
        return self._id_orden

    def agregar_computadora(self, computadora):
        self._computadoras.append(computadora)

    def __str__(self):
        contador = 0
        print(f'Orden N° {self._id_orden}')
        for computadora in self._computadoras:
            contador += 1
            print(f'\t\t\t{contador}->>')
            print(computadora, end='\n')
        return ''


print('\n\n')
paraOrden1 = [computadora1, computadora2]
orden1 = Orden(paraOrden1)
print(orden1)
orden1.agregar_computadora(computadora1)
print(orden1)
teclado3 = Teclado('Bluetooth', 'Dell')
teclado4 = Teclado('USB', 'Acer')
raton3 = Raton('USB', 'Razer')
raton4 = Raton('USB', 'Chess')
monitor3 = Monitor('Samsung', '14"')
monitor4 = Monitor('Philips', '27"')
computadora3 = Computadora('Juani', monitor5, teclado4, raton3)
computadora4 = Computadora('Lucia', monitor4, teclado1, raton5)
computadora5 = Computadora('Trabajo', monitor1, teclado2, raton4)

paraOrden2 = [computadora4]
orden2 = Orden(paraOrden2)
orden2.agregar_computadora(computadora1)
orden2.agregar_computadora(computadora2)
print(orden2)
print('\n\n')
paraOrden3 = [computadora1, computadora2, computadora3, computadora4]
orden3 = Orden(paraOrden3)
print(orden3)

print(orden3.id_orden)



