# metodos
# def --> palabra reservada def para definir un metodo
# self --> representa el objeto que se esta creando


class Matematica:
    def suma(self):
        self.a = 10
        self.b = 15


s = Matematica()

s.suma()

print(s.a + s.b)
