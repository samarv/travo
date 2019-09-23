from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('command', views.command, name='command'),
    path('interactive', views.interactive, name='interactive'),
]
