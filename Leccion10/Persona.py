class Persona:
    contador_personas = 0  # Variable de clase

    @classmethod
    def generar_siguiente_valor(cls):
        cls.contador_personas += 1
        # print('Método de clase. Se genera nuevo valor!')
        return cls.contador_personas

    def __init__(self, nombre, edad):
        Persona.generar_siguiente_valor()
        # Persona.contador_personas += 1  # Incrementa en 1
        self.id_persona = Persona.contador_personas
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'Persona [ID: {self.id_persona} - NOMBRE: {self.nombre} - EDAD: {self.edad}]'


persona1 = Persona('Maximiliano', 39)
print(persona1)
persona2 = Persona('Juani', 15)
print(persona2)

print(f'El valor de la variable de clase contador de personas es: {Persona.contador_personas}\n')

persona3 = Persona('Lucia', 13)
print(persona3)
print('Se ejecuta el método de clase Persona.generar_siguiente_valor()\n')
Persona.generar_siguiente_valor()
persona4 = Persona('Vale', 37)
print(persona4)
