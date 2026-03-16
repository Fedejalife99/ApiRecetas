class Recetas():
    def __init__(self):
        self.recetas = []

    def agregar_receta(self, receta):
        self.recetas.append(receta)

    def mostrar_recetas(self):
        return self.recetas