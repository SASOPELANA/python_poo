# metodo constructor


class Persona:
    pass

    def __init__(self, _nombre, _anio):
        self._nombre = _nombre
        self._anio = _anio

    def descripcion(self):
        return "{} tiene {} años.".format(self._nombre, self._anio)

    def comentario(self, frase):
        return "{} dice {}".format(self._nombre, frase)


doctor = Persona("Juan", 33)

print(doctor.descripcion())
print(doctor.comentario("Hola como esta?"))
