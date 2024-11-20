import datetime
from django.shortcuts import render, redirect, reverse
from main.forms import productEntryForm
from main.models import productEntry
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse

@login_required(login_url='/login')

def show_main(request):
    #product_entries = productEntry.objects.filter(user=request.user)
    context = {
        'application' : 'Trubuy',
        'self_name': request.user.username,
        'class': 'PBP F',
        'npm': '2306275960',
        'last_login': request.COOKIES.get('last_login', str(datetime.datetime.now())),
        #'product_entries': product_entries,
    }

    return render(request, "main.html", context)
 
def add_product(request):
    form = productEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        productEntry = form.save(commit=False)
        productEntry.user = request.user
        productEntry.save()

        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "add_product.html", context)

def show_xml(request):
    data = productEntry.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = productEntry.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = productEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = productEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
        
    context = {'form':form}
    return render(request, 'register.html', context)


def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.error(request, "Invalid username or password. Please try again.")
        
    else:
        form = AuthenticationForm(request)
    context = {'form': form}

    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_product(request, id):
    product = productEntry.objects.get(pk = id)
    form = productEntryForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)

def delete_product(request, id):
    product = productEntry.objects.get(pk = id)
    product.delete()

    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    product = strip_tags(request.POST.get("product"))
    price = request.POST.get("price")
    description = strip_tags(request.POST.get("description"))
    rating = request.POST.get("rating")
    quantity = request.POST.get("quantity")
    user = request.user

    new_product = productEntry(
        product=product, price=price, description=description,
        rating=rating, quantity=quantity, user=user
    )
    new_product.save()

    return HttpResponse(b"CREATED", status=201)

@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':

        data = json.loads(request.body)
        new_product = productEntry.objects.create(
            user=request.user,
            name=data["name"],
            price=int(data["price"]),
            quantity=int(data["quantity"]),
            rating=data["rating"],
            description=data["desqription"],
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)