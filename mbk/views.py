from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def registre(request):
    return render(request, 'mbk/registre.html', {})