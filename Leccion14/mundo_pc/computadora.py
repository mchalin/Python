from mundo_pc.monitor import *
from mundo_pc.raton import *
from mundo_pc.teclado import *


class Computadora:
    contador_computadoras = 0

    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contador_computadoras += 1
        self._id_computadora = Computadora.contador_computadoras
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton

    @property
    def id_computadora(self):
        return self._id_computadora

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def monitor(self):
        return self._monitor

    @monitor.setter
    def monitor(self, monitor):
        self._monitor = monitor

    @property
    def teclado(self):
        return self._teclado

    @teclado.setter
    def teclado(self, teclado):
        self._teclado = teclado

    @property
    def raton(self):
        return self._raton

    @raton.setter
    def raton(self, raton):
        self._raton = raton

    def __str__(self):
        return f'Computadora [Id: {self._id_computadora}, Nombre: {self._nombre}] \n>> {self._monitor} \n>> {self._teclado} \n>> {self._raton}'


monitor5 = Monitor('Noblex', '23"')
teclado5 = Teclado('USB', 'Gamer')
raton5 = Raton('USB', 'Logitech')

computadora1 = Computadora('Maxi', monitor5, teclado2, raton1)
print()
print(computadora1)

computadora2 = Computadora('Vale', monitor1, teclado2, raton5)
print()
print(computadora2)
