from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.db.models import Q
import random
from math import ceil
from apps.forms import userForm, expForm, indexForm, signForm, userCreation, slideForm, newPlanForm
import json
from apps.models import person, body_style, make, transmission_type, drive_train, fuel_type, engine, drive, car, model, mImage, theme, favourite, slide, trim, trim_year, plans
from apps.views import carCreation, logUser, useField, checkNumberOfCars, authUser


@login_required
def delete_car(request, id, username = None):
    context = logUser(request)
    # context["slides"] = slide.objects.all()
    try:
        user = person.objects.get(username = username) if username is not None and context["is_admin"] else context["userobj"]
        user_car = car.objects.get(id=id, owner=user)
        user_car.delete()
    except Exception as e:
        print(e)
    return redirect("/dashboard/manage/" + username) if username is not None and context["is_admin"] else redirect("/dashboard/Inventory")

@login_required
def sold_car(request, id, username = None):
    context = logUser(request)
    # context["slides"] = slide.objects.all()
    try:
        user = person.objects.get(username = username) if username is not None and context["is_admin"] else context["userobj"]
        user_car = car.objects.get(id=id, owner=user)
        user_car.sold = not user_car.sold
        user_car.published = not user_car.published
        user_car.save()
    except Exception as e:
        print(e)
    return redirect("/dashboard/manage/" + username) if username is not None and context["is_admin"] else redirect("/dashboard/sold_inventory")

