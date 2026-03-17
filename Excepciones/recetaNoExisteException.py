class recetaNoExisteException(Exception):
    def __init__(self):
        self.mensaje = "La receta no existe"