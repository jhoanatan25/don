from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.db.models import Q
import random
from math import ceil
import json
from .models import person, body_style, make, transmission_type, drive_train, fuel_type, engine, drive, car, model, mImage, theme, favourite, blog_entry, Category, slide, trim, trim_year, plans
from .forms import userForm, expForm, indexForm, signForm, slideForm
from django.contrib.auth import(
    authenticate, login as auth_login,
    logout as auth_logout
)

def logUser(request):
    context = {
    "authenticated": False,
    "username": "",
    "is_admin": False,
    "is_dealer": False,
    "userobj": None,
    }
    if(request.user.is_authenticated()):
        current_user = request.user.get_username() #Este es el nombre de usuario
        auth_user = person.objects.filter(username=current_user)[0]
        context["userobj"] = auth_user
        context["username"] = auth_user.username
        context["is_admin"] = auth_user.is_staff
        context["is_dealer"] = auth_user.is_dealer
        context["authenticated"] = True
    else:
        print("User not authenticated")
    return context


def authUser(request, username, password):
	user = authenticate(username=username, password=password)
	if user is not None and user.is_active:
		print("USER " + user.get_short_name() + " IS LOGGED IN")
		auth_login(request, user)
	return user

def logSign(request, is_dealer):
    form = userForm()
    todo = {"url": "pages/login.html"}
    context = {"auth_error": False}
    context["is_dealer"] = is_dealer
    if request.method == 'POST':
        if request.POST.get('type') == "log":
            username = request.POST.get('form-username')
            password = request.POST.get('form-password')
            user = authUser(request, username, password)
            if user is not None:
                todo["redirect"] = '/' if not user.is_staff else '/admin'
            else:
                context["auth_error"] = True
        else:
            print("SIGN")
            form = userForm(request.POST, request.FILES)
            if form.is_valid():
                sign_up = form.save(commit=False)
                sign_up.password = make_password(form.cleaned_data['password'])
                sign_up.is_dealer = is_dealer
                sign_up.status = 1
                sign_up.save()
                authUser(request, form.cleaned_data['username'], form.cleaned_data['password'])
                todo["redirect"] = '/'
    context["form"] = form
    todo["context"] = context
    return todo


def paginate(obj_per_page, objects, page_number = 1):
    truncated_objs = None
    p_info = []
    try:
        obj_per_page = obj_per_page if obj_per_page != len(objects) and obj_per_page > 0 else 5
        max_pages = ceil(len(objects) / obj_per_page)
        if not(int(page_number) <= max_pages) or page_number < 1:
            page_number = 1
        truncated_objs = objects[((page_number - 1)*obj_per_page) : ((page_number)*obj_per_page)]
        return page_number, int(max_pages), truncated_objs
    except:
        return None

def Index(request):
    posible_results_offered = 10
    ordenation = {
    1: "-created_at",
    2: "created_at",
    3: "-year",
    4: "year",
    5: "-price",
    6: "price",
    }
    page = 1 if request.method != "GET" else request.GET.get("page") if request.GET.get("page") else 1
    obj_per_page = 5 if request.method != "GET" else request.GET.get("result") if request.GET.get("result") else 5
    order = 1 if request.method != "GET" else int(request.GET.get("filter")) if request.GET.get("filter") else 1
    context = logUser(request)
    context["result"] = int(obj_per_page)
    context["body_styles"] = body_style.objects.all().order_by('index')
    context["makers"] = make.objects.all()
    page, max_pages, context["cars"]  = paginate(obj_per_page = int(obj_per_page), page_number = int(page),  objects = car.objects.filter(published=True).order_by(ordenation.get(order, "-created_at")) )
    context["max_pages_range"]= range(0, max_pages if max_pages else 1)
    context["max_pages"] = max_pages if max_pages else 1
    context["current_page"] = int(page) if (int(page) <= max_pages) else 1
    context["load_result_range"] = range(1, posible_results_offered)
    context["filter"] = order
    context["form"] = indexForm()
    context["slides"] = slide.objects.all()
    context["all_photos"] = {}
    for c in context["cars"]:
        cars_p = (mImage.objects.filter(rcar = c))
        context["all_photos"][c.id] = cars_p

    return render(request,'pages/index.html', context)

def Advance(request):
    context = logUser(request)
    context["body_styles"] = body_style.objects.all().order_by('index')
    return render(request,'pages/advance.html', context)

