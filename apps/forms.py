from django import forms
from .models import person, body_style, make, transmission_type, drive_train, fuel_type, engine, drive, car, model, slide, plans

class userForm(forms.ModelForm):
	class Meta:
		model = person
		fields = [
			'username',
			'email',
			'password',
			# 'phone',
			# 'image',
		]
		labels= {
			'username': 'Username',
			'email': 'Email',
			'password': 'Password',
			# 'phone': 'Phone',
			# 'image': 'Image',
		}

		widget = {
			'user': forms.TextInput(attrs={'class':'form-control'}),
			'email': forms.TextInput(attrs={'class':'form-control'}),
			'password': forms.TextInput(attrs={'class':'form-control'}),
			'userid': forms.HiddenInput(attrs={'class':'form-control'}),
			# 'phone': forms.TextInput(attrs={'class':'form-control'}),
			# 'image': forms.ImageField(),
		}
class newPlanForm(forms.ModelForm):
	class Meta:
		model = plans
		fields = [
			'name',
			'image',
			'number_of_cars',
			'price',
		]
		labels= {
			'name': 'Nombre del plan',
			'image': 'Imagen asociada',
			'number_of_cars': 'Número máximo de carros',
			'price': 'Precio del plan',
		}
		error_messages = {
			'number_of_cars': {
				'unique': "Ya hay otro plan con ese número de carros",
			},
        }
		widget = {
			'name': forms.TextInput(attrs={'class':'form-control'}),
			'image': forms.FileInput(attrs={'class':'form-control file'}),
			'number_of_cars': forms.TextInput(attrs={'class':'form-control'}),
			'price': forms.TextInput(attrs={'class':'form-control'}),
		}
class slideForm(forms.ModelForm):
	class Meta:
		model = slide
		fields = [
			'title_1',
			'title_2',
			'title_3',
			'url_1',
			'url_2',
			'url_3',
			'image',
		]
		labels= {
			'title_1': 'Title 1',
			'title_2': 'Title 2',
			'title_3': 'Title 3',
			'url_1': 'Url 1',
			'url_2': 'Url 2',
			'url_3': 'Url 3',
			'image': 'Image',
		}

		widget = {
			'image': forms.FileInput(attrs={'class':'file'}),
		}
class userCreation(forms.Form):
	username = forms.CharField(
	required=True,
	label='Nombre de usuario*',
	widget=forms.TextInput(attrs={'class':'form-control', 'id':'username', 'name':'username',}),
	)
	first_name = forms.CharField(
	required=False,
	label='Nombre',
	widget=forms.TextInput(attrs={'class':'form-control', 'id':'fname', 'name':'fname',}),
	)
	last_name = forms.CharField(
	required=False,
	label='Apellido',
	widget=forms.TextInput(attrs={'class':'form-control', 'id':'lname', 'name':'lname',}),
	)
	password = forms.CharField(
	required=True,
	label='Contraseña*',
	widget=forms.PasswordInput(render_value = True, attrs={'class':'form-control', 'id':'psw', 'name':'psw',}),
	)
	email = forms.CharField(
	required=True,
	label='Correo*',
	widget=forms.EmailInput(attrs={'class':'form-control', 'id':'email', 'name':'email',}),
	)
	phone = forms.CharField(
	required=False,
	label='Teléfono',
	widget=forms.TextInput(attrs={'class':'form-control', 'id':'phone', 'name':'phone',}),
	)
	cell_phone = forms.CharField(required=False,
	label='Teléfono Celular',
	widget=forms.TextInput(attrs={'class':'form-control', 'id':'cell_phone', 'name':'cell_phone',}),
	)
	photo = forms.ImageField(required=False,
	label='Foto',
	widget=forms.FileInput(attrs={'class':'form-control', 'id':'photo', 'name':'photo',}),
	)
	address = forms.CharField(required=False,
	label='Dirección',
	widget=forms.TextInput(attrs={'class':'form-control', 'id':'address', 'name':'address',}),
	)
	description = forms.CharField(required=False,
	label='Descripción',
	widget=forms.Textarea(attrs={'rows':"4", 'cols':"50", 'class':'form-control', 'id':'cell_phone', 'name':'cell_phone',}),
	)
	facebook = forms.CharField(required=False,
	label='Facebook',
	widget=forms.TextInput(attrs={'class':'form-control', 'id':'facebook', 'name':'facebook',}),
	)
	twitter = forms.CharField(required=False,
	label='Twitter',
	widget=forms.TextInput(attrs={'class':'form-control', 'id':'twitter', 'name':'twitter',}),
	)
	instagram = forms.CharField(required=False,
	label='Instagram',
	widget=forms.TextInput(attrs={'class':'form-control', 'id':'instagram', 'name':'instagram',}),
	)
	youtube = forms.CharField(required=False,
	label='Youtube',
	widget=forms.TextInput(attrs={'class':'form-control', 'id':'youtube', 'name':'youtube',}),
	)
	google = forms.CharField(required=False,
	label='Google plus',
	widget=forms.TextInput(attrs={'class':'form-control', 'id':'google', 'name':'google',}),
	)
	pinterest = forms.CharField(required=False,
	label='Pinterest',
	widget=forms.TextInput(attrs={'class':'form-control', 'id':'pinterest', 'name':'pinterest',}),
	)

	user_type = forms.ChoiceField(
        required=True,
        label='Tipo de Usuario*',
		widget=forms.Select(attrs={'class':'form-control', 'id':'user_type', 'name':'user_type',}),
        choices=[("Private user", "Private user"), ("Dealer user", "Dealer user")],
    )


