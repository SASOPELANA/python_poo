# Herencia en Python

# Clase padre
class Pokemon:
    pass

    def __init__(self, nombre, tipo):
        self._nombre = nombre
        self._tipo = tipo

    def descripcion(self):
        return "{} es un Pokemon de tipo {}".format(self._nombre, self._tipo)


# Clase hija --> Herencia en Python
class Pikachu(Pokemon):
    def ataque(self, tipoAtaque):
        return "{} tipo de ataque: {}".format(self._nombre, tipoAtaque)


# Clase hija --> Herencia en Python
class Charmander(Pokemon):
    def ataque(self, tipoAtaque):
        return "{} tipo de ataque: {}".format(self._nombre, tipoAtaque)


pokemon1 = Pikachu("Domador", "electrico")
print(pokemon1.descripcion())

print(pokemon1.ataque("impacto trueno"))
