from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from . import models

# Create your views here.
from .models import Electronics


menu = [
    {'title': 'Home', 'url_name': 'home'},
    {'title': 'Visual', 'url_name': 'search'},
    {'title': 'Inserimento', 'url_name': 'categories'}
]


def home(request):
    title = 'Home'
    return render(request, 'electronics/index.html', {'title': title})


def data_visualization(request):
    title = 'Visual'
    if request.GET:

        marca: str = request.GET.get('modello')
        print(f'{"-" * 50}\n\n')
        print(request.GET)

        lst = Electronics.objects.filter(title__istartswith=marca)
        data_s = [(query.title, query.content) for query in lst]

        return render(request, 'electronics/data_visual.html', {'extracted_data': data_s, 'title':title})
    data_s = []
    return render(request, 'electronics/data_visual.html', {'extracted_data': data_s, 'title':title})


def categories(request):
    title = "Inserimento"
    if request.GET:
        marca: str = request.GET.get('marca').capitalize()
        model: str = request.GET.get('modello').capitalize()
        print(f'{"-" * 50}\n\n')
        print(marca, model)
        print(request.GET)
        dt = models.Electronics(title=marca, content=model)
        dt.save()
        print(f'\n\n{"-" * 50}')
    return render(request, 'electronics/data_insetion.html', {'title':title})


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Ops! pagina inesistente!</h1>')



