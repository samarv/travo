from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

from django.conf.urls import url, include

urlpatterns = [
    path('org/', views.OrganizationList.as_view()),
    path('org/<int:pk>/', views.OrganizationtDetail.as_view()),
    path('user/', views.UserList.as_view()),
    path('user/<int:pk>/', views.UserDetail.as_view()),
    path('shoutout/', views.ShoutoutList.as_view()),
    path('shoutout/<int:pk>/', views.ShoutoutDetail.as_view()),
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('command', views.command, name='command'),
    path('interactive', views.interactive, name='interactive')
]

urlpatterns = format_suffix_patterns(urlpatterns)
