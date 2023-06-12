from logger_base import log


class Persona:
    def __init__(self, id_persona=None, nombre=None, apellido=None, email=None):
        self._id_persona = id_persona
        self._nombre = nombre
        self._apellido = apellido
        self._email = email

    def __str__(self):
        return f'''
            Id: {self._id_persona}, 
            Nombre: {self._nombre}, 
            Apellido: {self._apellido}, 
            Email: {self._email}
        '''

    # Métodos Getters y Setters
    @property
    def id_persona(self):
        return self._id_persona

    @id_persona.setter
    def id_persona(self, id_persona):
        self._id_persona = id_persona

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email


if __name__ == '__main__':
    persona1 = Persona(1, 'Juan', 'Perez', 'juan@perez.com')
    log.debug(persona1)
    # Simulamos un cambio de nombre
    persona1.nombre = 'Juan Carlos'
    log.debug(persona1)

    # Aclaramos la falta de argumentos
    persona2 = Persona(nombre='Karla', apellido='Gomez', email='karla@gomez.com')
    log.debug(persona2)

    persona2 = Persona(id_persona=2)
    log.debug(persona2)
    

