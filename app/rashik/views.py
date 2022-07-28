from django.shortcuts import render
from django.http import HttpResponse
from .models import Image

def index(request):
    images = Image.objects.all()
    context = {
        "images": images
    }
    return render(request, 'rashik/index.html', context)