@login_required
def edit_car(request, id, username = None):
    context = logUser(request)
    context["slides"] = slide.objects.all()
    try:
        user = person.objects.get(username = username) if username is not None and context["is_admin"] else context["userobj"]
        user_car = car.objects.get(id=id, owner=user)
        if request.method == 'POST':
            form = expForm(request.POST, request.FILES)
            form.fields["photo"].required = False
            if form.is_valid():
                _make = request.POST.get('makefield')
                _model = request.POST.get('modelfield')
                _trim = request.POST.get('trim')
                _year = request.POST.get('year')
                engine_des = request.POST.get('eng_des')
                city_mpg = request.POST.get('city_mpg')
                _transmission_type = (request.POST.get('transmission_type_in'))
                transmission_des = request.POST.get('transmission_des')
                _drive_train = (request.POST.get('drive_train_in'))
                _fuel_Type = (request.POST.get('fuel_type_in'))
                high_mpg = request.POST.get('high_mpg')
                _engine = request.POST.get('engine_in')
                doors = (request.POST.get('doors'))
                exterior_color = (request.POST.get('ext_c'))
                int_color_des = request.POST.get('int_c_des')
                _drive = (request.POST.get('drive'))
                interior_fabric = (request.POST.get('int_f'))
                ext_color_des = request.POST.get('ext_c_des')
                interior_color = (request.POST.get('int_c'))
                condition = (request.POST.get('condition'))
                price = request.POST.get('price')
                stock = request.POST.get('stock_n')
                mileage = request.POST.get('mileage')
                off_price = request.POST.get('off_price')
                comfort = request.POST.getlist('Convenience_Comfort')
                entertainment = request.POST.getlist('Entertainment_Technology')
                luxury = request.POST.getlist('Luxury')
                miscellaneous = request.POST.getlist('Miscellaneous')
                images = request.FILES.getlist("photo")
                latitude = request.POST.get('latitude')
                longitude = request.POST.get('longitude')
                print('make: ' + str(_make))
                print('model: ' + str(_model))
                print('trim: ' + str(_trim))
                print('year: ' + str(_year))
                print('engine_des: ' + str(engine_des))
                print('city_mpg: ' + str(city_mpg))
                print('transmission_type: ' + str(_transmission_type))
                print('transmission_des: ' + str(transmission_des))
                print('drive_train: ' + str(_drive_train))
                print('fuel_Type: ' + str(_fuel_Type))
                print('high_mpg: ' + str(high_mpg))
                print('engine: ' + str(_engine))
                print('doors: ' + str(doors))
                print('exterior_color: ' + str(exterior_color))
                print('int_color_des: ' + str(int_color_des))
                print('drive: ' + str(_drive))
                print('interior_fabric: ' + str(interior_fabric))
                print('ext_color_des: ' + str(ext_color_des))
                print('interior_color: ' + str(interior_color))
                print('condition: ' + str(condition))
                print('price: ' + str(price))
                print('stock: ' + str(stock))
                print('mileage: ' + str(mileage))
                print('latitude: ' + str(latitude))
                print('longitude: ' + str(longitude))
                print('off_price: ' + str(off_price))
                print(comfort)
                print(entertainment)
                print(luxury)
                print(miscellaneous)
                print('images: ' + str(images))
                print(request.FILES)
                makerobj = make.objects.get(id=_make)
                user_car.year = int(_year)
                user_car.trim = _trim
                user_car.model = model.objects.get(maker=makerobj, id=_model)
                user_car.transmission = transmission_type.objects.get(id=_transmission_type) if useField(_transmission_type) else None
                user_car.transmission_des = transmission_des if useField(transmission_des) else ''
                user_car.drive_t = drive_train.objects.get(id=_drive_train) if useField(_drive_train) else None
                user_car.engine_des = engine_des if useField(engine_des) else ''
                user_car.fuel_t = fuel_type.objects.get(id=_fuel_Type) if useField(_fuel_Type) else None
                user_car.city_MPG = city_mpg if useField(city_mpg) else ''
                user_car.highway_MPG = high_mpg if useField(high_mpg) else ''
                user_car.mileage = mileage if useField(mileage) else None
                user_car.price = int(price)
                user_car.off_price = off_price if useField(off_price) else 0
                user_car.stock_number = stock if useField(stock) else None
                user_car.engine_t = engine.objects.get(id=_engine) if useField(_engine) else None
                user_car.drive = drive.objects.get(id=_drive) if useField(_drive) else None
                user_car.doors = doors if useField(doors) else 0
                user_car.exterior_color = exterior_color if useField(exterior_color) else ''
                user_car.interior_color = interior_color if useField(interior_color) else ''
                user_car.interior_fabric = interior_fabric if useField(interior_fabric) else ''
                user_car.condition = condition if useField(condition) else ''
                user_car.lat = latitude if useField(latitude) else 0
                user_car.lon = longitude if useField(longitude) else 0
                user_car.comfort = json.dumps(comfort)
                user_car.entertainment = json.dumps(entertainment)
                user_car.luxury = json.dumps(luxury)
                user_car.miscellaneous = json.dumps(miscellaneous)

                user_car.save()
                for file in images:
                    newImage = mImage.objects.create(image = file, rcar = user_car)
                return redirect("/dashboard/manage/" + username) if username is not None and context["is_admin"] else redirect("/dashboard")
        else:

            data = {
                    'makefield': user_car.model.maker.id,
                    'modelfield': user_car.model.description,
                    'trim': user_car.trim,
                    'year': user_car.year,
                    'eng_des': user_car.engine_des,
                    'city_mpg': user_car.city_MPG,
                    'transmission_type_in': user_car.transmission.id if user_car.transmission is not None else '',
                    'transmission_des': user_car.transmission_des,
                    'drive_train_in': user_car.drive_t.id if user_car.drive_t is not None else '',
                    'fuel_type_in': user_car.fuel_t.id if user_car.fuel_t is not None else '',
                    'high_mpg': user_car.highway_MPG,
                    'engine_in': user_car.engine_t.id if user_car.engine_t is not None else '',
                    'drive': user_car.drive.id if user_car.drive is not None else '',
                    'doors': user_car.doors,
                    'ext_c': user_car.exterior_color,
                    'int_c': user_car.interior_color,
                    # 'ext_color_des': user_car.ext_color_des,
                    # 'int_color_des': user_car.int_color_des,
                    'int_f': user_car.interior_fabric,
                    'condition': user_car.condition,
                    'price': user_car.price,
                    'off_price': user_car.off_price,
                    'stock_n': user_car.stock_number,
                    'mileage': user_car.mileage,
                    'latitude': user_car.lat,
                    'longitude': user_car.lon,
                    'Convenience_Comfort': json.loads(user_car.comfort) if user_car.comfort else '',
                    'Entertainment_Technology': json.loads(user_car.entertainment) if user_car.entertainment else '',
                    'Luxury': json.loads(user_car.luxury) if user_car.luxury else '',
                    'Miscellaneous': json.loads(user_car.miscellaneous) if user_car.miscellaneous else '',
                    }
            form = expForm()
            model_maker = make.objects.get(id = data["makefield"])
            maker_models = model.objects.filter(maker = model_maker)
            model_fields = ((str(element.id), element.description) for element in (maker_models))
            form.fields["modelfield"].choices = model_fields

            model_trims = trim.objects.filter(model__description = data["modelfield"])
            trim_fields = list((element.description, element.description) for element in (model_trims))
            if data["trim"] not in list(el[1] for el in trim_fields):
                trim_fields.append((data["trim"], data["trim"]))
            form.fields["trim"].choices = trim_fields

            years = []
            for tr in model_trims:
                t_y = trim_year.objects.filter(trim = tr)
                for y in t_y:
                    years.append(y.year)
            trims_years = list((element, element) for element in (years))
            form.fields["year"].choices = trims_years

            context["car_edit_images"] = mImage.objects.filter(rcar__id = user_car.id)

            form.initial = data
            form.fields["photo"].required = False
        context['form'] = form
    except Exception as e:
        print(e)
    return render(request, 'pages/add_cars.html', context)