class signForm(forms.Form):
	username = forms.CharField(required=True, label='Username', widget=forms.TextInput(attrs={'class':'form-control'}))
	email = forms.CharField(required=True, label='Email', widget=forms.TextInput(attrs={'class':'form-control'}))
	password = forms.CharField(required=True, label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
	phone = forms.CharField(required=True, label='Phone', widget=forms.TextInput(attrs={'class':'form-control'}))

class MySelect(forms.Select):
    def render_option(self, selected_choices, option_value, option_label):
        return u'<option id=' + str(option_value)  + ' style="display:none" class=\' opts _' + (str(option_value)).replace('_', ' ')  + ' ' + ('' if str(option_value) != '' else 'no')  + '\' value=\'' + str(option_value) + '\' >' + str(option_label) + '</option>'

class indexForm(forms.Form):
	makers = make.objects.all()
	dominician_republic_cities = [('', "Seleccione una ciudad"),
								  ("Azua", "Azua"),
								  ("Baoruco", "Baoruco"),
								  ("Barahona", "Barahona"),
								  ("Dajabon", "Dajabon"),
								  ("Distrito Nacional", "Distrito Nacional"),
								  ("Duarte", "Duarte"),
								  ("El Seibo", "El Seibo"),
								  ("Elias Piña", "Elias Piña"),
								  ("Espaillat", "Espaillat"),
								  ("Hato Mayor", "Hato Mayor"),
								  ("Hermanas Mirabal", "Hermanas Mirabal"),
								  ("Independencia", "Independencia"),
								  ("La Altagracia", "La Altagracia"),
								  ("La Romana", "La Romana"),
								  ("La Vega", "La Vega"),
								  ("Maria Trinidad Sanchez", "Maria Trinidad Sanchez"),
								  ("Monseñor Nouel", "Monseñor Nouel"),
								  ("Monte Cristi", "Monte Cristi"),
								  ("Monte Plata", "Monte Plata"),
								  ("Pedernales", "Pedernales"),
								  ("Peravia", "Peravia"),
								  ("Puerto Plata", "Puerto Plata"),
								  ("Samaná", "Samaná"),
								  ("San Cristóbal", "San Cristóbal"),
								  ("San José de Ocoa", "San José de Ocoa"),
								  ("San Juan", "San Juan"),
								  ("San Pedro de Macoris", "San Pedro de Macoris"),
								  ("Sánchez Ramirez", "Sánchez Ramirez"),
								  ("Santiago", "Santiago"),
								  ("Santiago Rodriguez", "Santiago Rodriguez"),
								  ("Santo Domingo", "Santo Domingo"),
								  ("Valverde", "Valverde"),]
	maker_options = [('', "Marca"),]
	maker_options += ((str(element.id), element.description) for element in (makers))
	makefield = forms.ChoiceField(
        required=False,
        label='Marca*',
		widget=forms.Select(attrs={'class':'dropdown', 'id':'make', 'name':'make', 'onchange':'changeModels();'}),
        choices=maker_options,
    )
	models_options = [('', "Seleccione marca"),]
	year_options = [('', "Seleccione trim"),]
	trim_options = [('', "Seleccione modelp"),]
	modelfield = forms.ChoiceField(
        required=False,
        label='Model',
		widget=forms.Select(attrs={'class':'dropdown', 'id':'model', 'name':'model', 'onchange':'addInfo();'}),
        choices=models_options,
    )
	trim = forms.ChoiceField(
		required=False,
		label='Trim',
		widget=forms.Select(attrs={'class':'dropdown', 'id':'trim', 'name':'trim', 'onchange':'bringYears();'}),
		choices=trim_options,
	)
	city = forms.ChoiceField(
        required=False,
        label='Ciudad',
		widget=forms.Select(attrs={'class':'dropdown', 'id':'city', 'name':'city'}),
        choices=dominician_republic_cities,
    )
	year = forms.ChoiceField(
		required=False,
		label='Year',
		widget=forms.Select(attrs={'class':'dropdown', 'id':'year', 'name':'year'}),
		choices=year_options,
	)

class expForm(forms.Form):
	#Taking data from DB
	makers = make.objects.all()
	trans_t = transmission_type.objects.all()
	drive_t = drive_train.objects.all()
	fuel_t = fuel_type.objects.all()
	eng = engine.objects.all()
	_drive = drive.objects.all()
	#Creating tuples
	maker_options = [('', "Marca"),]
	maker_options += ((str(element.id), element.description) for element in (makers))
	trans_options = [('', "Tipo de Transmisión"),]
	trans_options += ((str(element.id), element.description) for element in trans_t)
	drive_t_options = [('', "Transmisión"),]
	drive_t_options += ((str(element.id), element.description) for element in drive_t)
	fuel_options = [('', "Tipo de combustible"),]
	fuel_options += ((str(element.id), element.description) for element in fuel_t)
	engine_options = [('', "Motor"),]
	engine_options += ((str(element.id), element.description) for element in eng)
	colors = [('', "Color"),]
	colors += car._meta.get_field('exterior_color').choices
	drive_options = [('', "Drive"),]
	drive_options += ((str(element.id), element.description) for element in _drive)
	models_options = [('', "Seleccione marca"),]
	trim_options = [('', "Seleccione modelo"),]
	year_options = [('', "Seleccione trim"),]
	dominician_republic_cities = [('', "Seleccione una ciudad"),
								  ("Azua", "Azua"),
								  ("Baoruco", "Baoruco"),
								  ("Barahona", "Barahona"),
								  ("Dajabon", "Dajabon"),
								  ("Distrito Nacional", "Distrito Nacional"),
								  ("Duarte", "Duarte"),
								  ("El Seibo", "El Seibo"),
								  ("Elias Piña", "Elias Piña"),
								  ("Espaillat", "Espaillat"),
								  ("Hato Mayor", "Hato Mayor"),
								  ("Hermanas Mirabal", "Hermanas Mirabal"),
								  ("Independencia", "Independencia"),
								  ("La Altagracia", "La Altagracia"),
								  ("La Romana", "La Romana"),
								  ("La Vega", "La Vega"),
								  ("Maria Trinidad Sanchez", "Maria Trinidad Sanchez"),
								  ("Monseñor Nouel", "Monseñor Nouel"),
								  ("Monte Cristi", "Monte Cristi"),
								  ("Monte Plata", "Monte Plata"),
								  ("Pedernales", "Pedernales"),
								  ("Peravia", "Peravia"),
								  ("Puerto Plata", "Puerto Plata"),
								  ("Samaná", "Samaná"),
								  ("San Cristóbal", "San Cristóbal"),
								  ("San José de Ocoa", "San José de Ocoa"),
								  ("San Juan", "San Juan"),
								  ("San Pedro de Macoris", "San Pedro de Macoris"),
								  ("Sánchez Ramirez", "Sánchez Ramirez"),
								  ("Santiago", "Santiago"),
								  ("Santiago Rodriguez", "Santiago Rodriguez"),
								  ("Santo Domingo", "Santo Domingo"),
								  ("Valverde", "Valverde"),]

	#year = forms.IntegerField(required=True, label='Year*', widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'year', 'type': 'text', 'placeholder': "year", 'aria-describedby': "sizing-addon2"}))
	year = forms.ChoiceField(
		required=True,
		label='Año*',
		widget=forms.Select(attrs={'class':'form-control', 'id':'year', 'name':'year'}),
		choices=year_options,
	)

	trim = forms.ChoiceField(
		required=True,
		label='Trim*',
		widget=forms.Select(attrs={'class':'form-control', 'id':'trim', 'name':'trim', 'onchange':'bringYears();'}),
		choices=trim_options,
	)

	makefield = forms.ChoiceField(
        required=True,
        label='Marca*',
		widget=forms.Select(attrs={'class':'form-control', 'id':'make', 'name':'make', 'onchange':'changeModels();'}),
        choices=maker_options,
    )
	modelfield = forms.ChoiceField(
        required=True,
        label='Modelo*',
		widget=forms.Select(attrs={'class':'form-control', 'id':'model', 'name':'model', 'onchange':'addInfo();'}),
        choices=models_options,
    )
	transmission_type_in = forms.ChoiceField(
        required=True,
        label='Tipo de Transmisión*',
		widget=forms.Select(attrs={'class':'form-control', 'id':'transmission_type', 'name':'transmission_type',}),
        choices=trans_options,
    )
	drive_train_in = forms.ChoiceField(
        required=True,
        label='Transmisión*',
		widget=forms.Select(attrs={'class':'form-control', 'id':'drive_train', 'name':'drive_train',}),
        choices=drive_t_options,
    )
	fuel_type_in = forms.ChoiceField(
        required=True,
        label='Tipo de Gasolina*',
		widget=forms.Select(attrs={'class':'form-control', 'id':'fuel_type', 'name':'fuel_type',}),
        choices=fuel_options,
    )
	engine_in = forms.ChoiceField(
        required=True,
        label='Motor*',
		widget=forms.Select(attrs={'class':'form-control', 'id':'engine', 'name':'engine',}),
        choices=engine_options,
    )
	doors = forms.ChoiceField(
        required=False,
        label='Puertas',
		widget=forms.Select(attrs={'class':'form-control', 'id':'doors', 'name':'doors',}),
        choices= [('', "Doors"),] + car._meta.get_field('doors').flatchoices
    )
	ext_c = forms.ChoiceField(
        required=False,
        label='Color Exterior',
		widget=forms.Select(attrs={'class':'form-control', 'id':'ext_colors', 'name':'exterior_color',}),
        choices= colors
    )
	int_c = forms.ChoiceField(
        required=False,
        label='Color Interior',
		widget=forms.Select(attrs={'class':'form-control', 'id':'int_colors', 'name':'interior_color',}),
		choices= colors
    )
	drive = forms.ChoiceField(
        required=False,
        label='Drive',
		widget=forms.Select(attrs={'class':'form-control', 'id':'drive', 'name':'drive',}),
		choices= drive_options
    )
	int_f = forms.ChoiceField(
        required=False,
        label='Tejido interior',
		widget=forms.Select(attrs={'class':'form-control', 'id':'int_f', 'name':'int_f',}),
		choices = [('', "Interior fabric"),] + car._meta.get_field('interior_fabric').flatchoices
    )
	latitude = forms.FloatField(required=True, label='Latitud * (para ubicación exacta del vehículo)', widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'latitude', 'type': 'text', 'placeholder': "Latitud", 'aria-describedby': "sizing-addon2"}))
	longitude = forms.FloatField(required=True, label='Longitud * (para ubicación exacta del vehículo)', widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'longitude', 'type': 'text', 'placeholder': "Latitud", 'aria-describedby': "sizing-addon2"}))
	transmission_des = forms.CharField(required=False, label='Descripción de la Transmisión', widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'transmission_des', 'type': 'text', 'placeholder': "Descripción de la Transmisión", 'aria-describedby': "sizing-addon2"}))
	eng_des = forms.CharField(required=False, label='Descripción del motor', widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'engine_des', 'type': 'text', 'placeholder': "Descripción del motor", 'aria-describedby': "sizing-addon2"}))
	city_mpg = forms.ChoiceField(
        required=True,
        label='Ciudad*',
		widget=forms.Select(attrs={'class':'form-control', 'id':'city_MPG', 'name':'city_MPG',}),
		choices= dominician_republic_cities
    )
	ext_c_des = forms.CharField(required=False, label='Descripcción del color exterior', widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'ext_c_des', 'type': 'text', 'placeholder': "Descripcción del color exterior", 'aria-describedby': "sizing-addon2"}))
	int_c_des = forms.CharField(required=False, label='Descripcción del color interior', widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'int_c_des', 'type': 'text', 'placeholder': "Descripcción del color interior", 'aria-describedby': "sizing-addon2"}))
	high_mpg = forms.FloatField(required=False, label='Highway MPG', widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'high_mpg', 'type': 'text', 'placeholder': "Highway MPG", 'aria-describedby': "sizing-addon2"}))
	price = forms.IntegerField(required=True, max_value=1000000, label='Precio', widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'price', 'type': 'text', 'placeholder': "Precio", 'aria-describedby': "sizing-addon2"}))
	stock_n = forms.IntegerField(required=False, max_value=1000, label='Numere de serie', widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'Numere de serie', 'type': 'text', 'placeholder': "Stock", 'aria-describedby': "sizing-addon2"}))
	mileage = forms.IntegerField(required=True, label='Kilometraje*', widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'mileage', 'type': 'text', 'placeholder': "Kilometraje", 'aria-describedby': "sizing-addon2"}))
	off_price = forms.IntegerField(required=False, max_value=500000, label='Precio de descuento', widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'off_price', 'type': 'text', 'placeholder': "Precio de descuento",  'aria-label': "Amount (to the nearest dollar)"}))
	condition = forms.ChoiceField(
        required=True,
        label='Condición',
		widget=forms.RadioSelect(attrs={'id':'condition', 'name':'condition',}),
		choices = car._meta.get_field('condition').flatchoices
    )
	photo = forms.FileField(required=True, label='Photos', widget=forms.FileInput(attrs={ 'name': "img", 'id': "img", 'type': 'file', 'class': "file", 'multiple accept': "image"}))
	# photo = forms.FileField(required=True, label='Photos', widget=forms.FileInput())
	# <input name="img" id="img" type=file class="file" multiple accept="image/*">
	copts = (
		('Asientos de tercera fila', 'Asientos de tercera fila'),
		('Cámara de respaldo', 'Cámara de respaldo'),
		('Control de velocidad', 'Control de velocidad'),
		('Entrada sin llave', 'Entrada sin llave'),
		('Control climatico', 'Control climatico'),
		('Cerraduras eléctricas', 'Cerraduras eléctricas'),
		('Ventanas eléctricas', 'Ventanas eléctricas'),
		('Controles de dirección', 'Controles de dirección'),
    )
