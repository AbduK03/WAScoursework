from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
    path('', views.index, name='index'),
    # about page url mapping
    path('about/', views.about, name='about')
]
