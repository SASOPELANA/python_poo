# funciones y atributos


class Persona:
    edad = 33
    nombre = "Ricardo"
    alias = "Pepe"
    pais = "Argentina"


p1 = Persona()

print("Me llamo", p1.nombre, "y mi apodo es", p1.alias)

print("Mi edad es", getattr(p1, "edad"))

print("\n")

print("Ricardo tiene una edad?", hasattr(p1, "edad"))

print("\n")

print(p1.nombre)
setattr(p1, "nombre", "Juan")
print(p1.nombre)

print("\n")

print(p1.pais)
delattr(Persona, "pais")
print(hasattr(p1, "pais"))