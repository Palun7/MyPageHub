from django.urls import path
from .views import index
from django.contrib.auth.views import LogoutView


app_name = 'usuarios'

urlpatterns = [
    path('', index.as_view(), name='index'),
    path('logout/', LogoutView.as_view(template_name='usuarios/logout.html'), name='logout'),
]