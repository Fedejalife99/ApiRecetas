import sys
import os
import json

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Api.gestionBd.database import engine, SessionLocal, Base
from Api.gestionBd.models import RecetaModel, IngredienteModel, RecetaIngrediente

Base.metadata.create_all(bind=engine)

RECETAS_SEED = [
    {
        "nombre": "Tortilla de papas",
        "categoria": "almuerzo",
        "ingredientes": [
            {"nombre": "papas", "cantidad": 4, "unidad": "unidades"},
            {"nombre": "huevos", "cantidad": 3, "unidad": "unidades"},
            {"nombre": "cebolla", "cantidad": 1, "unidad": "unidades"},
            {"nombre": "aceite de oliva", "cantidad": 3, "unidad": "cucharadas"},
            {"nombre": "sal", "cantidad": 1, "unidad": "pizca"},
        ],
        "pasos": [
            "Pelar y cortar las papas en rodajas finas.",
            "Pochar las papas y la cebolla en aceite a fuego medio durante 20 minutos.",
            "Batir los huevos con sal en un bol grande.",
            "Escurrir las papas y mezclarlas con el huevo batido.",
            "Calentar un poco de aceite en una sartén y volcar la mezcla.",
            "Cocinar 5 minutos, dar vuelta con un plato y cocinar 3 minutos más."
        ]
    },
    {
        "nombre": "Milanesas a la napolitana",
        "categoria": "almuerzo",
        "ingredientes": [
            {"nombre": "peceto", "cantidad": 500, "unidad": "gramos"},
            {"nombre": "huevos", "cantidad": 2, "unidad": "unidades"},
            {"nombre": "pan rallado", "cantidad": 1, "unidad": "taza"},
            {"nombre": "tomate", "cantidad": 2, "unidad": "unidades"},
            {"nombre": "jamón", "cantidad": 100, "unidad": "gramos"},
            {"nombre": "queso mozzarella", "cantidad": 200, "unidad": "gramos"},
            {"nombre": "sal", "cantidad": 1, "unidad": "pizca"},
            {"nombre": "aceite", "cantidad": 3, "unidad": "cucharadas"},
        ],
        "pasos": [
            "Salpimentar las milanesas y pasarlas por huevo batido.",
            "Empanarlas en pan rallado presionando bien.",
            "Freír en aceite caliente 3 minutos por lado hasta dorar.",
            "Colocar en una fuente, cubrir con rodajas de tomate, jamón y queso.",
            "Llevar al horno a 200°C hasta que el queso se derrita."
        ]
    },
    {
        "nombre": "Asado de tira",
        "categoria": "cena",
        "ingredientes": [
            {"nombre": "tira de asado", "cantidad": 1, "unidad": "kg"},
            {"nombre": "sal gruesa", "cantidad": 2, "unidad": "cucharadas"},
        ],
        "pasos": [
            "Encender el carbón y esperar que se forme brasa pareja.",
            "Colocar la carne con el hueso hacia abajo a altura media.",
            "Salar con sal gruesa y dejar cocinar 30 minutos sin tocar.",
            "Dar vuelta y cocinar del otro lado 20 minutos.",
            "Retirar y dejar reposar 5 minutos antes de servir."
        ]
    },
    {
        "nombre": "Empanadas de carne",
        "categoria": "entrada",
        "ingredientes": [
            {"nombre": "carne picada", "cantidad": 500, "unidad": "gramos"},
            {"nombre": "cebolla", "cantidad": 2, "unidad": "unidades"},
            {"nombre": "morrón rojo", "cantidad": 1, "unidad": "unidades"},
            {"nombre": "huevos", "cantidad": 2, "unidad": "unidades"},
            {"nombre": "aceitunas", "cantidad": 50, "unidad": "gramos"},
            {"nombre": "pimentón", "cantidad": 1, "unidad": "cucharadita"},
            {"nombre": "comino", "cantidad": 1, "unidad": "cucharadita"},
            {"nombre": "sal", "cantidad": 1, "unidad": "pizca"},
            {"nombre": "tapas de empanada", "cantidad": 12, "unidad": "unidades"},
        ],
        "pasos": [
            "Rehogar la cebolla y el morrón en aceite hasta tiernizar.",
            "Agregar la carne y cocinar 10 minutos, sazonar con pimentón y comino.",
            "Dejar enfriar y agregar huevo duro picado y aceitunas.",
            "Colocar una cucharada del relleno en cada tapa.",
            "Cerrar repulgando el borde y pintar con huevo.",
            "Hornear a 200°C por 20 minutos hasta dorar."
        ]
    },
    {
        "nombre": "Locro",
        "categoria": "almuerzo",
        "ingredientes": [
            {"nombre": "maíz blanco", "cantidad": 300, "unidad": "gramos"},
            {"nombre": "porotos", "cantidad": 200, "unidad": "gramos"},
            {"nombre": "carne de cerdo", "cantidad": 300, "unidad": "gramos"},
            {"nombre": "chorizo colorado", "cantidad": 2, "unidad": "unidades"},
            {"nombre": "panceta", "cantidad": 150, "unidad": "gramos"},
            {"nombre": "calabaza", "cantidad": 300, "unidad": "gramos"},
            {"nombre": "cebolla", "cantidad": 2, "unidad": "unidades"},
            {"nombre": "pimiento", "cantidad": 1, "unidad": "unidades"},
            {"nombre": "comino", "cantidad": 1, "unidad": "cucharadita"},
            {"nombre": "pimentón", "cantidad": 1, "unidad": "cucharadita"},
        ],
        "pasos": [
            "Remojar el maíz y los porotos la noche anterior.",
            "Cocinar el maíz y los porotos en agua durante 1 hora.",
            "Agregar las carnes y las verduras cortadas.",
            "Condimentar con comino y pimentón.",
            "Cocinar a fuego lento durante 2 horas revolviendo ocasionalmente.",
            "Servir caliente con salsa de cebolla de verdeo picante."
        ]
    },
    {
        "nombre": "Carbonada",
        "categoria": "almuerzo",
        "ingredientes": [
            {"nombre": "carne de ternera", "cantidad": 500, "unidad": "gramos"},
            {"nombre": "papas", "cantidad": 3, "unidad": "unidades"},
            {"nombre": "batata", "cantidad": 1, "unidad": "unidades"},
            {"nombre": "choclo", "cantidad": 2, "unidad": "unidades"},
            {"nombre": "durazno", "cantidad": 2, "unidad": "unidades"},
            {"nombre": "tomate", "cantidad": 2, "unidad": "unidades"},
            {"nombre": "cebolla", "cantidad": 1, "unidad": "unidades"},
            {"nombre": "caldo de carne", "cantidad": 500, "unidad": "ml"},
            {"nombre": "sal", "cantidad": 1, "unidad": "pizca"},
            {"nombre": "pimienta", "cantidad": 1, "unidad": "pizca"},
        ],
        "pasos": [
            "Dorar la carne en cubos en aceite caliente.",
            "Agregar la cebolla y el tomate picado, rehogar 5 minutos.",
            "Incorporar las papas, batatas y choclo en trozos.",
            "Cubrir con caldo y cocinar 30 minutos a fuego medio.",
            "Añadir los duraznos en mitades 10 minutos antes de terminar.",
            "Rectificar sal y pimienta y servir."
        ]
    },
    {
        "nombre": "Alfajores de maicena",
        "categoria": "postre",
        "ingredientes": [
            {"nombre": "maicena", "cantidad": 200, "unidad": "gramos"},
            {"nombre": "harina", "cantidad": 100, "unidad": "gramos"},
            {"nombre": "manteca", "cantidad": 150, "unidad": "gramos"},
            {"nombre": "azúcar impalpable", "cantidad": 100, "unidad": "gramos"},
            {"nombre": "yemas", "cantidad": 3, "unidad": "unidades"},
            {"nombre": "esencia de vainilla", "cantidad": 1, "unidad": "cucharadita"},
            {"nombre": "dulce de leche", "cantidad": 200, "unidad": "gramos"},
            {"nombre": "coco rallado", "cantidad": 50, "unidad": "gramos"},
        ],
        "pasos": [
            "Batir la manteca con el azúcar impalpable hasta cremar.",
            "Agregar las yemas y la vainilla, mezclar bien.",
            "Incorporar la maicena y la harina tamizadas hasta formar masa.",
            "Estirar la masa y cortar discos de 4 cm.",
            "Hornear a 160°C por 12 minutos, deben quedar blancos.",
            "Dejar enfriar, rellenar con dulce de leche y rebozar en coco."
        ]
    },
    {
        "nombre": "Dulce de leche casero",
        "categoria": "postre",
        "ingredientes": [
            {"nombre": "leche entera", "cantidad": 1, "unidad": "litro"},
            {"nombre": "azúcar", "cantidad": 300, "unidad": "gramos"},
            {"nombre": "bicarbonato de sodio", "cantidad": 1, "unidad": "pizca"},
            {"nombre": "esencia de vainilla", "cantidad": 1, "unidad": "cucharadita"},
        ],
        "pasos": [
            "Mezclar la leche con el azúcar y llevar a fuego medio.",
            "Agregar el bicarbonato de sodio y revolver.",
            "Cocinar a fuego bajo durante 1.5 a 2 horas revolviendo constantemente.",
            "Cuando espese y tome color caramelo, retirar del fuego.",
            "Agregar la vainilla y dejar enfriar antes de envasar."
        ]
    },
    {
        "nombre": "Humita en chala",
        "categoria": "entrada",
        "ingredientes": [
            {"nombre": "choclos", "cantidad": 6, "unidad": "unidades"},
            {"nombre": "cebolla", "cantidad": 1, "unidad": "unidades"},
            {"nombre": "morrón", "cantidad": 1, "unidad": "unidades"},
            {"nombre": "tomate", "cantidad": 2, "unidad": "unidades"},
            {"nombre": "queso mantecoso", "cantidad": 150, "unidad": "gramos"},
            {"nombre": "albahaca", "cantidad": 5, "unidad": "hojas"},
            {"nombre": "sal", "cantidad": 1, "unidad": "pizca"},
            {"nombre": "pimienta", "cantidad": 1, "unidad": "pizca"},
            {"nombre": "azúcar", "cantidad": 1, "unidad": "cucharadita"},
        ],
        "pasos": [
            "Desgranar los choclos rallándolos en un bol, reservar las chalas.",
            "Rehogar la cebolla y el morrón en aceite.",
            "Agregar el tomate picado y cocinar 5 minutos.",
            "Incorporar el choclo rallado y cocinar revolviendo 10 minutos.",
            "Añadir el queso en cubos y condimentar.",
            "Armar los paquetes con las chalas y cocinar al vapor 30 minutos."
        ]
    },
    {
        "nombre": "Chimichurri",
        "categoria": "entrada",
        "ingredientes": [
            {"nombre": "perejil", "cantidad": 1, "unidad": "taza"},
            {"nombre": "orégano", "cantidad": 2, "unidad": "cucharadas"},
            {"nombre": "ajo", "cantidad": 4, "unidad": "dientes"},
            {"nombre": "ají molido", "cantidad": 1, "unidad": "cucharadita"},
            {"nombre": "vinagre", "cantidad": 50, "unidad": "ml"},
            {"nombre": "aceite", "cantidad": 50, "unidad": "ml"},
            {"nombre": "sal", "cantidad": 1, "unidad": "pizca"},
            {"nombre": "pimentón", "cantidad": 1, "unidad": "cucharadita"},
        ],
        "pasos": [
            "Picar finamente el perejil y los ajos.",
            "Mezclar con el orégano, ají molido y pimentón.",
            "Incorporar el vinagre y el aceite en partes iguales.",
            "Salar a gusto y mezclar bien.",
            "Dejar reposar al menos 1 hora antes de usar.",
            "Conservar en frasco de vidrio en la heladera."
        ]
    },
    {
        "nombre": "Sopa de verduras",
        "categoria": "cena",
        "ingredientes": [
            {"nombre": "zanahoria", "cantidad": 2, "unidad": "unidades"},
            {"nombre": "apio", "cantidad": 2, "unidad": "ramas"},
            {"nombre": "papas", "cantidad": 2, "unidad": "unidades"},
            {"nombre": "zapallo", "cantidad": 200, "unidad": "gramos"},
            {"nombre": "puerro", "cantidad": 1, "unidad": "unidades"},
            {"nombre": "caldo de verduras", "cantidad": 1, "unidad": "litro"},
            {"nombre": "sal", "cantidad": 1, "unidad": "pizca"},
            {"nombre": "pimienta", "cantidad": 1, "unidad": "pizca"},
        ],
        "pasos": [
            "Cortar todas las verduras en cubos medianos.",
            "Rehogar el puerro en aceite hasta transparentar.",
            "Agregar el resto de las verduras y el caldo.",
            "Cocinar a fuego medio durante 25 minutos.",
            "Salpimentar y servir caliente.",
            "Opcionalmente mixear la mitad para dar cremosidad."
        ]
    },
    {
        "nombre": "Tarta de choclo",
        "categoria": "almuerzo",
        "ingredientes": [
            {"nombre": "choclo cremoso", "cantidad": 400, "unidad": "gramos"},
            {"nombre": "queso crema", "cantidad": 200, "unidad": "gramos"},
            {"nombre": "queso rallado", "cantidad": 100, "unidad": "gramos"},
            {"nombre": "huevos", "cantidad": 3, "unidad": "unidades"},
            {"nombre": "tapas de tarta", "cantidad": 1, "unidad": "unidades"},
            {"nombre": "sal", "cantidad": 1, "unidad": "pizca"},
            {"nombre": "pimienta", "cantidad": 1, "unidad": "pizca"},
        ],
        "pasos": [
            "Precalentar el horno a 180°C.",
            "Mezclar el choclo con el queso crema, queso rallado y huevos.",
            "Salpimentar la mezcla.",
            "Colocar la tapa en el molde y volcar el relleno.",
            "Hornear 35 minutos hasta que el relleno esté firme y dorado."
        ]
    },
    {
        "nombre": "Arroz con leche",
        "categoria": "postre",
        "ingredientes": [
            {"nombre": "arroz", "cantidad": 200, "unidad": "gramos"},
            {"nombre": "leche entera", "cantidad": 1, "unidad": "litro"},
            {"nombre": "azúcar", "cantidad": 150, "unidad": "gramos"},
            {"nombre": "canela en rama", "cantidad": 1, "unidad": "unidades"},
            {"nombre": "cáscara de limón", "cantidad": 1, "unidad": "unidades"},
            {"nombre": "canela molida", "cantidad": 1, "unidad": "cucharadita"},
        ],
        "pasos": [
            "Hervir la leche con la canela en rama y la cáscara de limón.",
            "Agregar el arroz y cocinar a fuego bajo revolviendo frecuentemente.",
            "Incorporar el azúcar y continuar cocinando 20 minutos.",
            "Retirar la canela y la cáscara de limón.",
            "Servir en copas y espolvorear con canela molida.",
            "Dejar enfriar y refrigerar antes de servir."
        ]
    },
    {
        "nombre": "Pizza de mozzarella",
        "categoria": "cena",
        "ingredientes": [
            {"nombre": "harina", "cantidad": 500, "unidad": "gramos"},
            {"nombre": "levadura", "cantidad": 10, "unidad": "gramos"},
            {"nombre": "agua", "cantidad": 300, "unidad": "ml"},
            {"nombre": "sal", "cantidad": 1, "unidad": "cucharadita"},
            {"nombre": "aceite de oliva", "cantidad": 2, "unidad": "cucharadas"},
            {"nombre": "salsa de tomate", "cantidad": 200, "unidad": "ml"},
            {"nombre": "queso mozzarella", "cantidad": 300, "unidad": "gramos"},
            {"nombre": "orégano", "cantidad": 1, "unidad": "cucharadita"},
        ],
        "pasos": [
            "Disolver la levadura en agua tibia con una pizca de azúcar.",
            "Mezclar la harina con sal, agregar el agua y el aceite.",
            "Amasar 10 minutos hasta obtener masa lisa, dejar levar 1 hora.",
            "Estirar la masa en la pizzera aceitada.",
            "Cubrir con salsa de tomate y mozzarella en rodajas.",
            "Hornear a 220°C por 15 minutos y agregar orégano al servir."
        ]
    },
    {
        "nombre": "Guiso de lentejas",
        "categoria": "cena",
        "ingredientes": [
            {"nombre": "lentejas", "cantidad": 300, "unidad": "gramos"},
            {"nombre": "chorizo", "cantidad": 2, "unidad": "unidades"},
            {"nombre": "zanahoria", "cantidad": 2, "unidad": "unidades"},
            {"nombre": "papas", "cantidad": 2, "unidad": "unidades"},
            {"nombre": "tomate", "cantidad": 2, "unidad": "unidades"},
            {"nombre": "cebolla", "cantidad": 1, "unidad": "unidades"},
            {"nombre": "pimiento", "cantidad": 1, "unidad": "unidades"},
            {"nombre": "comino", "cantidad": 1, "unidad": "cucharadita"},
            {"nombre": "pimentón", "cantidad": 1, "unidad": "cucharadita"},
            {"nombre": "caldo", "cantidad": 500, "unidad": "ml"},
        ],
        "pasos": [
            "Remojar las lentejas en agua fría durante 2 horas.",
            "Rehogar el chorizo cortado en rodajas hasta dorar.",
            "Agregar la cebolla, el pimiento y el tomate picado.",
            "Incorporar las lentejas escurridas, la zanahoria y la papa en cubos.",
            "Cubrir con caldo y condimentar con comino y pimentón.",
            "Cocinar a fuego bajo 40 minutos hasta que todo esté tierno."
        ]
    },
    {
        "nombre": "Revuelto gramajo",
        "categoria": "almuerzo",
        "ingredientes": [
            {"nombre": "papas", "cantidad": 3, "unidad": "unidades"},
            {"nombre": "jamón", "cantidad": 150, "unidad": "gramos"},
            {"nombre": "huevos", "cantidad": 4, "unidad": "unidades"},
            {"nombre": "arvejas", "cantidad": 100, "unidad": "gramos"},
            {"nombre": "aceite", "cantidad": 3, "unidad": "cucharadas"},
            {"nombre": "sal", "cantidad": 1, "unidad": "pizca"},
            {"nombre": "pimienta", "cantidad": 1, "unidad": "pizca"},
        ],
        "pasos": [
            "Cortar las papas en juliana fina y freír en aceite caliente hasta crocantes.",
            "Escurrir las papas sobre papel absorbente.",
            "En la misma sartén, saltear el jamón en tiras.",
            "Agregar las arvejas y las papas.",
            "Volcar los huevos batidos y revolver hasta integrar.",
            "Salpimentar y servir de inmediato."
        ]
    },
    {
        "nombre": "Matambre a la pizza",
        "categoria": "cena",
        "ingredientes": [
            {"nombre": "matambre", "cantidad": 1, "unidad": "kg"},
            {"nombre": "salsa de tomate", "cantidad": 200, "unidad": "ml"},
            {"nombre": "queso mozzarella", "cantidad": 300, "unidad": "gramos"},
            {"nombre": "orégano", "cantidad": 1, "unidad": "cucharadita"},
            {"nombre": "sal", "cantidad": 1, "unidad": "pizca"},
            {"nombre": "pimienta", "cantidad": 1, "unidad": "pizca"},
        ],
        "pasos": [
            "Salpimentar el matambre por ambos lados.",
            "Cocinar a la plancha o parrilla 15 minutos por lado.",
            "Cubrir la superficie con salsa de tomate.",
            "Agregar el queso mozzarella en rodajas.",
            "Llevar al horno o tapar hasta que el queso se derrita.",
            "Espolvorear orégano y cortar en porciones."
        ]
    },
    {
        "nombre": "Budín de pan",
        "categoria": "postre",
        "ingredientes": [
            {"nombre": "pan lactal", "cantidad": 200, "unidad": "gramos"},
            {"nombre": "leche entera", "cantidad": 500, "unidad": "ml"},
            {"nombre": "huevos", "cantidad": 3, "unidad": "unidades"},
            {"nombre": "azúcar", "cantidad": 150, "unidad": "gramos"},
            {"nombre": "esencia de vainilla", "cantidad": 1, "unidad": "cucharadita"},
            {"nombre": "pasas de uva", "cantidad": 50, "unidad": "gramos"},
            {"nombre": "caramelo", "cantidad": 100, "unidad": "ml"},
        ],
        "pasos": [
            "Remojar el pan en la leche hasta que absorba bien.",
            "Batir los huevos con el azúcar y la vainilla.",
            "Mezclar el pan remojado con los huevos y las pasas.",
            "Preparar caramelo y cubrir el molde.",
            "Volcar la mezcla y cocinar a baño maría en horno a 180°C por 45 minutos.",
            "Dejar enfriar, desmoldar y refrigerar."
        ]
    },
    {
        "nombre": "Cazuela de pollo",
        "categoria": "cena",
        "ingredientes": [
            {"nombre": "pollo", "cantidad": 1, "unidad": "kg"},
            {"nombre": "papas", "cantidad": 3, "unidad": "unidades"},
            {"nombre": "zanahoria", "cantidad": 2, "unidad": "unidades"},
            {"nombre": "cebolla", "cantidad": 1, "unidad": "unidades"},
            {"nombre": "pimiento", "cantidad": 1, "unidad": "unidades"},
            {"nombre": "tomate", "cantidad": 2, "unidad": "unidades"},
            {"nombre": "caldo de pollo", "cantidad": 500, "unidad": "ml"},
            {"nombre": "laurel", "cantidad": 2, "unidad": "hojas"},
            {"nombre": "sal", "cantidad": 1, "unidad": "pizca"},
            {"nombre": "pimienta", "cantidad": 1, "unidad": "pizca"},
        ],
        "pasos": [
            "Sellar los trozos de pollo en aceite caliente por todos lados.",
            "Retirar el pollo y rehogar la cebolla y el pimiento.",
            "Agregar el tomate picado y cocinar 5 minutos.",
            "Incorporar el pollo, las papas y zanahorias en cubos.",
            "Cubrir con caldo, agregar el laurel y salpimentar.",
            "Cocinar tapado a fuego medio 35 minutos."
        ]
    },
    {
        "nombre": "Panqueques con dulce de leche",
        "categoria": "desayuno",
        "ingredientes": [
            {"nombre": "harina", "cantidad": 200, "unidad": "gramos"},
            {"nombre": "huevos", "cantidad": 2, "unidad": "unidades"},
            {"nombre": "leche entera", "cantidad": 300, "unidad": "ml"},
            {"nombre": "manteca", "cantidad": 50, "unidad": "gramos"},
            {"nombre": "azúcar", "cantidad": 2, "unidad": "cucharadas"},
            {"nombre": "sal", "cantidad": 1, "unidad": "pizca"},
            {"nombre": "dulce de leche", "cantidad": 200, "unidad": "gramos"},
        ],
        "pasos": [
            "Mezclar la harina, el azúcar y la sal en un bol.",
            "Agregar los huevos y la leche de a poco, batiendo sin grumos.",
            "Incorporar la manteca derretida y dejar reposar 15 minutos.",
            "Calentar una sartén antiadherente con un poco de manteca.",
            "Volcar un cucharón de mezcla, cocinar 1 minuto por lado.",
            "Rellenar con dulce de leche, enrollar y servir."
        ]
    },
]


