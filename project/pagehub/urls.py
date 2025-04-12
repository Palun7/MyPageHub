from django.urls import path
from pagehub.views import index, PageHubView

app_name = 'pagehub'

urlpatterns = [
    path('', index, name='index'),
    path('cargar_page/', PageHubView.as_view(), name='cargar_page'),
]