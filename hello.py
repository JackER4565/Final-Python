"""
import django
django.VERSION
django-admin startproject Proyecto1
print("test")

python manage.py runserver




python manage.py startapp App   ---- crea una nueva aplicacion, luego de usar este comando hay que agregar la app en INSTALLED_APPS en el settings.py
python manage.py check App  ----- verifica la app si tiene errore

python manage.py makemigrations  ------- no se, viene antes de migrate, esto te crea el 0001

 python manage.py migrate   ----- impacta los modelos que hiciste en modelos.py
(Con ésto, esas líneas de sql impactan en nuestra base de datos)

python manage.py sqlmigrate App 0001   ------ guarda en el sql las nuevas columnas
(Eso nos dará muchas líneas en código sql)


from App.models import Curso ------- en una vista, usas esto para importar el modelo con los datos
 curso = Curso(nombre="Python", camada=23800)  ------ aca le decis que datos vas a guardar, tiene que coincidir con los datos en el modelos.py
curso.save()  ------ literalmente lo guarda en la base de datos.
"""