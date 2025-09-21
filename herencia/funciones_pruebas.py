# Herencia ejemplo practico en Python


class Calculadora:
    def __init__(self, num):
        self._num = num
        self._datos = [0 for x in range(num)]

    def ingresarDatos(self):
        self._datos = [
            int(input("Ingresar datos " + str(x + 1) + " = ")) for x in range(self._num)
        ]


class Op_basicas(Calculadora):
    def __init__(self):
        Calculadora.__init__(self, 2)

    def suma(self):
        a, b = self._datos
        return a + b

    def resta(self):
        a, b = self._datos
        return a - b


class Raiz(Calculadora):
    def __init__(self):
        Calculadora.__init__(self, 1)

    def raizCuadrada(self):
        import math

        (a,) = self._datos
        return math.sqrt(a)


op = Op_basicas()
op.ingresarDatos()
print(f"La suma es: {op.suma()}")


op2 = Raiz()
op2.ingresarDatos()
print(f"La raiz cuadrada es: {op2.raizCuadrada()}")
