import os
from django.core.exceptions import ValidationError

#Valida el campo files, este debe cumplir con unos criterios de extensiones soportadas
#En el FrontEnd hay una validación pero puede ser burlada por lo que se añade esta también
def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.xlsx', '.xls']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')