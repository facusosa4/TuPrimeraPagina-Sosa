# Blog de Películas 🎬

Este es mi primera página web hecha con Django. Es una página estilo blog donde se pueden cargar películas, directores y críticas, y también hacer búsquedas por título.
Forma parte de la tercera entrega del curso de programación en CoderHouse

---

## ¿Qué se puede hacer?

- Cargar una nueva película.
- Cargar un director.
- Cargar una crítica.
- Buscar películas por su título.

---

## ¿En qué orden se prueba?

1. Primero se cargan los directores.
2. Después se cargan las películas .
3. Después se pueden cargar críticas.
4. Por último, se puede usar la búsqueda.

---

## ¿Cómo se usa?

1. Abrir el proyecto en VS Code.
2. Activar el entorno virtual.
3. En la terminal, correr estas líneas:

python manage.py makemigrations  
python manage.py migrate  
python manage.py runserver

4. Ir al navegador y entrar a:

http://localhost:8000/

Desde ahí podés acceder a:

- /crear_director/ → para cargar directores
- /crear_pelicula/ → para cargar películas
- /crear_critica/ → para cargar críticas
- /buscar_pelicula/ → para buscar películas por nombre

---

## Estructura de carpetas importante

Las plantillas están organizadas así:

peliculas/  
├── templates/  
│   ├── base.html  
│   └── peliculas/  
│       ├── crear_pelicula.html  
│       ├── crear_director.html  
│       ├── crear_critica.html  
│       └── buscar_pelicula.html

---

## Notas

- Uso herencia de plantillas con base.html.
- Todos los formularios usan {% csrf_token %}.
- La búsqueda se hace con coincidencia parcial del título (icontains).

---

Facundo Sosa – 2025