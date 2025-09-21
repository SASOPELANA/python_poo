#metodos
#def --> palabra reservada def para definir un metodo
#self --> representa el objeto que se esta creando
# __init__ --> metodo constructor en python

class Ropa:
    def __init__(self):
        self.marca = "Lacoste"
        self.talla = "XL"
        self.color = "Verde"


camisa  = Ropa()

print(camisa.marca)
print(camisa.talla)
print(camisa.color)