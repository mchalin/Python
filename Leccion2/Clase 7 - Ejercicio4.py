# haremos un programa que cuando el usuario ingrese su edad
# le diga, o imprima la etapa de su vida en una breve oracion
# 0 a 10 = la infancia es increible y bella
# 11 a 19 = tienes muchos cambios, mucho que estudiar
# 20 a 29 = amor y comienza el trabajo
# para las siguientes etapas deberas completarlo

edad = int(input("ingrese su edad: "))
if 0 < edad <= 10:
    print("la infancia es increible y bella")
elif 10 < edad <= 19:
    print("tienes muchos cambios, mucho que estudiar")
elif 19 < edad <= 29:
    print("amor y comienza el trabajo")
else:
    print("error, etapa de la vida no encontrada")
