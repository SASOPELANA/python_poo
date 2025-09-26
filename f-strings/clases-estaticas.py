# f-strings

class Estudiantes:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    def __repr__(self):
        return f"Hola soy {self._nombre} {self._apellido} y tengo {self._edad} años."


estudiante1 = Estudiantes('Juan', 'Luna', 22)

print(f"{estudiante1 !r}")