@login_required
def add_inventory(request, body=None):
    return carCreation(request, body)

@login_required
def Inventory(request):
    context = logUser(request)
    context["slides"] = slide.objects.all()
    context["cars"] = (car.objects.filter(owner=context["userobj"], published = True, sold = False))
    context["all_photos"] = {}
    for c in context["cars"]:
        cars_p = (mImage.objects.filter(rcar = c))
        context["all_photos"][c.id] = cars_p
    # print(context["all_photos"])
    return render(request,'pages/inventory.html', context)

@login_required
def Backend(request):
    context = logUser(request)
    context["slides"] = slide.objects.all()
    context["cars"] = (car.objects.filter(owner=context["userobj"], published = True, sold = False))
    context["all_photos"] = {}
    for c in context["cars"]:
        cars_p = (mImage.objects.filter(rcar = c))
        context["all_photos"][c.id] = cars_p
    # print(context["all_photos"])
    return render(request,'pages/backend.html', context)

@login_required
def sold_inventory(request):
    context = logUser(request)
    context["slides"] = slide.objects.all()
    context["cars"] = (car.objects.filter(owner=context["userobj"], published = False, sold = True))
    context["all_photos"] = {}
    for c in context["cars"]:
        cars_p = (mImage.objects.filter(rcar = c))
        context["all_photos"][c.id] = cars_p
    return render(request,'pages/sold_inventory.html', context)



@login_required
def my_favourites(request):
    context = logUser(request)
    context["slides"] = slide.objects.all()
    favo = favourite.objects.filter(user = context["userobj"])
    context["cars"] = list()
    context["all_photos"] = {}
    for el in favourite.objects.filter(user = context["userobj"]):
        context["cars"].append(el.car)
        cars_p = (mImage.objects.filter(rcar = el.car))
        context["all_photos"][el.car.id] = cars_p

    return render(request,'pages/my_favourites.html', context)

@login_required
def inventory_analysis(request):
    return render(request,'pages/inventory_analysis.html', logUser(request))