def Login(request):
    todo = logSign(request, True) # <- REVISAR
    # if "redirect" in todo:
    return redirect("/")
    # return render(request, todo["url"], todo["context"])

def Search(request):
    if request.method == 'POST':
        if request.POST.get('type') == "simple":
            byear = request.POST.get("byear") if "byear" in request.POST else None
            city = request.POST.get("city") if "city" in request.POST else None
            fyear = request.POST.get("fyear")  if "fyear" in request.POST else None
            bprice = request.POST.get("bprice").replace(',', '')  if "bprice" in request.POST else None
            fprice = request.POST.get("fprice").replace(',', '')  if "fprice" in request.POST else None
            Miles = request.POST.get("Miles")  if "Miles" in request.POST else None
            condition = request.POST.get('condition')  if "condition" in request.POST else None
            make = request.POST.get('makefield')  if "makefield" in request.POST else request.POST.get('nmake') if "nmake" in request.POST else None
            model = request.POST.get('modelfield') if request.POST.get('modelfield') and int(request.POST.get('modelfield')) > 0  else None
            body = request.POST.get('body')  if "body" in request.POST else None
            # trunc_cars = paginate(obj_per_page = obj_per_page, page_number = int(page),  objects = car.objects.all())
            # context["max_pages"], context["cars"] = range(0, trunc_cars[0] if trunc_cars[0] else 1) , trunc_cars[1]
            context = logUser(request)
            context["form"] = indexForm()
            print(condition)
            context["cars"] = carSearch(body_id = body, byear = byear, fyear = fyear, bprice = bprice, fprice = fprice, miles = Miles, condition = condition, make_id = make, model_id = model, city = city)
            context["all_photos"] = {}
            for c in context["cars"]:
                cars_p = (mImage.objects.filter(rcar = c))
                context["all_photos"][c.id] = cars_p
    else:
        return redirect("/")
    return render(request,'pages/search.html', context)

def Sing_Up(request):
	return render(request,'pages/Sing_Up.html', logUser(request))

def Become(request):
    context = logUser(request)
    context["all_themes"] = theme.objects.all()
    context["plans"] = plans.objects.all()
    return render(request,'pages/become.html', context)

def car_detail(request, id = None, at_dealer = '', more_context = None):
    context = logUser(request)
    print(at_dealer)
    try:
        context['car'] = car.objects.get(id = id)
        context['owner'] = context['car'].owner
        context["all_photos"] = (mImage.objects.filter(rcar = context['car']))
        context['rest_of_cars'] = car.objects.filter(~Q(id = context['car'].id), owner = context['owner'])
    except:
        id = None
    if id:
        context["rest_of_cars_photos"] = {}
        for c in context["rest_of_cars"]:
            img = (mImage.objects.filter(rcar = c))
            context["rest_of_cars_photos"][c.id] = img[0] if len(img) else None
        try:
            context["features"] = json.loads(context['car'].comfort ) + json.loads(context['car'].entertainment ) + json.loads(context['car'].luxury ) + json.loads(context['car'].miscellaneous )
            print(context["features"])
        except:
            context["features"] = []
        if more_context is not None:
            context.update(more_context)
    return render(request,('pages/Detail.html' if at_dealer == '' else at_dealer), context) if id is not None else redirect('/')

def useField(field):
    return False if field is None or field is '' else True

def checkNumberOfCars(user):
    return len(car.objects.filter(owner = user)) if user is not None else 0

