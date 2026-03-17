from Excepciones.recetaNoExisteException import recetaNoExisteException

class Recetas():
    def __init__(self):
        self.recetas = []

    def agregar_receta(self, receta):
        receta.id = len(self.recetas) + 1
        self.recetas.append(receta)

    def mostrar_recetas(self):
        return self.recetas
    
    def eliminar_receta(self, nombre):
        try:
            encontre = False
            i = int(0)
            while(not encontre and i < len(self.recetas)):
                if self.recetas[i].nombre== nombre:
                    self.recetas.pop(i)
                encontre = True
            i += 1
        except recetaNoExisteException as e:
            print(e.mensaje)
         
    def recetasCoinciden(self, ingredientes: list[str]):
        recetasCoincidentes = []
        for receta in self.recetas:
            for ingrediente in ingredientes:
                if ingrediente in receta.ingredientes: 
                    recetasCoincidentes.append(receta)
        return recetasCoincidentes
                
           