@login_required
def website(request):
    context = logUser(request)
    context["slides"] = slide.objects.all()
    if context["is_dealer"]:
        context["all_themes"] = theme.objects.all()
        if request.method == "POST":
            try:
                new_theme = theme.objects.get(name = request.POST.get('change'))
                person.objects.filter(username = context["userobj"].username).update(utheme = new_theme)
                context["message"] = "Theme changed"
                context["current"] = new_theme
            except:
                context["message"] = "A terrible error has happened"
                context["current"] = context["userobj"].utheme if context["userobj"].utheme is not None else theme.objects.filter(name = "A1001")
        else:
            context["current"] = context["userobj"].utheme if context["userobj"].utheme is not None else theme.objects.filter(name = "A1001")

    return render(request,'pages/website.html', context) if context["is_dealer"] else redirect("/dashboard")

@login_required
def profile(request):
    context = logUser(request)
    context["slides"] = slide.objects.all()
    if request.method == "POST":
        if context["userobj"].check_password(request.POST.get('old_psw')):
            first_name = request.POST.get('fname')
            last_name = request.POST.get('lname')
            raw_new_psw = request.POST.get('new_psw')
            new_psw = make_password(raw_new_psw)
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            cell_phone = request.POST.get('cphone')
            address = request.POST.get('address')
            description = request.POST.get('description')
            photo = request.FILES.get('img')

            if context["userobj"].first_name != first_name and first_name is not None and first_name != '':
                person.objects.filter(username = context["userobj"].username).update(first_name = first_name)
            if context["userobj"].last_name != last_name and last_name is not None and last_name != '':
                person.objects.filter(username = context["userobj"].username).update(last_name = last_name)
            if context["userobj"].phone != phone and phone is not None and phone != '':
                person.objects.filter(username = context["userobj"].username).update(phone = phone)
            if context["userobj"].cell_phone != cell_phone and cell_phone is not None and cell_phone != '':
                person.objects.filter(username = context["userobj"].username).update(cell_phone = cell_phone)
            if context["userobj"].address != address and address is not None and address != '':
                person.objects.filter(username = context["userobj"].username).update(address = address)
            if context["userobj"].description != description and description is not None and description != '':
                person.objects.filter(username = context["userobj"].username).update(description = description)
            if photo is not None:
                user = person.objects.get(username = context["userobj"].username)
                user.image.save(photo.name, photo)

            if raw_new_psw is not None and raw_new_psw != '':
                person.objects.filter(username = context["userobj"].username).update(password = new_psw)
                authUser(request, context["userobj"].username, raw_new_psw)
            context = logUser(request)
            context["message"] = "Info updated"
        else:
            context["message"] = "Wrong password. You need to enter your password in order to change your info"

    return render(request,'pages/profile.html', context)

