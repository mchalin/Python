# Ejercicio 9: Mostrar una frase sin espacios y contar su longitud
# Hacer un programa donde el usuario ingrese una frase, se le devolverá la misma
# frase pero sin espacios en blanco, y además un contador de cuantos caracteres tiene
# la frase, sin contar los espacios en blanco
# Ejemplo:      frase = vivir por siempre en paz
#               frase final = vivirporsiempreenpaz
#               nro de caracteres = 20
print("Mostrar una frase sin espacios y contar su longitud.")
frase = input("Ingrese una frase: ")
frasenueva = ""
for letra in frase:
    if letra != " ":
        frasenueva += letra

print(f'''
La nueva frase sin espacios es:
[{frasenueva}]
y tiene {len(frasenueva)} caracteres.''')