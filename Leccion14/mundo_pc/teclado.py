from Leccion14.mundo_pc.dispositivo_entrada import DispositivoEntrada


class Teclado(DispositivoEntrada):
    contador_teclados = 0

    def __init__(self, tipo_entrada, marca):
        Teclado.contador_teclados += 1
        self._id_teclado = Teclado.contador_teclados
        super().__init__(tipo_entrada, marca)

    @property
    def id_teclado(self):
        return self._id_teclado

    def __str__(self):
        return f'Teclado [ID: {self._id_teclado}] {super().__str__()}'


teclado1 = Teclado('USB', 'Razer')
print(teclado1)
teclado2 = Teclado('Bluetooth', 'Acer')
print(teclado2)
