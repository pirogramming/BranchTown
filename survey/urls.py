from django.urls import path
from . import views

app_name = "survey"

urlpatterns = [
    path('make/', views.make_survey, name='make_survey'),
    path('make/<int:pk>/', views.make_index, name='make_index'),
    path('make/<int:pk>/field', views.make_field, name='make_field'),

    path('make/<int:pk>/new', views.make_field_new, name='make_field_new'),

    path('<int:pk>/multiple_choice/', views.multiple_choice, name='multiple_choice'),
    path('<int:pk>/results/', views.results, name='results'),

]
