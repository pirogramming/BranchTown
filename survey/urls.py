from django.urls import path
from . import views

app_name = "survey"

urlpatterns = [
    path('make/', views.make_survey, name='make_form'),
    path('make/index/', views.make_index, name='make_index'),
    path('<int:pk>', views.make_field, name='make_field'),
    path('<int:pk>/multiple_choice/', views.multiple_choice, name='multiple_choice'),
    path('<int:pk>/results/', views.results, name='results'),

]
