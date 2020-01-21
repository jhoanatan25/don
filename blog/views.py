from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.db.models import Q
import random
from math import ceil
from apps.forms import userForm, expForm, indexForm, signForm, userCreation
import json
from apps.models import person, body_style, make, transmission_type, drive_train, fuel_type, engine, drive, car, model, mImage, theme, favourite, blog_entry, Category
from apps.views import carCreation, logUser, useField, checkNumberOfCars

@login_required
def car_reviews(request):
    context = logUser(request)
    if not context["is_admin"]:
        return redirect("/dashboard")
    try:
        context["blog_name"] = "Car reviews"
        category = Category.objects.get(name = context["blog_name"])
        context["articles"] = blog_entry.objects.filter(category = category)
    except:
        pass
    return render(request,'pages/blog_page.html', context)

@login_required
def press_room(request):
    context = logUser(request)
    if not context["is_admin"]:
        return redirect("/dashboard")
    try:
        context["blog_name"] = "Press room"
        category = Category.objects.get(name = context["blog_name"])
        context["articles"] = blog_entry.objects.filter(category = category)
    except:
        pass
    return render(request,'pages/blog_page.html', context)

@login_required
def buying_guide(request):
    context = logUser(request)
    if not context["is_admin"]:
        return redirect("/dashboard")
    try:
        context["blog_name"] = "Buying guide"
        category = Category.objects.get(name = context["blog_name"])
        context["articles"] = blog_entry.objects.filter(category = category)
    except:
        pass
    return render(request,'pages/blog_page.html', context)

@login_required
def article(request, blog_name = None):
    context = logUser(request)
    if not context["is_admin"]:
        return redirect("/dashboard")
    context["all_categories"] = Category.objects.all()
    category = None
    _redirect = False
    context["edit"] = False
    try:
        if blog_name:
            try:
                context["blog_name"] = blog_name.replace("_", " ")
                category = Category.objects.get(name = context["blog_name"])
            except:
                context["edit"] = True
                article = blog_entry.objects.get(id = blog_name)
                context["title"] = article.title
                context["content"] = article.content
                context["blog_name"] = article.title

        if request.method == "POST":
            if not category and not context["edit"]:
                context["blog_name"] = request.POST.get("type")
                category = Category.objects.get(name = context["blog_name"])
                blog_name = context["blog_name"].replace(" ", "_")

            title = request.POST.get("title")
            content = request.POST.get("content")
            photo = request.FILES.get("arimg")
            if not context["edit"]:
                article = blog_entry.objects.create(category = category, title = title, content = content)
                page = blog_name
            else:
                page = str(article.category).replace(" ", "_")
                article.title = title
                article.content = content
                article.save()

            print("AQUI1")
            if photo is not None:
                print("AQUI")
                print(photo)
                article.image.save(photo.name, photo)
            _redirect = True
    except Exception as e:
        print(e)

    return render(request,'pages/article.html', context) if not _redirect else redirect("/dashboard/blog/" + page.lower())


@login_required
def delete(request):
    if request.method == "GET":
        context = logUser(request)
        if context["is_admin"]:
            try:
                id = request.GET.get("id")
                entry = blog_entry.objects.get(id = id)
                entry.delete()
                return HttpResponse(status=201)
            except:
                pass
    return HttpResponse(status=400)

@login_required
def published(request):
    if request.method == "GET":
        context = logUser(request)
        if context["is_admin"]:
            try:
                id = request.GET.get("id")
                entry = blog_entry.objects.get(id = id)
                entry.published = not entry.published
                entry.save()
                return HttpResponse(status=201)
            except:
                pass
    return HttpResponse(status=400)
