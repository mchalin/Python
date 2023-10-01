from mi_clase import MiClase

# Muestra la ayuda de la clase
print("Ayuda de la clase".center(50, "-"))
help(MiClase)

# Muestra la documentación de la clase
print("Documentación de la clase".center(50, "-"))
print(MiClase.__doc__)

# Muestra la documentación del método __init__
print("Método __init__".center(50, "-"))
print(MiClase.__init__.__doc__)

# Muestra la documentación del método mi_metodo
print("Método mi_metodo".center(50, "-"))
print(MiClase.mi_metodo.__doc__)

# Imprimimos el objeto
print("Objeto".center(50, "-"))
print(MiClase.mi_metodo)

# Mostramos el tipo
print("Tipo".center(50, "-"))
print(type(MiClase.mi_metodo))