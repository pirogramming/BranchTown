from django.conf import settings
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('signup/', views.signup, name='signup'),
    path('signup2/', views.signup2, name='signup2'),
    path('login/', views.login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page=settings.LOGIN_URL), name='logout',
         kwargs={'next_page': settings.LOGIN_URL}),
]
