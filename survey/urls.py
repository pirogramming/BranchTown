from django.urls import path
from . import views

app_name = "survey"

urlpatterns = [
    path('make/', views.make_survey, name='make_form'),
    path('make/index/', views.make_index, name='make_index'),
    path('make/field/<int:pk>', views.make_field, name='make_field'),
]
