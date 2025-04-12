from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .models import PageHub, SubCategoria

def index(request):
    return render(request, 'pagehub/index.html')

class PageHubView(View):
    def get(self, request):
        if 'json' in request.GET:
            categorias = PageHub.CategoriaPrincipal.choices
            sub_categorias = SubCategoria.objects.all().values('id', 'sub_categoria')
            return JsonResponse({
                'categorias': categorias,
                'sub_categorias': list(sub_categorias),
            })
        return render(request, 'pagehub/cargar_page.html')

    def post(self, request):
        try:
            nombre = request.POST.get('nombre')
            link = request.POST.get('link')
            categoria_principal = request.POST.get('categoria')
            descripcion = request.POST.get('descripcion')
            sub_categorias_ids = request.POST.getlist('sub_categoria')
            foto = request.FILES.get('foto')

            # Crea el objeto PageHub
            pagehub = PageHub.objects.create(
                nombre=nombre,
                link=link,
                categoria_principal=categoria_principal,
                descripcion=descripcion,
                foto=foto
            )
            pagehub.sub_categoria.set(sub_categorias_ids)

            return JsonResponse({'message': 'PageHub creada con éxito'})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)