@login_required
def edit_user(request, username):
    context = logUser(request)
    context["slides"] = slide.objects.all()
    if context["is_admin"]:
        context["title"] = "Edit user " + username
        context["edit_user"] = True
        try:
            user = person.objects.get(username = username)
        except Exception as e:
            return redirect("/dashboard/all_users")
        context["form"] = userCreation(initial={'username': user.username, 'password': "Not so fast", 'email': user.email, 'first_name': user.first_name, 'last_name': user.last_name,'address': user.address,'description': user.description, 'phone': user.phone, 'cell_phone': user.cell_phone, 'user_type': 'Private user' if not user.is_dealer else 'Dealer user',
        'facebook': user.facebook, 'twitter': user.twitter, 'instagram': user.instagram, 'google': user.google, 'pinterest': user.pinterest, 'youtube': user.youtube})
        if request.method == "POST":
            context["form"] = userCreation(request.POST, request.FILES)
            print(context["form"])
            if context["form"].is_valid():
                print("ES VÁLIDO")
                username = context["form"].cleaned_data['username']
                first_name = context["form"].cleaned_data['first_name']
                last_name = context["form"].cleaned_data['last_name']
                psw = context["form"].cleaned_data['password']
                email = context["form"].cleaned_data['email']
                phone = context["form"].cleaned_data['phone']
                cell_phone = context["form"].cleaned_data['cell_phone']
                user_type = context["form"].cleaned_data['user_type']
                address = context["form"].cleaned_data['address']
                description = context["form"].cleaned_data['description']
                facebook = context["form"].cleaned_data['facebook']
                twitter = context["form"].cleaned_data['twitter']
                instagram = context["form"].cleaned_data['instagram']
                google = context["form"].cleaned_data['google']
                pinterest = context["form"].cleaned_data['pinterest']
                youtube = context["form"].cleaned_data['youtube']
                photo = request.FILES.get('photo')

                if user.first_name != first_name and first_name is not None and first_name != '':
                    person.objects.filter(username = user.username).update(first_name = first_name)
                if user.last_name != last_name and last_name is not None and last_name != '':
                    person.objects.filter(username = user.username).update(last_name = last_name)
                if user.phone != phone and phone is not None and phone != '':
                    person.objects.filter(username = user.username).update(phone = phone)
                if user.cell_phone != cell_phone and cell_phone is not None and cell_phone != '':
                    person.objects.filter(username = user.username).update(cell_phone = cell_phone)
                if user.address != address and address is not None and address != '':
                    person.objects.filter(username = user.username).update(address = address)
                if user.description != description and description is not None and description != '':
                    person.objects.filter(username = user.username).update(description = description)
                if user.facebook != facebook and facebook is not None and facebook != '':
                    person.objects.filter(username = user.username).update(facebook = facebook)
                if user.twitter != twitter and twitter is not None and twitter != '':
                    person.objects.filter(username = user.username).update(twitter = twitter)
                if user.instagram != instagram and instagram is not None and instagram != '':
                    person.objects.filter(username = user.username).update(instagram = instagram)
                if user.google != google and google is not None and google != '':
                    person.objects.filter(username = user.username).update(google = google)
                if user.pinterest != pinterest and pinterest is not None and pinterest != '':
                    person.objects.filter(username = user.username).update(pinterest = pinterest)
                if user.youtube != youtube and youtube is not None and youtube != '':
                    person.objects.filter(username = user.username).update(youtube = youtube)
                if user.is_dealer == (user_type == "Private user"):
                    person.objects.filter(username = user.username).update(is_dealer = (user_type != "Private user"))

                if photo is not None:
                    user = person.objects.get(username = user.username)
                    user.image.save(photo.name, photo)
                context["message"] = "User " + username + " updated!"

    return render(request,'pages/create_user.html', context) if context["is_admin"] else redirect('/dashboard')

@login_required
def all_users(request, type = None):
    context = logUser(request)
    context["slides"] = slide.objects.all()
    if context["is_admin"]:
        if request.method == 'POST':
            try:
                if request.POST.get('delete') is not None:
                    user = person.objects.get(username = request.POST.get('delete'))
                    context["message"] = "El usuario " + user.username + " ha sido eliminado :("
                    user.delete()
                elif request.POST.get('upgrade') is not None:
                    user = person.objects.get(username = request.POST.get('upgrade'))
                    context["message"] = "¡El usuario " + user.username + " Es ahora distribuidor!"
                    plan = plans.objects.all().first()
                    if plan:
                        person.objects.filter(username = request.POST.get('upgrade')).update(is_dealer = True, cars_to_sell = plan.number_of_cars)
                    else:
                        person.objects.filter(username = request.POST.get('upgrade')).update(is_dealer = True)
                elif request.POST.get('edit') is not None:
                    return redirect("/dashboard/edit_user/"+request.POST.get('edit'))
                elif request.POST.get('down') is not None:
                    user = person.objects.get(username = request.POST.get('down'))
                    context["message"] = "¡El usuario " + user.username + " es ahora vendedor privado!"
                    person.objects.filter(username = request.POST.get('down')).update(is_dealer = False)
                elif request.POST.get('manage') is not None:
                    return redirect("/dashboard/manage/"+request.POST.get('manage'))
                elif request.POST.get('theme') is not None and request.POST.get('theme') != '':
                    info = request.POST.get('theme').split('|')
                    user = info[0]
                    theme_name = info[1]
                    user = person.objects.get(username = user)
                    new_theme = theme.objects.get(name = theme_name)
                    person.objects.filter(username = user).update(utheme = new_theme)
                    context["message"] = "Usuario " + user.username + " está usando el tema " + theme_name + " ahora"
                elif request.POST.get('plan') is not None:
                    info = request.POST.get('plan').split('|')
                    user = info[0]
                    plan_id = info[1]
                    user = person.objects.get(username = user)
                    new_plan = plans.objects.get(id = plan_id)
                    person.objects.filter(username = user).update(cars_to_sell = new_plan.number_of_cars)
                    context["message"] = "Usuario " + user.username + " está usando el plan " + str(new_plan)  + " ahora"
            except Exception as e:
                print(e)
        context["all_themes"] = theme.objects.all()
        context["plans"] = plans.objects.all()
        context["all_users"] = person.objects.filter(~Q(username = 'admin'), anonymous = False) if type is None else (person.objects.filter(~Q(username = 'admin'), anonymous = False, is_dealer = (type == "dealer")) if type == "dealer" or type == "private" else person.objects.filter(~Q(username = 'admin'), anonymous = False))

    return render(request,'pages/all_users.html', context) if context["is_admin"] else redirect('/dashboard')

