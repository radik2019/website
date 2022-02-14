
from django.contrib import admin
from django.urls import path, include
from electronics.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('electronics.urls'))
]

handler404 = pageNotFound

