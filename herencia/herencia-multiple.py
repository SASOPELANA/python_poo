# Herencia múltiple en Python


class Telefono:
    def __init__(self):
        pass

    def llamar(self):
        print("llamando....")

    def ocupado(self):
        print("ocupado....")


class Camara:
    def __init__(self):
        pass

    def fotos(self):
        print("tomando fotos....")


class Reproduccion:
    def __init__(self):
        pass

    def reproduccirMusica(self):
        print("reproduciendo musica....")

    def reproduccirVideo(self):
        print("tomando fotos....")


# Método  __del__   -->  para liberar memoria
class Smarphone(Telefono, Camara, Reproduccion):
    def __del__(self):
        print("Telefono apagado....")


movil = Smarphone()
movil.llamar()
