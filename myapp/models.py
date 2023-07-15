from typing import Optional
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.

class create_nuevo_curso(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_curso = models.CharField(max_length=100)
    img_curso =  models.ImageField(upload_to="img/cursos" ,null=True, blank=True)
    form_carga_curso = models.FileField(upload_to="documents", null=True, blank=True)
    descrip_corta_curso = models.CharField(max_length=250)
    descrip_larga_curso = models.CharField(max_length=600)
    requisitos_curso = models.CharField(max_length=100)
    time_start_curso = models.DateField() 
    time_end_curso = models.DateField() 
    servicio_curso = models.CharField(max_length=100)
    hospital_curso = models.CharField(max_length=100)
    personal_cursos = models.CharField(max_length=80)
    activo = models.BooleanField(default=True)

class create_nuevo_card(models.Model):
    id = models.AutoField(primary_key=True)
    img_card =  models.ImageField(upload_to="img/carta",null=True, blank=True)
    nombre_card = models.CharField(max_length=25)
    cargo_card = models.CharField(max_length=100)
    descrip_card = models.CharField(max_length=100)

class create_nuevo_publicacion(models.Model):
    id = models.AutoField(primary_key=True)
    img_pub = models.ImageField(upload_to="img/public" ,null=True, blank=True)
    nombre_pub = models.CharField(max_length=100)
    descrip_pub = models.CharField(max_length=100, default='SOME STRING')
    is_curso = models.BooleanField(default=False)
    is_curso_id = models.IntegerField(null=True,default=None)

class create_new_consultas(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_completo = models.CharField(max_length=100)
    rut = models.IntegerField()
    telefono = models.IntegerField()
    Correo = models.CharField(max_length=100)

class new_class_hospital(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_hospital = models.CharField(max_length=70)

class new_class_servicio(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_sev = models.CharField(max_length=50)


class create_new_consultas_respondidas(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_completo = models.CharField(max_length=70)
    rut = models.IntegerField()
    telefono = models.IntegerField()
    Correo = models.CharField(max_length=100)
    fecha_respuesta = models.DateTimeField()    


class UsuarioManager(BaseUserManager):
    def create_user(self, email, username, nombres, celular, password=None):
        if not email:
            raise ValueError('El usuario debe tener un correo electrónico')
        
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            nombres=nombres,
            celular=celular,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username, nombres, celular, password):
        user = self.create_user(
            email=email,
            username=username,
            nombres=nombres,
            celular=celular,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Usuario(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    celular = models.IntegerField()
    nombres = models.CharField(max_length=255 ,default='')
    username = models.CharField(max_length=150, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'nombres', 'celular']

    objects = UsuarioManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, app_label):
        return self.is_staff
    
    def set_password(self, raw_password):
        # Encriptar la contraseña utilizando el método de la clase base
        super().set_password(raw_password)

    class Meta:
        db_table = 'mi_tabla_usuario'



        