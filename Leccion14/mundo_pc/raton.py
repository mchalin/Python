from Leccion14.mundo_pc.dispositivo_entrada import DispositivoEntrada


class Raton(DispositivoEntrada):
    contador_ratones = 0

    def __init__(self, tipo_entrada, marca):
        Raton.contador_ratones += 1
        self._id_raton = Raton.contador_ratones
        super().__init__(tipo_entrada, marca)

    @property
    def id_raton(self):
        return self._id_raton

    def __str__(self):
        return f'Raton [ID: {self._id_raton}] {super().__str__()}'

    # if __name__ == '__main__':


raton1 = Raton('USB', 'Logitech')
print(raton1)
raton2 = Raton('Bluetooth', 'HP')
print(raton2)
