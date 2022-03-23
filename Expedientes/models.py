import os

from django.db import models


# Create your models here.
def content_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s_%s_%s.%s" % (instance.numExpediente, instance.nombre, instance.fechaApertura, ext)
    return os.path.join('uploads', filename)


class registroExpediente(models.Model):
    SEXO=[("F","Femenino"),("M","Masculino")]
    numNue = models.IntegerField(primary_key=True)
    numNut = models.IntegerField()
    numExpediente = models.IntegerField()
    fechaApertura = models.DateField()
    nombre = models.CharField(max_length=150)
    sexo = models.CharField(
        max_length=1,
        choices=SEXO,
        default="F",)
    nacionalidad = models.CharField(max_length=30)
    fechaNacimiento = models.DateField()
    expedientePDF = models.FileField(null=True,default=None, upload_to=content_file_name)