from django.shortcuts import render

def show_main(request):
    context = {
        'application' : 'Trubuy',
        'self_name': 'Nisrina Annaisha Sarnadi',
        'class': 'PBP F',
        'name': 'BRUNBÅGE Desk Lamp',
        'price': 'Rp349.000',
        'description': 'LED desk lamp with a storage that can be dimmed' ,
        'rating': '5/5',
        'quantity': '17'
    }

    return render(request, "main.html", context)