def seed():
    db = SessionLocal()
    try:
        existing = db.query(RecetaModel).count()
        if existing > 0:
            print(f"La base ya tiene {existing} recetas. Omitiendo seed.")
            return

        for data in RECETAS_SEED:
            # 1. crear la receta
            receta = RecetaModel(
                nombre=data["nombre"],
                categoria=data["categoria"],
                pasos=json.dumps(data["pasos"], ensure_ascii=False),
            )
            db.add(receta)
            db.flush()  # genera el id de la receta sin hacer commit

            # 2. crear o reutilizar cada ingrediente y asociarlo
            for ing_data in data["ingredientes"]:
                # buscar si el ingrediente ya existe
                ingrediente = db.query(IngredienteModel).filter(
                    IngredienteModel.nombre == ing_data["nombre"]
                ).first()

                # si no existe, crearlo
                if not ingrediente:
                    ingrediente = IngredienteModel(nombre=ing_data["nombre"])
                    db.add(ingrediente)
                    db.flush()  # genera el id del ingrediente

                # 3. crear la asociacion con cantidad y unidad
                asociacion = RecetaIngrediente(
                    receta_id=receta.id,       # ← id de la receta
                    ingrediente_id=ingrediente.id,  # ← id del ingrediente
                    cantidad=ing_data["cantidad"],
                    unidad=ing_data["unidad"],
                )
                db.add(asociacion)

        db.commit()
        print(f"✅ Se insertaron {len(RECETAS_SEED)} recetas exitosamente.")
    except Exception as e:
        db.rollback()
        import traceback
        traceback.print_exc()
        print(f"❌ Error al insertar recetas: {e}")
    finally:
        db.close()


if __name__ == "__main__":
    seed()