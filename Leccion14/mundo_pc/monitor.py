class Monitor:
    contador_monitores = 0

    def __init__(self, marca, tamanio):
        Monitor.contador_monitores += 1
        self._id_monitor = Monitor.contador_monitores
        self._marca = marca
        self._tamanio = tamanio

    @property
    def id_monitor(self):
        return self._id_monitor

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def tamanio(self):
        return self._tamanio

    @tamanio.setter
    def tamanio(self, tamanio):
        self._tamanio = tamanio

    def __str__(self):
        return f'Monitor [ID: {self._id_monitor}, Marca: {self._marca}, Tamaño: {self._tamanio}]'


monitor1 = Monitor('LG', '19"')
print(monitor1)
monitor2 = Monitor('HP', '24"')
print(monitor2)
