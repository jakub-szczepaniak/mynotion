from django.urls import path
from . import views

urlpatterns = [
    path('', views.notes),
    path('notes/<slug:note>', views.note),
]