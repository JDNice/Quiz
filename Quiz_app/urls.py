from django.urls import path
from . import views

urlpatterns = [
    path('', views.start, name='home'),
    path('question', views.question, name='question'),
    path('results', views.result, name='results'),
]
