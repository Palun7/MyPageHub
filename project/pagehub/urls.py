from django.urls import path
from pagehub.views import index, PageHubView, categoria_view, Cargar_Sub, obtener_subcategorias

app_name = 'pagehub'

urlpatterns = [
    path('', index.as_view(), name='index'),
    path('cargar_page/', PageHubView.as_view(), name='cargar_page'),
    path('categoria/<str:categoria>/', categoria_view, name='categoria'),
    path('cargar_sub_categoria/', Cargar_Sub.as_view(), name='cargar_sub_categoria'),
    path('subcategorias/<str:categoria_nombre>/', obtener_subcategorias, name='obtener_subcategorias'),
]