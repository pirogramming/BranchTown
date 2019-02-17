from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.mainpage, name='mainpage'),
    path('into/', views.intropage, name='intropage'),

]
