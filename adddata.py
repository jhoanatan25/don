import os
from collections import OrderedDict
import csv
if 'OPENSHIFT_REPO_DIR' in os.environ:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cars4driver.settings")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cars4driver.development")
import django
django.setup()
from django.core.files import File
import random
from apps.models import body_style, make, transmission_type, drive_train, fuel_type, engine as _engine, drive, model, theme, trim, trim_year

class load:
    def __init__ (self):
        pass
    def addMake(self, _make):
        try:
            nmake = make.objects.get(description = _make)
        except Exception as e:
            print("Adding maker: " + _make)
            nmake = make.objects.create(description= _make)
        return nmake

    def addTrans(self, trans):
        for obj in trans:
            try:
                print("Adding " + obj + " to transmission_type")
                transmission_type.objects.create(description=obj)
            except:
                print("Error on " + obj)
    def addDriveTrain(self, drive_t):
        for obj in drive_t:
            try:
                print("Adding " + obj + " to drive_train")
                drive_train.objects.create(description=obj)
            except:
                print("Error on " + obj)
    def addFuelType(self, fuel_t):
        for obj in fuel_t:
            try:
                print("Adding " + obj + " to fuel_type")
                fuel_type.objects.create(description=obj)
            except:
                print("Error on " + obj)

    def addEngine(self, eng):
        for obj in eng:
            try:
                print("Adding " + obj + " to engine")
                _engine.objects.create(description=obj)
            except:
                print("Error on " + obj)
    def addDrive(self, dri):
        for obj in dri:
            try:
                print("Adding " + obj + " to drive")
                drive.objects.create(description=obj)
            except:
                print("Error on " + obj)
    def addBody(self, body_dict):
        for des, image_url in body_dict.items():
            try:
                print("Adding " + des + " to body_style")
                body_object = body_style.objects.create(description=des)
                image_url = os.getcwd() + image_url
                print(image_url)
                with open(image_url, 'rb') as f:
                    image_file = File(f)
                    print("Image url: " + image_url.split("/")[-1])
                    body_object.image.save(image_url.split("/")[-1], image_file, True)
                    body_object.save()
            except:
                print("Error on " + des)
    def addThemes(self, themes_d):
        for name, info in themes_d.items():
            try:
                print("Adding " + name + " to themes")
                ntheme = theme.objects.create(name=name, number_of_cars=info[1])
                image_url = os.getcwd() + info[0]
                with open(image_url, 'rb') as f:
                    image_file = File(f)
                    print("Image url: " + image_url.split("/")[-1])
                    ntheme.image.save(image_url.split("/")[-1], image_file, True)
                    ntheme.save()
            except Exception as e:
                print(e)
                print("Error on " + name)
    def addModels(self, maker, model_name, model_trim, model_year):
        mmake = self.addMake(maker)
        print("Creating model:")
        print(model_name)

        try:
            _model = model.objects.get(description=model_name, maker=mmake)
            print("Model already exists")
        except:
            _model = model.objects.create(description=model_name, maker=mmake)
        print("Creating trim:")
        print(model_trim)
        try:
            _trim = trim.objects.get(description=model_trim, model=_model)
            print("Trim already exists")
        except:
            _trim = trim.objects.create(description=model_trim, model=_model)
        print("Creating trim year:")
        print(model_year)
        try:
            _trim_year = trim_year.objects.get(year=int(model_year), trim=_trim)
            print("Year on that trim already exists")
        except:
            _trim_year = trim_year.objects.create(year=int(model_year), trim=_trim)



    def dataExtract(self):
        with open('data.csv', newline='') as csvfile:
            data = csv.reader(csvfile, delimiter=',')
            old_model_trim = ""
            for row in list(data)[1:]:
                maker, model_name, model_trim, model_year = self.modelCreator(row)
                if len(maker) and len(model_name) and len(model_trim) and len(model_year):
                    if not len(model_trim):
                        model_trim = old_model_trim
                    else:
                        old_model_trim = model_trim
                    maker = maker[0].upper() + maker[1:].lower()
                    self.addModels(maker, model_name.lower(), model_trim, model_year)
                else:
                    print("empty line")
                print("--")

    def modelCreator(self, row):
        maker = row[1]
        model_name = row[2]
        model_trim = row[3]
        model_year = row[4]
        return maker, model_name, model_trim, model_year



