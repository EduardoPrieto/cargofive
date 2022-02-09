from django.db import models
from .validator import validate_file_extension

# Create your models here.
class Contracts(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    file = models.FileField(upload_to="cargo/", validators=[validate_file_extension])

    def __str__(self):
        return self.name

class Rates(models.Model):
    pol = models.CharField(max_length=100)
    pod = models.CharField(max_length=100)
    curr = models.CharField(max_length=10)
    twenty = models.CharField(max_length=10)
    forty = models.CharField(max_length=10)
    fortyhc = models.CharField(max_length=10)
    contract = models.ForeignKey(Contracts, on_delete=models.CASCADE)
