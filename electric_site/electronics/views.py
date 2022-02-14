
from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404, QueryDict
from . import models
from django.core import serializers
import json
from .models import Electronics
from django.views.decorators.csrf import csrf_exempt


menu = [
    {'title': 'Home', 'url_name': 'home'},
    {'title': 'Visual', 'url_name': 'search'},
    {'title': 'Inserimento', 'url_name': 'categories'}
]


def debug_(s):
    print('*' * 50,'\n\n\n\n', s, '\n\n\n\n', '*' * 50)


class SerData:

    @csrf_exempt
    def all_data(self, request):
        debug_(request.method)
        if request.method == "GET":
            data = serializers.serialize('json',
                                         Electronics.objects.all(),
                                         fields=('title', 'content','time_create',  'time_update'),
                                         indent=4)
            return HttpResponse(data)
        raise Http404("****************Error*****************")


    @csrf_exempt
    def update_article(self, request):

        if request.method == "POST":
            df = json.loads(request.body)
            print(df)
            brand: str = request.POST.get('brand')
            model: str = request.POST.get('model')
            print('~~~~~~~~~~~~~~~~~~~~~~~',brand)            
            print('               ', brand, model)
            df = Electronics.objects.filter(content=df['model'])
            
            srlzd = serializers.serialize('json',
                                          df,
                                     fields=('title', 'content', 'time_create', 'time_update'),
                                     indent=4)
            print(srlzd)
            return HttpResponse(srlzd)
        return HttpResponse('df[0]')


    @csrf_exempt
    def searche_by_brand(self, request, brand_name_product):
        data = serializers.serialize('json',
                                     Electronics.objects.filter(title__istartswith=brand_name_product),
                                     fields=('title', 'content', 'time_create', 'time_update'),
                                     indent=4)
        return HttpResponse(data)

    @csrf_exempt
    def post_(self, request):
        if request.method == "POST":
            brand: str = request.POST.get('brand')
            model: str = request.POST.get('model')
            
            if (brand and model):
                dt = models.Electronics(title=brand, content=model)
                dt.save()
                return HttpResponse("ok")
            return HttpResponse('no data')
        return HttpResponse('no data')


def detailed_data(request, article_id):
    title = 'Single Data'
    data_s = Electronics.objects.get(pk=article_id)
    return render(request,
                  'electronics/generated_visual.html',
                  {'title': title, 'extracted_data': data_s})

 
def show_all_article(request):

    data_s = Electronics.objects.all()    
    title = 'All_article'
    print('\n\n\n')
    return  render(request,
                   'electronics/all_article.html',
                   {'title': title, 'extracted_data': data_s})


def home(request):
    title = 'Home'
    return render(request,
                  'electronics/index.html',
                  {'title': title})


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
    
    if request.method == "POST":
        marca: str = request.POST.get('marca').capitalize()
        model: str = request.POST.get('modello').capitalize()
        print(f'{"-" * 50}\n\n')
        print(marca, model)
        print(request.POST)
        dt = models.Electronics(title=marca, content=model)
        dt.save()
        print(f'\n\n{"-" * 50}')
    return render(request, 'electronics/data_insetion.html', {'title':title})


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Ops! pagina inesistente!</h1>')



