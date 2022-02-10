from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from . import models

# Create your views here.
from .models import Electronics


def home(request):
    title = 'Home'
    return render(request, 'electronics/index.html', {'title': title})

def data_visualization(request):
    if request.GET:

        marca: str = request.GET.get('modello')
        print(f'{"-" * 50}\n\n')
        print(request.GET)

        lst = Electronics.objects.filter(title__istartswith=marca)
        data_s = [(query.title, query.content) for query in lst]

        return render(request, 'electronics/data_visual.html', {'extracted_data': data_s})


    return HttpResponse("""<!DOCTYPE html>
        <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <link rel="stylesheet" href="mystyle.css">
                <title>Document</title>
        
            </head>
            
            <body>
            <p><h1>Visualizzazione dati</h1></p>
                <h2>Cerca dati nel database</h2>
        
                <form action="/search">
                    <label for="modello"> nome del modello:</label>
                    <input type="text" id="modello" name="modello"><br><br>
                    <input type="submit" value="Cerca">
                </form>
        
        
            </body>
        </html>""")




def categories(request):
    if request.GET:

        marca: str = request.GET.get('marca').capitalize()
        model: str = request.GET.get('modello').capitalize()
        print(f'{"-" * 50}\n\n')
        print(marca, model)
        print(request.GET)
        dt = models.Electronics(title=marca, content=model)
        dt.save()
        print(f'\n\n{"-" * 50}')
        

    return HttpResponse("""<!DOCTYPE html>
        <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <link rel="stylesheet" href="mystyle.css">
                <title>Document</title>
        
            </head>
            
            <body>
                <h1>Inserimento dei dati nel database</h1>
        
                <form action="/categories">
                    <label for="marca">Marca:</label>
                    <input type="text" id="marca" name="marca"><br><br>
                    <label for="modello">Modello:</label>
                    <input type="text" id="modello" name="modello"><br><br>
                    <input type="submit" value="Inserisci">
                </form>
        
                <p>Clicca "Inserisci"</p>
        
            </body>
        </html>""")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Ops! pagina inesistente!</h1>')



