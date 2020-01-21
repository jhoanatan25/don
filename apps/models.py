from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
#Clases o Tablas Independientes
from django.utils import timezone
from django.contrib.auth.models import BaseUserManager
from django.core.validators import MaxValueValidator
import json
# from .forms import MultiSelectFormField

class CustomUserManager(BaseUserManager):
	def _create_user(self, username, email, is_staff=False, is_superuser=False, password=None, is_dealer=False, **extra_fields):
		if not email:
			raise ValueError('Email needed')

		user = self.model(email=self.normalize_email(email),
		username=username,
		is_dealer=is_dealer,
		is_staff=is_staff,
		is_superuser=is_superuser,
		last_login=timezone.now(),
		**extra_fields)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_user(self, username, password, email, is_dealer=False, **extra_fields):
		return self._create_user(email=email,
		username=username,
		password=password,
		is_dealer=is_dealer,
		**extra_fields)

	def create_superuser(self, username, password, email, **extra_fields):
		return self._create_user(email=email,
		username=username,
		password=password,
		is_staff=True,
		is_superuser=True,
		**extra_fields)

class person(AbstractBaseUser, PermissionsMixin):
	username = models.CharField(max_length=80, primary_key=True)
	email = models.EmailField(unique=True)
	first_name = models.CharField(max_length=80, blank = True, null=True)
	last_name = models.CharField(max_length=80, blank = True, null=True)
	username = models.CharField(max_length=80, primary_key=True)
	anonymous = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	is_dealer = models.BooleanField(default=False)
	is_staff = models.BooleanField(default=False)
	image = models.ImageField(upload_to="users/", blank = True, null=True)
	logo = models.ImageField(upload_to="logo/", blank = True, null=True)
	phone = models.CharField(max_length=80, default='0')
	cell_phone = models.CharField(max_length=80, blank = True, null=True)
	objects = CustomUserManager()
	utheme = models.ForeignKey('theme', blank = True, null=True)
	address = models.CharField(max_length=160, blank = True, null=True)
	description = models.CharField(max_length=140, blank = True, null=True)
	facebook = models.CharField(max_length=140, default="#")
	instagram = models.CharField(max_length=140, default="#")
	twitter = models.CharField(max_length=140, default="#")
	pinterest = models.CharField(max_length=140, default="#")
	google = models.CharField(max_length=140, default="#")
	youtube = models.CharField(max_length=140, default="#")
	cars_to_sell = models.IntegerField(default=1)
	REQUIRED_FIELDS = ['email']
	USERNAME_FIELD = 'username'
	def get_short_name(self):
	 	return self.username
	def get_email(self):
		return self.email
	def __unicode__(self):
		return self.username
	def __str__(self):
		return self.username

class favourite(models.Model):
	user = models.ForeignKey(
        'person',
        on_delete=models.CASCADE,
    )
	car = models.ForeignKey(
        'car',
        on_delete=models.CASCADE,
    )
	def __unicode__(self):
		return self.user.username + " <3 " + self.car.__unicode__()
	def __str__(self):
		return self.user.username + " <3 " + self.car.__str__()

class theme(models.Model):
	name = models.CharField(max_length=15, unique=True)
	image = models.ImageField(upload_to="themes/", blank=True, null=True)
	number_of_cars = models.IntegerField(default=5)
	def __unicode__(self):
		return self.name
	def __str__(self):
		return self.name
class plans(models.Model):
	name = models.CharField(max_length=15)
	image = models.ImageField(upload_to="plans/")
	number_of_cars = models.IntegerField(unique = True)
	price = models.FloatField()
	def __unicode__(self):
		return self.name
	def __str__(self):
		return self.name
class Category(models.Model):
	name = models.CharField(max_length=200)
	def __unicode__(self):
		return self.name
	def __str__(self):
		return self.name

class blog_entry(models.Model):
	title = models.CharField(max_length=150)
	image = models.ImageField(upload_to="blog/", blank=True, null=True)
	content = models.TextField()
	category = models.ForeignKey(Category)
	published = models.BooleanField(default=True)
	created_at = models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
		return self.title
	def __str__(self):
		return self.title

class body_style(models.Model):
	description = models.CharField(max_length=80, unique=True)
	image = models.ImageField(upload_to="photos/")
	index = models.IntegerField(default=1)
	def __unicode__(self):
		return self.description
	def __str__(self):
		return self.description

class make(models.Model):
	description = models.CharField(max_length=80, unique=True)
	def __unicode__(self):
		return self.description
	def __str__(self):
		return self.description

class model(models.Model):
	description = models.CharField(max_length=80)
	maker = models.ForeignKey(
        'make',
        on_delete=models.CASCADE,
    )
	def __unicode__(self):
		return self.description
	def __str__(self):
		return self.description

class trim(models.Model):
	description = models.CharField(max_length=80)
	model = models.ForeignKey(
        'model',
        on_delete=models.CASCADE,
    )
	def __unicode__(self):
		return self.description
	def __str__(self):
		return self.description

class trim_year(models.Model):
	year = models.IntegerField()
	trim = models.ForeignKey(
        'trim',
        on_delete=models.CASCADE,
    )
	def __unicode__(self):
		return str(self.year) + "(" + self.trim.description + ")"
	def __str__(self):
		return str(self.year) + "(" + self.trim.description + ")"


