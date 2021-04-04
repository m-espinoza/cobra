# Sistema de cobranza

Imagenes Utilizadas:
- mariaDB
- django
- fastAPI

## MiniTutorial de DJANGO
- **django-admin startproject mysite** - Generar carpeta de proyecto
- **python manage.py runserver 0:80** - Correr servidor
- **python manage.py startapp polls** - Crear Apliación
- configurar setings.py en project
- agregar vistas en app
- configurar urls en project y app
- Configuro INSTALLED_APPS en config.py para que la migracion tenga en cuenta a la app
- **python manage.py migrate** - Genera migración de tablas por defecto
- Hacer el modelo
- **python manage.py makemigrations polls** - Genero los archivos de migración
- **python manage.py sqlmigrate polls 0001** - Reviso el sql generado
- **python manage.py migrate** - Aplico modelo
- **python manage.py createsuperuser**