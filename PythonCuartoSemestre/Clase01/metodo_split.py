help(str.split)

cursos = "Python Java JavaScript C# C++ C Ruby PHP"
print("cursos: ", cursos)
lista_cursos = cursos.split()
print("lista_cursos: ", lista_cursos)
print("tipo: ", type(lista_cursos))

cursos = "Python,Java,JavaScript,C#,C++,C,Ruby,PHP"
print("cursos: ", cursos)
lista_cursos = cursos.split(",")
print("lista_cursos: ", lista_cursos)
print("tipo: ", type(lista_cursos))

cursos = "Python,Java,JavaScript,C#,C++,C,Ruby,PHP"
print("cursos: ", cursos)
lista_cursos = cursos.split(",", 3)
print("lista_cursos split 3: ", lista_cursos)
print("tipo: ", type(lista_cursos))

cursos = "Python,Java,JavaScript,C#,C++,C,Ruby,PHP"
print("cursos: ", cursos)
lista_cursos = cursos.split(",", 5)
print("lista_cursos split 5: ", lista_cursos)
print("tipo: ", type(lista_cursos))

cursos = "Python,Java,JavaScript,C#,C++,C,Ruby,PHP"
print("cursos: ", cursos)
lista_cursos = cursos.split(",", 10)
print("lista_cursos split 10: ", lista_cursos)
print("tipo: ", type(lista_cursos))



