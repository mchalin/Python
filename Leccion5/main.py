# Comenzamos ocn funciones

# Definimos una función
def mi_funcion():
    print('Holixxx a todos')


mi_funcion()


# Desempaquetado de listas o List Unpacking
def show(name, lastName):
    print(name + ' ' + lastName)


person = ["Maxi", "Chalin"]
show(person[0], person[1])  # Pasamos uno por uno los datos de la lista a la funcion
show(*person)  # Lo mismo que lo anterior pero le pasamos todo junto

person2 = ("Juani", "Chalin")
show(*person2)  # Desempaquetamos a través de una tupla

person3 = {"name": "Lucia", "lastName": "Chalin"}
show(**person3)  # Desempaquetamos a través de un diccionario

# Repaso for else
numbers = [1, 2, 3, 4, 5]
for n in numbers:
    print(n)
    # if n == 3:
    #     break
else:  # Al terminar el for, va hacia el else, salvo que tenga un break antes
    print("Esto se terminó.")

# Lista de comprension o List comprehension
names = ["Maxi", "Pepo", "Vale", "Paolo"]
alongP = [p for p in names if p[0] == 'P']  # Esto regresa una nueva lista
print(alongP)

bottleC = [{"name": "Quilmes", "country": "Arg"},
           {"name": "Corona", "country": "Mx"},
           {"name": "Stella Artois", "country": "Belgium"},
           ]
Arg = [b for b in bottleC if b["country"] == "Arg"]
print(Arg)
print(bottleC)


# Paso de argumentos (funciones)

def mi_funcion2(name, lastName):  # recibe Parámetro
    print("Saludos a todos!")
    print(f'Nombre: {name}, Apellido: {lastName}')


mi_funcion2('Maxi', 'Chalin')  # necesita Argumento
mi_funcion2('Juani', 'Chalin')  # necesita Argumento


# La palabra return en funciones
# Creamos una funcion para sumar

def sumar(a, b):  # parámetros
    return a + b


resultado = sumar(78, 22)  # paso de argumentos
print(f'El resultado de la suma es: {resultado}')
print(f'El resultado de la suma es: {sumar(10, 15)}')


# Valores por default en los parámetros de una funcion

def sumar2(a=0, b=0):  # Le asignamos un valor por default
    return a + b


resultado = sumar2()
print(f'Resultado de la suma: {resultado}')
print(f'Resultado de la suma: {sumar2(12, 34)}')


# Argumentos, variables en funciones
def listarNombres(*nombres): # Normalmente se utiliza: *args
    print(type(nombres))
    for nombre in nombres: # Se convierte en una tupla
        print(nombre)


listarNombres('MAxi', 'Juani', 'Vale', 'Lucia')
listarNombres('Marcos', 'Daniel', 'Romina', 'Carolina')
