# Sistema de cobranza

## Imagenes Utilizadas:
- PostgreSQL
- Django

## Para ponerlo en marcha
- Generar el archivo **.env** basandose en **.env.example**
- Ejecutas **docker-compose up --build**
- Postgresql [demora en genrar la db ](https://github.com/docker-library/docs/blob/master/postgres/README.md#caveats) lo que hace que cuando django quiera conectarse no la va a encontrar, debes hacer un restart al contenedor **cobra_system** para que se conecte a la db ya creada.
- Luego entrar en **cobra_system** y ejecutar **python ./sistema_cobranza/manage.py migrate** para generar las tablas en la db
- Crear admin **python manage.py createsuperuser**

## Mini tutorial de DJANGO para generar un proyecto nuevo
- **django-admin startproject mysite** - Generar carpeta de proyecto
- **python manage.py runserver 0:80** - Correr servidor
- **python manage.py startapp polls** - Crear Apliación
- configurar setings.py en project
- agregar vistas en app
- configurar urls en project y app
- Configuro INSTALLED_APPS en config.py para que la migracion tenga en cuenta a la app
- **python manage.py migrate** - Genera migración de tablas por defecto
- Hacer el modelo
- **python manage.py makemigrations (nombre app)** - Genero los archivos de migración
- **python manage.py sqlmigrate (nombre app) 0001** - Reviso el sql generado
- **python manage.py migrate** - Aplico modelo
- **python manage.py createsuperuser**
- Toda la info de como hacer querys con el modelo: https://docs.djangoproject.com/es/3.2/ref/models/querysets/
- Info sobre usuarios de django https://docs.djangoproject.com/en/3.2/topics/auth/default/#authentication-in-web-requests
- Tutorial de DJANGO en video: https://youtube.com/playlist?list=PLEsfXFp6DpzTD1BD1aWNxS2Ep06vIkaeW