# metodo contructor
# modificar atributos


class Email:
    def __init__(self):
        self.enviado = False

    def enviarCorreo(self):
        self.enviado = True


mi_correo = Email()

print(mi_correo.enviado)

mi_correo.enviarCorreo()
print(mi_correo.enviado)
