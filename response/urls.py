from django.urls import path
from . import views

app_name = 'response'

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('api/data', views.get_data, name='api-data'),
    path('api/chart/data/', views.ChartData.as_view()),
]
