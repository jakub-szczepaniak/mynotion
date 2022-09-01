"""mynotion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def notes(request, note=''):
    status_code = 200
    if note == '':
        note = 'New-note'
        status_code = 301
    value = HttpResponse('This is the main page for notes' + str(note))
    value.headers['Location'] = note
    value.status_code = status_code
    print(value.headers) 
    return value


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', notes),
    path('<slug:note>', notes),
]
