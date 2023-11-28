from django.shortcuts import render

# Create your views here.
#Http Request

def home(request):
    return render(request, 'recipes/pages/home.html', context = {
        'name' : 'Pedro Delduck Castrequini',
    })