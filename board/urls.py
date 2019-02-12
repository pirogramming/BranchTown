from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.survey_list),
    path('<int:pk>/', views.survey_detail, name='survey_detail'),
]
