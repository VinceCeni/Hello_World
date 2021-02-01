from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    names = ["Vince", "Jon", "Scott", "Mike"]
    context = {
        'names': names,
    }
    return render (request, "home.html", context)