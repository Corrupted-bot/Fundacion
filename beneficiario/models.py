from django.db import models
from django.contrib.auth.models import AbstractUser
import os
from django.conf import settings
# Create your models here.
class Usuario(AbstractUser):
    nombre = models.CharField(max_length=30)

class Solicitud(models.Model):
    nombre = models.CharField(max_length=60)
    rut = models.CharField(max_length=12)
    solicitudes = models.Manager()
    telefono = models.CharField(max_length=12)
    email = models.EmailField(max_length=50)
    imagen=models.FileField(upload_to='imagenes',blank=True, null=True)
    estado = models.BooleanField(default=False)

    def __sts__(self):
        return self.nombre
    def delete(self, *args, **kwargs):
        if(self.imagen):
            os.remove(os.path.join(settings.MEDIA_ROOT, self.imagen.name))
        super(Solicitud,self).delete(*args,**kwargs)
    
class SolicitudFacade:
    def __init__(self):
        self.solicitudes_beneficiarios = Solicitud.solicitudes
    def buscarSolicitudes(self):
        return self.solicitudes_beneficiarios.all()
    def buscarSolicitud(self,id):
        return self.solicitudes_beneficiarios.get(id=id)



