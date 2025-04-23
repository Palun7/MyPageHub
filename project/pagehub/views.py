from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .models import PageHub, SubCategoria



def categoria_view(request, categoria):
    pages = PageHub.objects.filter(categoria_principal=categoria)
    return render(request, 'pagehub/categoria.html', {'pages': pages, 'categoria': categoria})

class index(View):
    def get(self, request):
        categorias = PageHub.CategoriaPrincipal.choices
        return render(request, 'pagehub/index.html', {'categorias': categorias})

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

            pagehub = PageHub.objects.create(
                nombre=nombre,
                link=link,
                categoria_principal=categoria_principal,
                descripcion=descripcion,
                foto=foto
            )
            pagehub.sub_categoria.set(sub_categorias_ids)

            return JsonResponse({'success': 'PageHub creada con éxito'})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

class Cargar_Sub(View):
    def get(self, request):
        return render(request, 'pagehub/cargar_sub_categoria.html')

    def post(self, request):
        try:
            sub_categoria = request.POST.get('sub_categoria')

            if SubCategoria.objects.filter(sub_categoria=sub_categoria).exists():
                return JsonResponse({'error': 'La Sub_categoría ya existe'}, status=400)

            SubCategoria.objects.create(
                sub_categoria=sub_categoria,
            )

            return JsonResponse({'success': 'Sub_categoría creada con éxito'})

        except Exception as e:
            return JsonResponse({'error': 'Error al crear la subcategoría'}, status=400)