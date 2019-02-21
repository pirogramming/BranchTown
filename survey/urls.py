from django.urls import path
from . import views

app_name = "survey"

urlpatterns = [
    path('make/<int:pk>/choice/', views.make_multiple_choice, name='make_multiple_choice'),
    path('make/<int:pk>/text/', views.make_text_answer, name='make_text_answer'),
    # path('<int:pk>/multiple_choice/', views.multiple_choice, name='multiple_choice'),
    path('<int:pk>/results/', views.results, name='results'),
    path('mysurvey/', views.my_survey, name='my_survey'),
    path('mysurvey/<int:pk>/', views.my_survey_detail, name='my_survey_detail'),
    path('mysurvey/<int:pk>/complete/', views.my_survey_complete, name='my_survey_complete'),
]
