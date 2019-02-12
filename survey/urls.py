from django.urls import path
from . import views

app_name = "survey"

urlpatterns = [
    path('make/', views.make_survey, name='make_form'),
    path('make/field/<int:pk>', views.make_field, name='make_field'),
]
