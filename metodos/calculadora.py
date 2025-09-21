# metodos

class Calculadora:
    def __init__(self,num1=0,num2=0):
        self.suma = num1 + num2
        self.resta = num1 - num2
        self.producto = num1 * num2
        self.division = num1 / num2


operaciones = Calculadora(15,3)

print("Suma:",operaciones.suma)
print("Resta:",operaciones.resta)
print("Multiplicacion:",operaciones.producto)
print("Division:",operaciones.division)
