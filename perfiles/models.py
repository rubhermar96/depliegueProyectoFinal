from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone


class PerfilManager(BaseUserManager):
    def create_user(self,email, username, nombre, apellidos, password = None):
        if not email:
            raise ValueError('El usuario debe tener un Email')
        usuario = self.model(
            username=username,
            email=self.normalize_email(email),
            nombre=nombre,
            apellidos=apellidos,
        )

        usuario.set_password(password)
        usuario.save()
        return usuario
    def create_superuser(self,username,email,nombre,apellidos,password):
        usuario = self.create_user(
            email=email,
            username=username,
            nombre=nombre,
            apellidos=apellidos,
            password=password,
        )
        usuario.usuario_administrador=True
        usuario.save()
        return usuario

class Perfil(AbstractBaseUser):
    username = models.CharField('Nombre de Usuario', unique=True, max_length=100,null=True)
    email = models.EmailField('Correo Electrónico', unique=True, max_length=100,null=True)
    nombre = models.CharField('Nombre', max_length=50, blank=True, null=True)
    apellidos = models.CharField('Apellidos', max_length=50, blank=True, null=True)
    foto = models.ImageField('Imagen de Perfil', upload_to='perfil/', height_field=None, width_field=None, max_length=None, blank=True, null=True)
    fecha_nacimiento = models.DateField('Fecha de Nacimiento', null=True, blank=True)
    telf_usuario = models.IntegerField('Número de Teléfono', null=True, blank=True)
    cvc = models.FileField('Curriculum', upload_to='cvcusuarios/',blank=True,null=True)
    usuario_activo = models.BooleanField(default=True)
    usuario_administrador = models.BooleanField(default=False)
    objects = PerfilManager()

    USERNAME_FIELD ='username'
    REQUIRED_FIELDS = ['email','nombre','apellidos']


    def __str__(self):
        return self.username
    def has_perm(self,perm):
        return True
    def has_module_perms(self, app_label):
        return True
    @property
    def is_staff(self):
        return self.usuario_administrador

class Oferta(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)
    author = models.ForeignKey('perfiles.Perfil', on_delete=models.CASCADE, null=True)
    experiencia = models.CharField(max_length=50, blank=True,null=True)
    tipo_contrato = models.CharField(max_length=50, blank=True, null=True)
    salario = models.IntegerField(blank=True,null=True)
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.titulo

class Candidatura(models.Model):
    nombre_candidatura = models.CharField(max_length=100,null=True)
    oferta = models.ForeignKey(Oferta, on_delete=models.CASCADE, null=True)
    candidato = models.ForeignKey('perfiles.Perfil', on_delete=models.CASCADE, null=True)
    published_date = models.DateTimeField(
        blank=True,null=True
    )
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.nombre_candidatura