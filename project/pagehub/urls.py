from django.urls import path
from pagehub.views import index, PageHubView, categoria_view, Cargar_Sub

app_name = 'pagehub'

urlpatterns = [
    path('', index.as_view(), name='index'),
    path('cargar_page/', PageHubView.as_view(), name='cargar_page'),
    path('categoria/<str:categoria>/', categoria_view, name='categoria'),
    path('cargar_sub_categoria/', Cargar_Sub.as_view(), name='cargar_sub_categoria'),
]