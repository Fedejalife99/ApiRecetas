# 🍽️ Recetas API

A RESTful API built with **FastAPI** and **SQLite** for managing cooking recipes. Supports full CRUD operations, ingredient-based search, category filtering, image uploads, and a normalized relational database model.

---

## 🛠️ Tech Stack

- **Python 3.11+**
- **FastAPI** — web framework
- **SQLAlchemy** — ORM
- **SQLite** — database
- **Pydantic** — data validation
- **Uvicorn** — ASGI server

---

## 📁 Project Structure

```
recetas_api/
├── Api/
│   ├── gestionBd/
│   │   ├── database.py       # DB connection, session, Base
│   │   ├── models.py         # SQLAlchemy models
│   │   └── seed.py           # Initial data (20 recipes)
│   ├── main.py               # Endpoints
│   ├── Receta.py             # Pydantic schemas
│   └── middleware.py         # Global error handling
├── imagenes/                 # Uploaded recipe images
├── requirements.txt
└── README.md
```

---

## 🗄️ Database Model

The API uses a **many-to-many** relationship between recipes and ingredients through an association table that stores quantity and unit:

```
recetas ──< receta_ingrediente >── ingredientes
               ├── cantidad
               └── unidad
```

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/your-username/recetas_api.git
cd recetas_api
```

### 2. Create and activate virtual environment
```bash
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the seed to populate the database
```bash
python -m Api.gestionBd.seed
```

### 5. Start the server
```bash
uvicorn Api.main:app --reload
```

### 6. Open the interactive docs
```
http://localhost:8000/docs
```

---

## 📌 Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/recetas` | Get all recipes |
| GET | `/recetas/{id}` | Get recipe by ID |
| GET | `/recetas/limitadas?skip=0&limit=10` | Paginated recipes |
| GET | `/recetas/categoria/{categoria}` | Filter by category |
| GET | `/recetas/coincidentes?ingredientes=papa` | Search by ingredients |
| POST | `/recetas` | Create a recipe |
| PUT | `/recetas/{nombre}` | Update a recipe |
| DELETE | `/recetas/{nombre}` | Delete a recipe |
| POST | `/recetas/{id}/imagen` | Upload recipe image |

---

## 📂 Categories

`almuerzo` · `cena` · `desayuno` · `postre` · `entrada`

---

## ⚠️ Error Handling

All endpoints return a consistent error format:

```json
{
  "error": "Receta no encontrada",
  "status_code": 404,
  "path": "http://localhost:8000/recetas/99"
}
```

---

## 📄 License

MIT

---

# 🍽️ Recetas API (ES)

API REST desarrollada con **FastAPI** y **SQLite** para gestionar recetas de cocina. Soporta operaciones CRUD completas, búsqueda por ingredientes, filtrado por categoría, subida de imágenes y un modelo relacional normalizado.

---

## 🛠️ Stack tecnológico

- **Python 3.11+**
- **FastAPI** — framework web
- **SQLAlchemy** — ORM
- **SQLite** — base de datos
- **Pydantic** — validación de datos
- **Uvicorn** — servidor ASGI

---

## 📁 Estructura del proyecto

```
recetas_api/
├── Api/
│   ├── gestionBd/
│   │   ├── database.py       # Conexión, sesión y Base
│   │   ├── models.py         # Modelos SQLAlchemy
│   │   └── seed.py           # Datos iniciales (20 recetas)
│   ├── main.py               # Endpoints
│   ├── Receta.py             # Schemas Pydantic
│   └── middleware.py         # Manejo global de errores
├── imagenes/                 # Imágenes subidas
├── requirements.txt
└── README.md
```

---

## 🗄️ Modelo de base de datos

La API usa una relación **muchos a muchos** entre recetas e ingredientes a través de una tabla de asociación que almacena cantidad y unidad:

```
recetas ──< receta_ingrediente >── ingredientes
               ├── cantidad
               └── unidad
```

---

## 🚀 Cómo ejecutar

### 1. Clonar el repositorio
```bash
git clone https://github.com/tu-usuario/recetas_api.git
cd recetas_api
```

### 2. Crear y activar entorno virtual
```bash
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Poblar la base de datos
```bash
python -m Api.gestionBd.seed
```

### 5. Iniciar el servidor
```bash
uvicorn Api.main:app --reload
```

### 6. Abrir la documentación interactiva
```
http://localhost:8000/docs
```

---

## 📌 Endpoints

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/recetas` | Obtener todas las recetas |
| GET | `/recetas/{id}` | Obtener receta por ID |
| GET | `/recetas/limitadas?skip=0&limit=10` | Recetas paginadas |
| GET | `/recetas/categoria/{categoria}` | Filtrar por categoría |
| GET | `/recetas/coincidentes?ingredientes=papa` | Buscar por ingredientes |
| POST | `/recetas` | Crear una receta |
| PUT | `/recetas/{nombre}` | Actualizar una receta |
| DELETE | `/recetas/{nombre}` | Eliminar una receta |
| POST | `/recetas/{id}/imagen` | Subir imagen de receta |

---

## 📂 Categorías

`almuerzo` · `cena` · `desayuno` · `postre` · `entrada`

---

## ⚠️ Manejo de errores

Todos los endpoints devuelven un formato de error consistente:

```json
{
  "error": "Receta no encontrada",
  "status_code": 404,
  "path": "http://localhost:8000/recetas/99"
}
```

## 🤖 Asistencia de IA

Este proyecto fue desarrollado con la asistencia de Claude (Anthropic) como herramienta de aprendizaje.
Todo el código fue revisado, comprendido y adaptado por el autor.
El objetivo fue aprender FastAPI y SQLAlchemy, no solo generar código funcional.
---

## 📄 Licencia

MIT