class slide(models.Model):
	image = models.ImageField(upload_to="slide/")
	title_1 = models.CharField(max_length=80)
	title_2 = models.CharField(max_length=80)
	title_3 = models.CharField(max_length=80)
	url_1 = models.CharField(max_length=80, default = "#")
	url_2 = models.CharField(max_length=80, default = "#")
	url_3 = models.CharField(max_length=80, default = "#")
	def __unicode__(self):
		return self.title_1 + " " + self.title_2 + " " + self.title_3
	def __str__(self):
		return self.title_1 + " " + self.title_2 + " " + self.title_3

class transmission_type(models.Model):
	description = models.CharField(max_length=80, unique=True)
	def __unicode__(self):
		return self.description
	def __str__(self):
		return self.description

class drive_train(models.Model):
	description = models.CharField(max_length=80, unique=True)
	def __unicode__(self):
		return self.description
	def __str__(self):
		return self.description

class fuel_type(models.Model):
	description = models.CharField(max_length=80, unique=True)
	def __unicode__(self):
		return self.description
	def __str__(self):
		return self.description

class engine(models.Model):
	description = models.CharField(max_length=80, unique=True)
	def __unicode__(self):
		return self.description
	def __str__(self):
		return self.description

class drive(models.Model):
	description = models.CharField(max_length=80, unique=True)
	def __unicode__(self):
		return self.description
	def __str__(self):
		return self.description

class mImage(models.Model):
	image = models.ImageField(upload_to="photos/cars")
	rcar = models.ForeignKey(
        'car',
        on_delete=models.CASCADE,
    )
	def url(self):
		return self.image.url
	def __unicode__(self):
		return self.image.url + " - " + self.rcar.owner.username + " - " + self.rcar.model.description
	def __str__(self):
		return self.image.url + " - " + self.rcar.owner.username + " - " + self.rcar.model.description

class MultiSelectField(models.Field):
    foo = models.CharField(max_length=2000)
    def setfoo(self, x):
        self.foo = json.dumps(x)
    def getfoo(self, x):
        return json.loads(self.foo)

class car(models.Model):
	owner = models.ForeignKey(
        'person',
        on_delete=models.CASCADE,
    )
	year = models.IntegerField()
	body_s = models.ForeignKey('body_style', null=True, blank=True)
	model = models.ForeignKey('model')
	trim = models.CharField(max_length=80)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	transmission = models.ForeignKey('transmission_type')
	transmission_des = models.CharField(max_length=100, blank=True)
	drive_t = models.ForeignKey('drive_train')
	engine_des = models.CharField(max_length=100, blank=True)
	fuel_t = models.ForeignKey('fuel_type')
	city_MPG = models.CharField(max_length=100, default = "Santo Domingo")
	highway_MPG = models.CharField(max_length=100, blank=True)
	published = models.BooleanField(default=True)
	sold = models.BooleanField(default=False)
	conditions = (
        ('Nuevo', 'Nuevo'),
        ('Usado', 'Usado'),
        ('Certificado', 'Certificado'),
    )
	condition = models.CharField(
		max_length=100,
		choices=conditions
	)
	mileage = models.FloatField()
	lat = models.FloatField(default = 1)
	lon = models.FloatField(default = 1)
	price = models.IntegerField(validators=[MaxValueValidator(1000000)])
	off_price = models.IntegerField(null=True, blank=True, validators=[MaxValueValidator(500000)])
	stock_number = models.IntegerField(null=True, blank=True, default = 1, validators=[MaxValueValidator(1000)])
	engine_t = models.ForeignKey('engine')
	drive = models.ForeignKey('drive', null=True, blank=True)
	doors = (
        (2, 'Dos'),
        (3, 'Tres'),
        (4, 'Cuatro'),
		(5, 'Cinco'),
    )
	doors = models.IntegerField(choices=doors, null=True, blank=True)
	colors = (
		("Negro", "Negro"),
		("Azul", "Azul"),
		("Marrón", "Marrón"),
		("Dorado", "Dorado"),
		("Gris", "Gris"),
		("Verde", "Verde"),
		("Blanco oscuro", "Blanco oscuro"),
		("Rojo", "Rojo"),
		("Plateado", "Plateado"),
		("Blanco", "Blanco"),
		("Violeta", "Violeta"),
		("Naranja", "Naranja"),
		("Otro", "Otro"))
	exterior_color = models.CharField(max_length=20, choices=colors, blank=True)
	interior_color = models.CharField(max_length=20, choices=colors, blank=True)
	exterior_color_des = models.CharField(max_length=100, blank=True)
	interior_color_des = models.CharField(max_length=100, blank=True)
	interior_ops = (
        ('Tela', 'Tela'),
        ('Cuero', 'Cuero'),
        ('No aplica', 'No aplica'),
		('Otro', 'Otro'),
    )
	interior_fabric = models.CharField(
		max_length=100,
		choices=interior_ops,
		blank=True
	)
	comfort = models.CharField(max_length=2000, blank=True)
	entertainment = models.CharField(max_length=2000, blank=True)
	luxury = models.CharField(max_length=2000, blank=True)
	miscellaneous = models.CharField(max_length=2000, blank=True)
	def __unicode__(self):
		return self.owner.username  + ": " + self.model.maker.description + ": " + self.model.description
	def __str__(self):
		return self.owner.username  + ": " + self.model.maker.description + ": " + self.model.description
