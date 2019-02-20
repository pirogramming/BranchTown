from django.urls import path
from . import views

app_name = 'response'

urlpatterns = [
    path('result/<int:pk>/', views.HomeView.as_view(), name="home"),
    path('<int:pk>/preview/', views.preview_survey, name='preview_survey'),
    path('<int:pk>/survey/', views.response_survey, name='response_survey'),

    path('<int:pk>/survey/text/', views.response_survey_text, name='response_survey_text')
]
