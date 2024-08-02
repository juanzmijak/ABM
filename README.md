**ABM API 🚀**

Esta es una API REST para gestionar usuarios, construida con FastAPI y SQLite.

**Requisitos 🛠️**

Python 3.8+

Docker (para ejecutar en contenedor)


**Instalación 💻**

**Clonar el repositorio**

bash <>

git clone https://github.com/juanzmijak/ABM

cd abm

**Crear y activar el entorno virtual**

bash <>

python3 -m venv venv

source venv/bin/activate  # En macOS/Linux

.\venv\Scripts\activate  # En Windows

**Instalar las dependencias**

bash <>

pip install -r requirements.txt

**Inicializar la base de datos**

bash <>

python app/models.py

**Ejecutar la aplicación**

bash <>


uvicorn app.main:app --reload

**Endpoints 📡**

**Crear un nuevo usuario**

Endpoint: POST /users/

Descripción: Crea un nuevo usuario.

Ejemplo de solicitud (usando cURL):

bash <>

curl -X POST "http://127.0.0.1:8000/users/" -H "accept: application/json" -H "Content-Type: application/json" -H "access_token: mysecretapikey" -d '{ "nombre": "Juan", "apellido": "Zmijak", "direccion": "Av Libertador 1234", "telefono": "+1234567890", "edad": 28 }'

**Obtener usuarios por nombre**

Endpoint: GET /users/

Descripción: Busca usuarios por nombre.

Ejemplo de solicitud (usando cURL):

bash <>

curl -X GET "http://127.0.0.1:8000/users/?nombre=Juan" -H "accept: application/json" -H "access_token: mysecretapikey"

**Obtener un usuario por ID**

Endpoint: GET /users/{user_id}

Descripción: Obtiene un usuario por ID.

Ejemplo de solicitud (usando cURL):

bash <>

curl -X GET "http://127.0.0.1:8000/users/1" -H "accept: application/json" -H "access_token: mysecretapikey"
Actualizar un usuario

Endpoint: PUT /users/{user_id}

Descripción: Actualiza un usuario existente.

Ejemplo de solicitud (usando cURL):

bash <>

curl -X PUT "http://127.0.0.1:8000/users/1" -H "accept: application/json" -H "Content-Type: application/json" -H "access_token: mysecretapikey" -d '{ "nombre": "Juan", "apellido": "Zmijak", "direccion": "Av Libertador 1234", "telefono": "+1234567890", "edad": 28 }'

**Eliminar un usuario**

Endpoint: DELETE /users/{user_id}
Descripción: Elimina un usuario por ID.

Ejemplo de solicitud (usando cURL):

bash <>

curl -X DELETE "http://127.0.0.1:8000/users/1" -H "accept: application/json" -H "access_token: mysecretapikey"

**Ejecución en Docker 🐳**

**Construir la imagen de Docker:**

bash <>

docker build -t abm .

**Ejecutar el contenedor:**

bash <>

docker run -d -p 8000:8000 abm

La API estará disponible en http://127.0.0.1:8000.

**Nuevas funcionalidades a futuro 🌟**

- Pagos y facturación de usuarios.

- Integración con servicios de mensajería y notificaciones a los usuarios sobre pagos y facturación.

- Generación de informes y estadísticas de usuarios.

**Recomendaciones de seguridad 🔒**

- Usar HTTPS en producción.

- Implementar límites de requests para proteger contra ataques de fuerza bruta.
- Monitoreo y alertas de seguridad críticas sobre acciones inusuales de usuarios.
  
