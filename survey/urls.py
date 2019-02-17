from django.urls import path
from . import views

app_name = "survey"

urlpatterns = [

    path('make/', views.make_survey, name='make_survey'),
    path('make/<int:pk>/', views.make_index, name='make_index'),
    path('make/<int:pk>/field/mul', views.make_field_mul, name='make_field_mul'),
    path('make/<int:pk>/field/txt', views.make_field_txt, name='make_field_txt'),
    path('make/test', views.this_is_test, name='test'),

    path('<int:pk>/results/', views.results, name='results'),

]