@login_required
def new(request, type = None):
    context = logUser(request)
    context["slides"] = slide.objects.all()
    if context["is_admin"]:
        context["title"] = "Create new " + ("" if type is None else type) + " user!"
        initial = {} if type is None else {'user_type': "Dealer user"} if type == "dealer" else {'user_type': "Private seller"} if type == "private" else {}
        context["show_selection"] = True if type is not None else False
        context["form"] = userCreation(initial = initial)
        context["edit_user"] = False
        if request.method == "POST":
            context["form"] = userCreation(request.POST, request.FILES)
            if context["form"].is_valid():
                username = context["form"].cleaned_data['username']
                first_name = context["form"].cleaned_data['first_name']
                last_name = context["form"].cleaned_data['last_name']
                psw = context["form"].cleaned_data['password']
                email = context["form"].cleaned_data['email']
                phone = context["form"].cleaned_data['phone']
                user_type = context["form"].cleaned_data['user_type']
                cell_phone = context["form"].cleaned_data['cell_phone']
                description = context["form"].cleaned_data['description']
                address = context["form"].cleaned_data['address']
                facebook = context["form"].cleaned_data['facebook']
                twitter = context["form"].cleaned_data['twitter']
                instagram = context["form"].cleaned_data['instagram']
                google = context["form"].cleaned_data['google']
                pinterest = context["form"].cleaned_data['pinterest']
                youtube = context["form"].cleaned_data['youtube']

                photo = request.FILES.get('photo')
                try:
                    new_user = person.objects.create(username = username,
                    password = make_password(psw),
                    first_name = first_name,
                    last_name = last_name ,
                    email = email,
                    phone = phone,
                    cell_phone = cell_phone,
                    description = description,
                    address = address,
                    facebook = facebook,
                    twitter = twitter,
                    instagram = instagram,
                    google = google,
                    pinterest = pinterest,
                    youtube = youtube,
                    image = photo,
                    is_dealer = (user_type != "Private user")
                    )
                    context["message"] = "User " + username + " created!. Want to create a new one?"
                    context["form"] = userCreation()
                except Exception as e:
                    print(e)
                    context["message"] = "Username or email already in use"
    return render(request,'pages/create_user.html', context) if context["is_admin"] else redirect('/dashboard')

@login_required
def manage(request, username):
    context = logUser(request)
    context["slides"] = slide.objects.all()
    if context["is_admin"]:
        user = None
        try:
            user = person.objects.get(username = username)
        except:
            return redirect("/dashboard/all_users")
        context["client"] = user.username
        context["all_cars"] = car.objects.filter(owner=user.username)
        context["cars_photos"] = {}
        for c in context["all_cars"]:
            img = (mImage.objects.filter(rcar = c))
            context["cars_photos"][c.id] = img[0] if len(img) else None
        if request.method == 'POST':
            try:
                if request.POST.get('delete') is not None:
                    car_id = request.POST.get('delete').split('|')
                    return redirect("/dashboard/delete/" + car_id[1] + "/" + car_id[0])
                elif request.POST.get('sold') is not None:
                    car_id = request.POST.get('sold').split('|')
                    return redirect("/dashboard/sold/" + car_id[1] + "/" + car_id[0])
                elif request.POST.get('edit') is not None:
                    car_id = request.POST.get('edit').split('|')
                    return redirect("/dashboard/edit/" + car_id[1] + "/" + car_id[0])
            except:
                pass
    return render(request,'pages/manage.html', context) if context["is_admin"] else redirect('/dashboard')

