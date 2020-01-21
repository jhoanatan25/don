from django.shortcuts import render, redirect, render_to_response
from apps.models import person, body_style, make, transmission_type, drive_train, fuel_type, engine, drive, car, model, mImage, theme
from apps.views import logUser, car_detail, paginate, carSearch
from apps.forms import indexForm

class themeFunctions():
    def __init__(self):
        self.all_themes = theme.objects.all()
        self.pages = {'index': self.index,
                    'inventory': self.inventory,
                    'car_finder': self.car_finder,
                    'specials': self.special,
                    'contact_us': self.contact,
                    'direction': self.direction,
                    'financing': self.financing,
                    'detail': self.detail,
                    'our_team': self.our_team,
                    'blog': self.blog,
                    'sell_or_trade': self.trade,
                    'approved': self.approved,
                    }

    def index(self, theme_name, request, context):
        context["cars_photos"] = {}
        if "dealer" in context:
            context["get_info"] = {}
            byear = request.GET.get("year") if "year" in request.GET and request.GET.get('year') != "-1" else None
            context["get_info"]["byear"] = byear
            fyear = request.GET.get("fyear")  if "fyear" in request.GET else None
            context["get_info"]["fyear"] = fyear
            bprice = request.GET.get("bprice")  if "bprice" in request.GET else None
            context["get_info"]["bprice"] = bprice
            fprice = request.GET.get("fprice")  if "fprice" in request.GET else None
            context["get_info"]["fprice"] = fprice
            milles = request.GET.get("milles")  if "milles" in request.GET else None
            context["get_info"]["milles"] = milles
            condition = request.GET.get('condition')  if "condition" in request.GET else None
            context["get_info"]["condition"] = condition
            make = request.GET.get('makefield') if "makefield" in request.GET and request.GET.get('makefield') != "-1" else None
            context["get_info"]["make"] = make
            model = request.GET.get('modelfield') if "modelfield" in request.GET and request.GET.get('modelfield') != "-1" else None
            context["get_info"]["model"] = model
            body = request.GET.get('body')  if "body" in request.GET else None
            context["get_info"]["body"] = body
            ctrim = request.GET.get("trim")  if "trim" in request.GET and request.GET.get("trim") != "-1" else None
            context["get_info"]["trim"] = ctrim
            if byear or fyear or bprice or fprice or milles or condition or make or model or body or ctrim:
                context["current_page"], context["max_pages"], context["cars"] = self.search(context["dealer"],
                context["current_page"], context["obj_per_page"], make = make, body = body, model = model, milleage = milles, byear = byear, fyear = fyear, min_price = bprice, max_price = fprice, condition = condition, off_price = True, ctrim = ctrim)
            else:
                context["current_page"], context["max_pages"], context["cars"] = self.getUsers(context["dealer"], context["current_page"], context["obj_per_page"])

            context["form"] = indexForm()
            context["max_pages_range"]= range(0, context["max_pages"] if context["max_pages"] else 1)

            for c in context["cars"]:
                context["cars_photos"][c.id] = self.getSinglePhoto(c.id)
        print(context["cars_photos"])
        return render(request,'themes/' + str(theme_name) + '/index.html', context)

    def inventory(self, theme_name, request, context):
        if "dealer" in context:
            context["current_page"], context["max_pages"], context["cars"] = self.getUsers(context["dealer"], context["current_page"], context["obj_per_page"])
            context["max_pages_range"]= range(0, context["max_pages"] if context["max_pages"] else 1)
            context["cars_photos"] = {}
            for c in context["cars"]:
                context["cars_photos"][c.id] = self.getSinglePhoto(c.id)

        return render(request,'themes/' + str(theme_name) + '/inventory.html', context)

    def car_finder(self, theme_name, request, context):
        return render(request,'themes/' + str(theme_name) + '/car_finder.html', context)

    def special(self, theme_name, request, context):
        context["cars_photos"] = {}
        if "dealer" in context:
            context["get_info"] = {}
            byear = request.GET.get("year") if "year" in request.GET and request.GET.get('year') != "-1" else None
            context["get_info"]["byear"] = byear
            fyear = request.GET.get("fyear")  if "fyear" in request.GET else None
            context["get_info"]["fyear"] = fyear
            bprice = request.GET.get("bprice")  if "bprice" in request.GET else None
            context["get_info"]["bprice"] = bprice
            fprice = request.GET.get("fprice")  if "fprice" in request.GET else None
            context["get_info"]["fprice"] = fprice
            milles = request.GET.get("milles")  if "milles" in request.GET else None
            context["get_info"]["milles"] = milles
            condition = request.GET.get('condition')  if "condition" in request.GET else None
            context["get_info"]["condition"] = condition
            make = request.GET.get('makefield') if "makefield" in request.GET and request.GET.get('makefield') != "-1" else None
            context["get_info"]["make"] = make
            model = request.GET.get('modelfield') if "modelfield" in request.GET and request.GET.get('modelfield') != "-1" else None
            context["get_info"]["model"] = model
            body = request.GET.get('body')  if "body" in request.GET else None
            context["get_info"]["body"] = body
            ctrim = request.GET.get("trim")  if "trim" in request.GET and request.GET.get("trim") != "-1" else None
            context["get_info"]["trim"] = ctrim
            if byear or fyear or bprice or fprice or milles or condition or make or model or body or ctrim:
                context["current_page"], context["max_pages"], context["cars"] = self.search(context["dealer"],
                context["current_page"], context["obj_per_page"], make = make, body = body, model = model, milleage = milles, byear = byear, fyear = fyear, min_price = bprice, max_price = fprice, condition = condition, off_price = True, ctrim = ctrim)
            else:
                context["current_page"], context["max_pages"], context["cars"] = self.getUsers(context["dealer"], context["current_page"], context["obj_per_page"])

            context["form"] = indexForm()
            context["max_pages_range"]= range(0, context["max_pages"] if context["max_pages"] else 1)

            for c in context["cars"]:
                context["cars_photos"][c.id] = self.getSinglePhoto(c.id)
        print(context["cars_photos"])
        return render(request,'themes/' + str(theme_name) + '/special.html', context)

    def contact(self, theme_name, request, context):
        return render(request,'themes/' + str(theme_name) + '/contact_us.html', context)

    def our_team(self, theme_name, request, context):
        return render(request,'themes/' + str(theme_name) + '/our.html', context)

    def blog(self, theme_name, request, context):
        return render(request,'themes/' + str(theme_name) + '/blog.html', context)

    def direction(self, theme_name, request, context):
        return render(request,'themes/' + str(theme_name) + '/direction.html', context)

    def financing(self, theme_name, request, context):
        return render(request,'themes/' + str(theme_name) + '/financing.html', context)

    def approved(self, theme_name, request, context):
        return render(request,'themes/' + str(theme_name) + '/calculator.html', context)


    def trade(self, theme_name, request, context):
        return render(request,'themes/' + str(theme_name) + '/sell_or_trade.html', context)

    def detail(self, theme_name, request, context):
        #puede que le deba concatenar el context
        go = context["owner"] == car.objects.get(id = context["car_id"]).owner
        return car_detail(request, context["car_id"], ('themes/' + str(theme_name) + '/Detail.html'), context) if context["car_id"] and go else self.redirect(theme_name, request, context)

    def redirect(self, theme_name, request, context):
        return redirect('/dealer/' + str(context['dealer'] if context['dealer'] is not None else context['name_page']))

    def getPages(self, page):
        return self.pages.get(page, self.redirect)

    def getThemes(self):
        return self.all_themes

    def search(self, userid, page, obj_per_page, make = None, body = None, model = None, milleage = None, byear = None, fyear = None, min_price = None, max_price = None, condition = None, off_price = False, ctrim = None):
        user = person.objects.filter(username = userid)
        cars = carSearch(user = user, make_id = make, body_id = body, model_id = model, byear = byear, fyear = fyear, bprice = min_price, fprice = max_price, miles = milleage, condition = condition, off_price = off_price, ctrim = ctrim)
        return paginate(obj_per_page = int(obj_per_page), page_number = int(page),  objects = cars)

    def getUsers(self, userid, page, obj_per_page, off_price = False):
        user = person.objects.filter(username = userid)
        return paginate(obj_per_page = int(obj_per_page), page_number = int(page),  objects = car.objects.filter(owner = user, published=True) if off_price else car.objects.filter(owner = user, published=True, off_price__isnull = False))

    def getSinglePhoto(self, carid):
        the_car = car.objects.get(id = carid)
        img = (mImage.objects.filter(rcar = the_car))
        return img[0] if len(img) else None

def dealer_page(request, username = None, page = None, id = None):
    theme_obj = themeFunctions()
    context = logUser(request)
    try:
        dealer = person.objects.get(username = username)
        if not dealer.is_dealer:
            username = None
    except:
        dealer = None

    if dealer is None:
        try:
            theme_name = username if (theme.objects.get(name = username) if username is not None else '') in theme_obj.getThemes() else theme_obj.getThemes()[0]
        except:
            theme_name = theme_obj.getThemes()[0]
        context["name_page"] = theme_name
    else:
        context["current_page"] = 1 if request.method != "GET" else int(request.GET.get("page")) if request.GET.get("page") else 1
        context["owner"] = dealer
        theme_name = dealer.utheme if dealer.utheme is not None else theme_obj.getThemes()[0]
        context["obj_per_page"] = dealer.utheme.number_of_cars if dealer.utheme is not None else 5
        context["car_id"] = id
        context["name_page"] = username
        context["dealer"] = username

    return theme_obj.getPages(page if page is not None else 'index')(theme_name, request, context) if username is not None else redirect('/')