loadobj = load()

# engine = [
# "3 Cylinder",
# "4 Cylinder",
# "5 Cylinder",
# "6 Cylinder",
# "8 Cylinder",
# "10 Cylinder",
# "12 Cylinder",
# "Electric",
# "Hybrid",
# "Rotary Engine",
# ]
#
#
# loadobj.addEngine(engine)

themes = OrderedDict()
themes["A1001"] = ("/static/images/1.png", 6)
themes["A1002"] = ("/static/images/2.png", 5)
themes["A1003"] = ("/static/images/3.png", 5)
themes["A1004"] = ("/static/images/4.png", 5)
themes["A1005"] = ("/static/images/5.png", 5)
themes["A1006"] = ("/static/images/6.png", 6)
themes["A1007"] = ("/static/images/7.jpg", 10)
themes["A1008"] = ("/static/images/8.jpg", 5)
themes["A1009"] = ("/static/images/9.jpg", 8)
themes["A1010"] = ("/static/images/10.jpg", 10)
themes["A1011"] = ("/static/images/11.jpg", 6)
themes["A1012"] = ("/static/images/12.png", 6)

loadobj.addThemes(themes)
# AGREGAR CATEGORIAS DE BLOG
# transmission_types = [
# 	"Automatic",
#     "Manual",
#     "CTV",
#     "Semi-Automatic",
#     "Automatic 1-Speed",
#     "Automatic 2-Speed",
#     "Automatic 3-Speed",
#     "Automatic 4-Speed",
#     "Automatic 5-Speed",
#     "Automatic 6-Speed",
#     "Automatic 7-Speed",
#     "Automatic 8-Speed",
#     "Automatic 9-Speed",
#     "Manual 3-Speed",
#     "Manual 4-Speed",
#     "Manual 5-Speed",
#     "Manual 6-Speed",
#     "Manual 7-Speed",
#     "CVT 6-Speed",
#     "CVT 7-Speed",
#     "CVT 8-Speed",
#     "Other 1-Speed",
#     "Other 8-Speed",
#     "Other",
# ]
#
# loadobj.addTrans(transmission_types)
#
# drive_trains = [
#     "Front Wheel Drive",
#     "Rear Wheel Drive",
#     "All Wheel Drive",
#     "4 Wheel Drive",
#     "4X4",
#     "4X2",
#     "Other",
# ]
#
# loadobj.addDriveTrain(drive_trains)
#
# fuel_types = [
#     "Gasoline",
#     "Flex Fuel",
#     "Diesel",
#     "Bio Diesel",
#     "Gas/Electric Hybrid",
#     "Plug-in Hybrid",
#     "Electric",
#     "Propane",
#     "Natural Gas",
#     "Hydrogen",
#     "Not Applicable",
# ]
#
# loadobj.addFuelType(fuel_types)
#
# _drive = [
#     "Front Wheel Drive",
#     "Rear Wheel Drive",
#     "AWD/4WD",
# ]
# loadobj.addDrive(_drive)
body_dict = {
    "Sedan": "/static/body_styles/Sedan.png",
    "Coupe": "/static/body_styles/coupe.png",
    "Hatchback Wagos": "/static/body_styles/HatchbacksWagons.png",
    "Sportcar": "/static/body_styles/sport.png",
    "Convertible": "/static/body_styles/Convertible.png",
    "Luxury Cars": "/static/body_styles/Luxyrycars.png",
    "Hybrid Electric": "/static/body_styles/HybridElectric.png",
    "Crossover": "/static/body_styles/Crossover.png",
    "SUV's": "/static/body_styles/SUVs.png",
    "Pick up trucks": "/static/body_styles/PickupTrucks.png",
    "Van/minivan": "/static/body_styles/VanMinivan.png",
    "Commercial Cars": "/static/body_styles/Commercial.png",
}
loadobj.addBody(body_dict)
#loadobj.dataExtract()
