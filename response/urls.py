from django.urls import path
from . import views


app_name = 'response'

urlpatterns = [
    path('result/<int:pk>', views.ResultView.as_view(), name="home"),

]
