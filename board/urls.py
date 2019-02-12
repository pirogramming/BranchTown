from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.survey_list),
    path('<int:pk>/', views.survey_detail, name='survey_detail'),

    path('interest/', views.survey_interest, name='survey_interest'),
    path('tag/<int:pk>/', views.survey_tag, name='survey_tag'),
    path('hot/', views.survey_hot, name='board_hot'),
    path('ongoing/', views.survey_ongoing, name='board_ongoing'),
    path('answer/', views.survey_answer, name='board_answer'),
    path('finish/', views.survey_finish, name='board_finish'),
    path('recent/', views.survey_recent, name='board_recent'),
]
