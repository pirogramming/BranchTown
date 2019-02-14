from django.urls import path
from . import views

app_name = "survey"

urlpatterns = [
    path('make/index/', views.index, name='index'),
    path('make/', views.make_survey, name='make_form'),
    # path('make/field/<int:pk>', views.make_field, name='make_field'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('<int:question_id>/results/', views.results, name='results'),
]
