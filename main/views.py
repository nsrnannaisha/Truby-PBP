from django.shortcuts import render

def show_main(request):
    context = {
        'application' : 'Trubuy',
        'name': 'Nisrina Annaisha Sarnadi',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)
