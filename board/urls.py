from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('list/', views.survey_list),
    path('<int:pk>/', views.survey_detail, name='survey_detail'),

    path('', views.main, name='main'),

    path('interest/', views.survey_interest, name='survey_interest'),
    path('recent/', views.survey_recent, name='survey_recent'),

    path('ongoing/', views.survey_ongoing, name='survey_ongoing'),
    path('complete/', views.survey_complete, name='survey_complete'),

    path('tag/<int:pk>/', views.survey_tag, name='survey_tag'),

]
