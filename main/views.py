from django.shortcuts import render, redirect
from main.forms import ProductEntryForm
from main.models import ProductEntry
from django.http import HttpResponse
from django.core import serializers

def show_main(request):
    product_entries = ProductEntry.objects.all()

    context = {
        'application' : 'Trubuy',
        'self_name': 'Nisrina Annaisha Sarnadi',
        'class': 'PBP F',
        'name': 'BRUNBÅGE Desk Lamp',
        'price': 'Rp349.000',
        'description': 'LED desk lamp with a storage that can be dimmed' ,
        'rating': '5/5',
        'quantity': '17',
        'product_entries': product_entries,

    }

    return render(request, "main.html", context)

def add_product(request):
    form = ProductEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "add_product.html", context)

def show_xml(request):
    data = ProductEntry.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = ProductEntry.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = ProductEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = ProductEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")