def carCreation(request, body=None, registered = True, user = None):
    context = logUser(request)
    if not context["authenticated"] or (context["authenticated"] and checkNumberOfCars(context["userobj"]) < context["userobj"].cars_to_sell) or user:
        context["body_styles"] = body_style.objects.all().order_by('index')
        if body is not None and body != '':
            for body_obj in context["body_styles"]:
                if body == body_obj.description.replace(" ", "_").replace("/", "_").replace("\'", "_"):
                    body = body_obj
                    break
            else:
                body = None
        form = expForm()
        if body is not None and body != '':
            if request.method == 'POST':
                form = expForm(request.POST, request.FILES)
                if form.is_valid():
                    # try:
                    print("YES CAR CREATED")
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
                    latitude = request.POST.get('latitude')
                    longitude = request.POST.get('longitude')
                    comfort = request.POST.getlist('Convenience_Comfort')
                    entertainment = request.POST.getlist('Entertainment_Technology')
                    luxury = request.POST.getlist('Luxury')
                    miscellaneous = request.POST.getlist('Miscellaneous')
                    # images = request.POST.getlist('img')
                    images = request.FILES.getlist("photo")
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
                    if int(price) > 1000000:
                        raise ValueError("Price is too big")
                    makerobj = make.objects.get(id=_make)
                    if user:
                        user.save()
                    newCar = car.objects.create(
                    owner = context["userobj"] if context["authenticated"] else user,
                    body_s = body,
                    year = _year,
                    trim =_trim,
                    model = model.objects.get(maker=makerobj, id=_model),
                    transmission = transmission_type.objects.get(id=_transmission_type) if useField(_transmission_type) else None,
                    transmission_des = transmission_des if useField(transmission_des) else '',
                    drive_t = drive_train.objects.get(id=_drive_train) if useField(_drive_train) else None,
                    engine_des = engine_des if useField(engine_des) else '',
                    fuel_t = fuel_type.objects.get(id=_fuel_Type) if useField(_fuel_Type) else None,
                    city_MPG = city_mpg if useField(city_mpg) else '',
                    highway_MPG = high_mpg if useField(high_mpg) else '',
                    mileage = mileage if useField(mileage) else None,
                    price = int(price) ,
                    off_price = off_price if useField(off_price) else 0,
                    stock_number = stock if useField(stock) else None,
                    engine_t = engine.objects.get(id=_engine) if useField(_engine) else None,
                    drive = drive.objects.get(id=_drive) if useField(_drive) else None,
                    doors = doors if useField(doors) else 0,
                    exterior_color = exterior_color if useField(exterior_color) else '',
                    interior_color = interior_color if useField(interior_color) else '',
                    interior_fabric = interior_fabric if useField(interior_fabric) else '',
                    condition = condition if useField(condition) else '',
                    comfort = json.dumps(comfort),
                    entertainment = json.dumps(entertainment),
                    luxury = json.dumps(luxury),
                    miscellaneous = json.dumps(miscellaneous),
                    published = registered,
                    lat = latitude,
                    lon = longitude
                    )
                    # print(":::")
                    # for f in images:
                    #     print(f)
                    #     print("..")
                    for file in images:
                        newImage = mImage.objects.create(image = file, rcar = newCar)
                    return redirect("/dashboard") if context["authenticated"] else createUserForCar(request)
                    # except Exception as e:
                    #     print("Error aqui")
                    #     print(e)
                    #     return redirect("/dashboard") if context["authenticated"] else redirect("/")
                else:
                    print(form.errors.as_json())
                    print("NO CAR NOT CREATED")
            makers = make.objects.all()
            context["all_models"] = {}
            for maker in makers:
                maker_models = list(model.objects.filter(maker = maker))
                context["all_models"][maker.id] = maker_models
        context["form"] = form
    else:
        context["error"] = "No puedes crear mas carros. ¡Actualiza tu plan!"
    return (render(request, ('pages/add_inventory.html' if body is None else 'pages/add_cars.html'), context) if registered else render(request, ('pages/create_listing.html' if body is None else 'pages/create_listingF.html'), context) )


def carSearch(user = None, make_id = None, body_id = None, model_id = None, byear = None, fyear = None, bprice = None, fprice = None, miles = None, condition = None, off_price = False, ctrim = None, city = None):
    body_obj = body_style.objects.get(id = body_id) if body_id is not None else None
    try:
        make_obj = make.objects.get(id=make_id) if make_id is not None else None
        print(make_obj)
        try:
            print(model.objects.filter(maker=make_obj))
            model_obj = model.objects.filter(maker=make_obj, id=model_id) if model_id and make_obj else model.objects.filter(maker=make_obj) if make_obj else model.objects.filter(id=model_id) if model_id else None
            print(model_obj)
            first_filtered_cars = car.objects.filter(published=True, model = model_obj, body_s = body_obj) if body_obj is not None and model_obj is not None else car.objects.filter(body = body_obj) if body_obj is not None else (car.objects.filter(model__in = model_obj) if model_obj is not None else car.objects.all())
            print(first_filtered_cars)
        except:
            if make_obj is not None:
                first_filtered_cars = car.objects.filter(model__maker = make_obj)
            else:
                first_filtered_cars = car.objects.filter(body_s = body_obj)
    except:
        first_filtered_cars = car.objects.all()

    if user:
        first_filtered_cars = first_filtered_cars.filter(owner = user)
    second_filtered_cars = first_filtered_cars

    if fprice and bprice:
        second_filtered_cars = first_filtered_cars.filter(Q(price__lte = float(fprice)) & Q(price__gte = float(bprice)))

    if fyear and byear:
        second_filtered_cars = second_filtered_cars.filter(Q(year__lte = int(fyear)) & Q(year__gte = int(byear)))

    if miles and float(miles) > 0:
        second_filtered_cars = second_filtered_cars.filter(Q(mileage__lte = float(miles)))

    if condition and condition.lower() != "all":
        second_filtered_cars = second_filtered_cars.filter(Q(condition = condition))

    if off_price:
        second_filtered_cars = second_filtered_cars.filter(off_price__isnull = False)
    if ctrim:
        second_filtered_cars = second_filtered_cars.filter(trim = ctrim)
    if city:
        second_filtered_cars = second_filtered_cars.filter(city_MPG = city)
    # for _car in first_filtered_cars:
    #     print(str(_car.model.maker) + " " + str(_car.model) + " " + str(_car.owner) + " " +str( _car.price) + " " + str( _car.model.year) + " " + str(_car.mileage) + " " + str(_car.condition))

    # print("filtered data:")
    # for _car in second_filtered_cars:
    #     print(str(_car.model.maker) + " " + str(_car.model) + " " + str(_car.owner) + " " + str( _car.price) + " " + str( _car.model.year) + " " + str(_car.mileage) + " " + str(_car.condition))
    return second_filtered_cars