@login_required
def blog_car_reviews(request):
    return render(request,'pages/blog_car_reviews.html', logUser(request))

@login_required
def blog_press_room(request):
    return render(request,'pages/blog_press_room.html', logUser(request))

@login_required
def blog_buying_guide(request):
    return render(request,'pages/blog_buying_guide.html', logUser(request))

@login_required
def article(request):
    return render(request,'pages/article.html', logUser(request))

@login_required
def slideFunction(request, id = None):
    context = logUser(request)
    context["slides"] = slide.objects.all()
    context["title"] = "New slide" if not id else "Slide " + id
    obj_slide = None
    # redirect_to = False
    try:
        if id:
            obj_slide = slide.objects.get(id = id)
    except:
        obj_slide = None
    if request.method == "POST":
        new_slide = slideForm(request.POST, request.FILES) if not obj_slide else slideForm(request.POST, request.FILES, instance = obj_slide)
        if new_slide.is_valid():
            new_slide.save()
            context["form"] = slideForm()
            context["message"] = "Slide agregado"
            # redirect_to = True
        else:
            context["form"] = new_slide
    else:
        context["form"] = slideForm(instance = obj_slide) if obj_slide else slideForm()
    return render(request,'pages/slide.html', context) #if not redirect_to else redirect("/dashboard/slide")

@login_required
def plans_function(request):
    context = logUser(request)
    if context["is_admin"]:
        context["plans"] = plans.objects.all()
        context["plan_form"] = newPlanForm
        if request.method == 'POST':
            if request.POST.get('delete') is not None:
                try:
                    plan_id = request.POST.get('delete')
                    plans.objects.get(id = plan_id).delete()
                    context["message"] = "Se ha eliminado el plan con éxito"
                except Exception as e:
                    print("Error while deleting plan")
            elif request.POST.get('edit') is not None:
                try:
                    plan_id = request.POST.get('edit')
                    request.session["edit_plan"] = plan_id
                    context["plan_form"] = newPlanForm(instance = plans.objects.get(id = plan_id))
                    context["check"] = True
                except Exception as e:
                    print("Error while editing plan")
            else:
                if 'edit_plan' in request.session :
                    try:
                        created_plan = newPlanForm(request.POST, request.FILES, instance = plans.objects.get(id = request.session["edit_plan"]))
                    except Exception as e:
                        created_plan = newPlanForm(request.POST, request.FILES)
                else:
                    created_plan = newPlanForm(request.POST, request.FILES)

                if created_plan.is_valid():
                    created_plan.save()
                    if 'edit_plan' in request.session :
                        del request.session["edit_plan"]
                else:
                    context["plan_form"] = created_plan
                    context["check"] = True
        return render(request,'pages/plans.html', context)
    else:
        return redirect("/dashboard")

@login_required
def logo(request):
    context = logUser(request)
    context["slides"] = slide.objects.all()
    if request.method == 'POST':
        try:
            images = request.FILES
            logo = list(images.values())[0]
            user = person.objects.get(username = context["userobj"].username)
            user.logo.save(context["userobj"].username, logo)
        except:
            pass
        print("Logo changed")
    return redirect("/dashboard/website")

@login_required
def manager(request):
    return render(request,'pages/manager.html', logUser(request))

@login_required
def editterms(request):
    return render(request,'pages/editterms.html', logUser(request))

@login_required
def Edit_Company_Information(request):
    return render(request,'pages/Edit_Company_Information.html', logUser(request))
