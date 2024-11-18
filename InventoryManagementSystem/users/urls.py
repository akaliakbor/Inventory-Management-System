from django.urls import path, include, re_path
from .views import user_login
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [
    path('login/', user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout')
]