def logout(request):
    auth_logout(request)
    return redirect('/')

def sell(request):
    return render(request,'pages/sell.html', logUser(request))

def contact_us(request):
    return render(request,'pages/contact_us.html', logUser(request))

def jobs(request):
    return render(request,'pages/jobs.html', logUser(request))

def car_reviews(request, id = None):
    context = logUser(request)
    goto_article = False
    context["blog_name"] = "Car reviews"
    category = Category.objects.get(name = context["blog_name"])
    if id:
        try:
            context["article"] = blog_entry.objects.get(id = id, category = category, published = True)
            goto_article = True
        except Exception as e:
            print(e)
    if not goto_article:
        context["articles"] = blog_entry.objects.filter(category = category, published = True)
    return render(request, ('pages/car_reviews.html' if not goto_article else "pages/post.html"), context)

def buying_guide(request, id = None):
    context = logUser(request)
    goto_article = False
    context["blog_name"] = "Buying guide"
    category = Category.objects.get(name = context["blog_name"])
    if id:
        try:
            context["article"] = blog_entry.objects.get(id = id, category = category, published = True)
            goto_article = True
        except Exception as e:
            print(e)
    if not goto_article:
        context["articles"] = blog_entry.objects.filter(category = category, published = True)
    return render(request,('pages/buying_guide.html' if not goto_article else "pages/post.html"), context)

def press_room(request, id = None):
    context = logUser(request)
    goto_article = False
    context["blog_name"] = "Press room"
    category = Category.objects.get(name = context["blog_name"])
    if id:
        try:
            context["article"] = blog_entry.objects.get(id = id, category = category, published = True)
            goto_article = True
        except:
            pass
    if not goto_article:
        context["articles"] = blog_entry.objects.filter(category = category, published = True)
    print('pages/press_room.html' if goto_article else "pages/post.html")
    return render(request,('pages/press_room.html' if not goto_article else "pages/post.html"), context)

def post(request):
    return render(request,'pages/post.html', logUser(request))

def create_listing(request, body=None):
    user = None
    registered = False
    context = logUser(request)
    if request.method == 'POST':
        form = expForm(request.POST, request.FILES)
        if form.is_valid():
            if not context["authenticated"]:
                user = createAnonymousUser()
                request.session["user"] = user.username
            else:
                registered = True
                # user = context["userobj"]
    return carCreation(request, body, registered=registered, user = user)

def createUserForCar(request):
    form = signForm()
    return render(request, 'pages/login.html', context={'form': form})

def create_normal_user(request):
    print("ENTRA")
    if request.method == "POST":
        form = signForm(request.POST)
        if form.is_valid():
            # userid = form.cleaned_data['userid']
            temporary_user_id = request.session["user"]
            try:
                username = form.cleaned_data['username']
                password = make_password(form.cleaned_data['password'])
                email = form.cleaned_data['email']
                phone = form.cleaned_data['phone']
                # temporary_user = person.objects.filter(username = userid)
                the_car = car.objects.get(owner__username = temporary_user_id)
                print(the_car)
                the_user = person.objects.get(username = temporary_user_id)
                the_user.phone = phone
                the_user.username = username
                the_user.password = password
                the_user.email = email
                the_user.anonymous = False
                the_user.save()
                person.objects.get(username = temporary_user_id).delete()
                the_car.owner = the_user
                the_car.published = True
                the_car.save()
                authUser(request, form.cleaned_data['username'], form.cleaned_data['password'])
            except Exception as e:
                print(e)
                form = signForm()
                error = "Username or email already in use"
                return render(request, 'pages/login.html', context={'form': form, 'error': error})
    return redirect('/')

