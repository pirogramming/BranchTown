from django.urls import path
from . import views


app_name = 'response'

urlpatterns = [
<<<<<<< HEAD
    path('result/<int:pk>', views.ResultView.as_view(), name="home"),
=======
    path('result/<int:pk>/', views.HomeView.as_view(), name="home"),
    path('<int:pk>/preview/', views.preview_survey, name='preview_survey'),
    path('<int:pk>/survey/', views.response_survey, name='response_survey'),
    path('<int:pk>/join/', views.join_survey, name='join_survey'),
>>>>>>> f17008f429dec73ba4e8a8288f23dd69daa778c5

    # path('<int:pk>/survey/text/', views.response_survey_text, name='response_survey_text')
]
