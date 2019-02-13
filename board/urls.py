from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    # path('', views.survey_list),
    path('<int:pk>/', views.survey_detail, name='survey_detail'),

    path('', views.main, name='main'),
    path('interest/', views.survey_interest, name='survey_interest'),
    path('tag/<int:pk>/', views.survey_tag, name='survey_tag'),
    path('hot/', views.survey_hot, name='survey_hot'),
    path('ongoing/', views.survey_ongoing, name='survey_ongoing'),
    path('answer/', views.survey_answer, name='survey_answer'),
    path('complete/', views.survey_complete, name='survey_complete'),
    path('recent/', views.survey_recent, name='survey_recent'),
]
