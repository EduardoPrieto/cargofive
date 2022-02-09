# cargofive

Lo primero que tenemos que hacer para correr el proyecto es hacer las respectivas migraciones usando el comando 

`python manage.py makemigrations`

Después corremos las migraciones

`python manage.py migrate`

Las librerías usadas están contenidas en requeriments.txt

Una vez terminemos estos pasos podremos usar la orden 

`python manage.py runserver`

Y podremos ver el programa, en formularios podemos subir los archivos donde se hará todo el proceso de guardar en la base de datos
una vez guardados podemos ver los contratos creados en Contratos y si le damos click al botón de ver podremos ver el detalle del contrato.
En el botón comparar, tomará los últimos 2 registros y comparara los archivos mostrándonos una ayuda visual para entender mejor la diferencia entre los diferentes archivos

