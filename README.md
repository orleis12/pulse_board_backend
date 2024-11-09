# Proyecto Backend - Django

Este es el backend del proyecto utilizando Django y Django Rest Framework. El propósito de este proyecto es proporcionar una API RESTful para manejar el manejo de usuarios y registros.

## Requisitos previos

Asegúrate de tener instalados los siguientes programas:

- [Python 3.x](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/)

## Pasos para ejecutar el proyecto

Primero, clona el repositorio de GitHub en tu máquina local. Abre la terminal (cmd o bash) y ejecuta el siguiente comando:

```bash
git clone https://github.com/usuario/nombre-del-repositorio.git
cd nombre-del-repositorio


Asegúrate de estar en el directorio del proyecto y crea un entorno virtual. Ejecuta el siguiente comando en la terminal:
## python -m venv venv

Activa el entorno virtual ejecutando:
## venv\Scripts\activate

Instala las dependencias necesarias para el proyecto. Puedes hacerlo manualmente con los siguientes comandos:

pip install django
pip install djangorestframework
pip install djangorestframework-simplejwt
pip install django-cors-headers
pip install Pillow

Ejecutamos las migraciones
## python manage.py migrate

Ejecutamos el proyecto con el comando
## python manage.py runserver
El servidor debería estar corriendo en http://127.0.0.1:8000/.

Ahora ya se puede utilizar la api Django y puedes correr el proyecto en el Front end.

### Para iniciar sesión
Entras ala url
Administrador: http://127.0.0.1:8000/api/v2/
te va pedir las credenciales.

Cuenta Administrador
username": admin,
password": Admin123456

Luego terminar presiamos "Crtl + s" y luego para desactivar el entorno virtual colocamos el comando
## deactivate

y finalmente ya podrias cerrar el proyecto.


#####################################################################


OTROS EN CASO DE PROBLEMAS CON LA BD
## Creación Automática de Usuarios

En el proyecto, existe un archivo `dataUser.json` que contiene los datos de los usuarios que deben ser creados en el sistema. Si este archivo no existe o se borra accidentalmente, puedes volver a generar los usuarios mediante un endpoint de la API.

### Paso 1: Verificar la existencia de `dataUser.json`

El archivo `dataUser.json` se encuentra en la raíz del proyecto. Este archivo debe contener un array de objetos con la información de los usuarios, por ejemplo:

```json
[
  {
    "username": "usuario1",
    "email": "usuario1@example.com",
    "password": "password123"
  },
  {
    "username": "usuario2",
    "email": "usuario2@example.com",
    "password": "password123"
  }
]

Para crear la base de datos db.sqlite3

Activamos el entorno virtual
## venv\Scripts\activate

luego migramos y que salga todo ok, se creará la BD
## python manage.py migrate

Creamos el superusuario
## python manage.py createsuperuser

"username": "admin",
"email": "admin@example.com",
"password": "Admin123456",

Ejecutamos el proyecto nuevamente
## python manage.py runserver


Y entramos a la Url
http://127.0.0.1:8000/api/v2/create-multiple-users-with-activity/

Copiamos el codigo del Archivo dataUser.json, lo pegamos en la pagina, le damos al boton "Post" y verificamos que se hayan creado exitosamente los usuarios.