# (attrs={'id':'concom', 'name':'Convenience_Comfort',})
	Convenience_Comfort = forms.MultipleChoiceField(
        required=False,
        label='Convenience/Comfort',
		widget=forms.CheckboxSelectMultiple(attrs={'id':'Convenience_Comfort', 'name':'Convenience_Comfort',}),
		choices = copts
    )

	ent = (
		('Bluetooth, Manos libres', 'Bluetooth, Manos libres'),
		('Reproductor de CD', 'Reproductor de CD'),
		('Reproductor de DVD', 'Reproductor de DVD'),
		('Navegación', 'Navegación'),
		('Audio portátil', 'Audio portátil'),
		('Audio Premium', 'Audio Premium'),
		('Sistema de seguridad', 'Sistema de seguridad'),
	)
	Entertainment_Technology = forms.MultipleChoiceField(
        required=False,
        label='Entertainment/Technology',
		widget=forms.CheckboxSelectMultiple(attrs={'id':'Entertainment_Technology', 'name':'Entertainment_Technology',}),
		choices = ent
    )
	lux = (
		('Asientos con calefacción', 'Asientos con calefacción'),
		('Asientos de cuero', 'Asientos de cuero'),
		('Ruedas Premium', 'Ruedas Premium'),
		('Techo solar', 'Techo solar'),
	)
	Luxury = forms.MultipleChoiceField(
        required=False,
        label='Luxury',
		widget=forms.CheckboxSelectMultiple(attrs={'id':'Luxury', 'name':'Luxury',}),
		choices = lux
    )

	misc = (
		('Discapacidad Equipada', 'Discapacidad Equipada'),
		('Kit de elevación', 'Kit de elevación'),
		('Enganche de remolque', 'Enganche de remolque'),
	)

	Miscellaneous = forms.MultipleChoiceField(
        required=False,
        label='Miscellaneous',
		widget=forms.CheckboxSelectMultiple(attrs={'id':'Miscellaneous', 'name':'Miscellaneous',}),
		choices = misc
    )

	def is_valid(self):
		valid = super(expForm, self).is_valid()
		if self.fields["modelfield"]:
			if int(self["modelfield"].value()) < 0:
				del self.errors["modelfield"]
				self.add_error('modelfield', 'You have to choose a model')
				valid = False
			else:
				valid = True

		if self.fields["trim"]:
			try:
				if int(self["trim"].value()) < 0:
					del self.errors["trim"]
					self.add_error('trim', 'You have to choose a trim')
					valid = False
			except:
				valid = True


		return valid