def log(request):
    log = logSign(request, False)
    return render(request,log["url"], log["context"])

@login_required
def like(request):
    context = logUser(request)
    if request.method == "GET":
        id = request.GET.get("id")
        try:
            _car = car.objects.get(id = id)
            already_liked = favourite.objects.filter(car = _car, user = context["userobj"])
            if not already_liked:
                favourite.objects.create(
                car = _car,
                user = context["userobj"],
                )
            return HttpResponse(status=201)
        except Exception as e:
            print(e)
    return HttpResponse(status=400)

@login_required
def unlike(request):
    context = logUser(request)
    if request.method == "GET":
        id = request.GET.get("id")
        try:
            _car = car.objects.get(id = id)
            _liked = favourite.objects.get(car = _car, user = context["userobj"])
            _liked.delete()
            return HttpResponse(status=201)
        except Exception as e:
            print(e)
    return HttpResponse(status=400)


def createAnonymousUser():
    username = "user" + str(random.randint(1, 1000000))
    email = username+"@gmail.com"
    return person(username=username, anonymous=True, email = email)

def find_local_dealer(request):
    return render(request,'pages/find_local_dealer.html')

def find_local_search(request):
    return render(request,'pages/find_local_search.html')

def sitemap(request):
    return render(request,'pages/sitemap.html')

def terms_conditions(request):
    return render(request,'pages/terms_conditions.html')

def getModels(request):
    if request.method == "GET":
        models = None
        if request.GET.get("maker"):
            mid = request.GET.get("maker")
            try:
                mmaker = make.objects.get(id = mid)
                models = list(model.objects.filter(maker = mmaker))
                models = {m.id: m.__unicode__() for m, m in zip(models, models)}
            except Exception as e:
                print(e)
        return HttpResponse(json.dumps(models))
    return HttpResponse(status=400)

def gettrim(request):
    if request.method == "GET":
        trims = None
        user_ = None
        user_trims = []
        if request.GET.get("model"):
            mid = request.GET.get("model")
            try:
                user_id = request.GET.get("user")
                user_ = person.objects.get(username = user_id)
            except Exception as e:
                print("no user")
            try:
                imodel = model.objects.get(id = mid)
                trims = list(t.description for t in trim.objects.filter(model = imodel))

                if user_:
                    user_trims = list(ucar.trim for ucar in car.objects.filter(model = imodel, owner = user_))

                if len(user_trims):
                    for extra_trim in user_trims:
                        if extra_trim not in trims:
                            trims.append(extra_trim)
                # trims = list((m.__unicode__(), m.__unicode__()) for m, m in zip(trims, trims))
                trims = {m: m for m, m in zip(trims, trims)}
            except Exception as e:
                print(e)
        return HttpResponse(json.dumps(trims))
    return HttpResponse(status=400)
def getyear(request):
    if request.method == "GET":
        trims_years = None
        if request.GET.get("model"):
            mid = request.GET.get("model")
            try:
                imodel = model.objects.get(id = mid)
                trims = list(trim.objects.filter(model = imodel))
                years = []
                for tr in trims:
                    t_y = trim_year.objects.filter(trim = tr)
                    for y in t_y:
                        years.append(y.year)
                trims_years = {m: m for m, m in zip(years, years)}
            except Exception as e:
                print(e)
        return HttpResponse(json.dumps(trims_years))
    return HttpResponse(status=400)

def approved(request):
    context = logUser(request)
    context["body_styles"] = body_style.objects.all().order_by('index')
    return render(request,'pages/calculator.html', context)

def financing(request):
    context = logUser(request)
    context["body_styles"] = body_style.objects.all().order_by('index')
    return render(request,'pages/financing.html', context)
def listingsel(request):
    context = logUser(request)
    context["body_styles"] = body_style.objects.all().order_by('index')
    return render(request,'pages/listingsel.html', context)

def Company_Information(request):
    return render(request,'pages/Company_Information.html', logUser(request))
