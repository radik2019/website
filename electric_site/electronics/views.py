
from datetime import datetime
from django.shortcuts import redirect
from http import HTTPStatus
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

        if request.method == "GET":
            data = serializers.serialize('json',
                                         Electronics.objects.all(),
                                         fields=('title', 'content','time_create',  'time_update'),
                                         indent=4)
            return HttpResponse(data)
        raise Http404("**Error**")

    @csrf_exempt
    def update_article(self, request):

        if request.method == "POST":
            df = json.loads(request.body)
            query = Electronics.objects.filter(content=df['model'])
            if query:
                query.update(title=df["updated_brand"],
                            content=df["updated_model"],
                            time_update=datetime.now())
                srlzd = serializers.serialize('json',
                                            query,
                                        fields=('id', 'title', 'content', 'time_create', 'time_update'),
                                        indent=4)
                return HttpResponse(srlzd)
            return HttpResponse(request.body, status=404)
        return HttpResponse('df[0]', status=405)

    @csrf_exempt
    def searche_by_brand(self, request, brand_name_product):
        data = serializers.serialize('json',
                                     Electronics.objects.filter(title__istartswith=brand_name_product),
                                     fields=('id', 'title', 'content', 'time_create', 'time_update'),
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

def updated(request, article_id):
    title = "Updated"

    data_s = Electronics.objects.filter(pk=article_id)
    if request.method == "GET":
        marca: str = request.GET.get('marca')
        model: str = request.GET.get('modello')
        if marca and model:
            data_s.update(title=marca,
                            content=model,
                            time_update=datetime.now())
        data_s = Electronics.objects.get(pk=article_id)
    return render(request, 'electronics/updated.html',
                  {'title': title,
                  'extracted_data': data_s,
                  'url_update': 'update/'
                  })

    
def detailed_data(request, article_id):
    title = 'Single Data'
    data_s = Electronics.objects.get(pk=article_id)
    return render(request,
                  'electronics/generated_visual.html',
                  {'title': title,
                  'extracted_data': data_s,
                  'url_update': 'update/'
                  })


def update_data(request, article_id):

    title="Update"
    data_s = Electronics.objects.get(pk=article_id)
    if request.method == "GET":
        marca: str = request.GET.get('marca')
        model: str = request.GET.get('modello')

    return render(request,
                  'electronics/update_data.html',
                  {
                  'title':title,
                  'extracted_data': data_s,
                  'url_update': 'updated/'
                  
                  })


def delete_data(request, article_id):
    data_s = Electronics.objects.get(pk=article_id)
    data_s.delete()
    return redirect('/all_article/')
    
 
def show_all_article(request):
    data_s = Electronics.objects.all()    
    title = 'All_article'
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
        if marca:
            lst = Electronics.objects.filter(title__istartswith=marca)
            data_s = [(query.title, query.content) for query in lst]
        else: data_s = []
        return render(request, 'electronics/data_visual.html', {'extracted_data': data_s, 'title':title})
    data_s = []
    return render(request, 'electronics/data_visual.html', {'extracted_data': data_s, 'title':title})


def categories(request):
    title = "Inserimento"
    if request.method == "POST":
        marca: str = request.POST.get('marca').capitalize()
        model: str = request.POST.get('modello').capitalize()
        if marca and model:
            dt = models.Electronics(title=marca, content=model)
            dt.save()
    return render(request, 'electronics/data_insetion.html', {'title':title})


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Ops! pagina inesistente!</h1>')



