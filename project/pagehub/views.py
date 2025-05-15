from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .models import PageHub, SubCategoria
from django.conf import settings


def categoria_view(request, categoria):
    pages = PageHub.objects.filter(categoria_principal=categoria).values('sub_categoria', 'id', 'nombre', 'link', 'foto', 'descripcion')
    return render(request, 'pagehub/categoria.html', {
        'pages': pages,
        'categoria': categoria,
        'MEDIA_URL': settings.MEDIA_URL
    })

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
            sub_categoria = request.POST.get('sub_categoria')
            foto = request.FILES.get('foto')

            PageHub.objects.create(
                nombre=nombre,
                link=link,
                categoria_principal=categoria_principal,
                descripcion=descripcion,
                foto=foto,
                sub_categoria=sub_categoria,
            )

            return JsonResponse({'success': 'PageHub creada con éxito'})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

class Cargar_Sub(View):
    def get(self, request):
        categorias = SubCategoria.CategoriaPrincipal.choices
        print(categorias)
        return render(request, 'pagehub/cargar_sub_categoria.html', {'categoria': categorias})

    def post(self, request):
        try:
            categoria_principal = request.POST.get('categoria')
            sub_categoria = request.POST.get('sub_categoria')

            print(categoria_principal, sub_categoria)

            if not categoria_principal or not sub_categoria:
                return JsonResponse({'error': 'Los campos no pueden estar vacíos'}, status=400)

            if SubCategoria.objects.filter(sub_categoria=sub_categoria).exists():
                return JsonResponse({'error': 'La Sub_categoría ya existe'}, status=400)

            SubCategoria.objects.create(
                categoria_principal=categoria_principal,
                sub_categoria=sub_categoria,
            )

            return JsonResponse({'success': 'Sub-categoría creada con éxito'})

        except Exception as e:
            return JsonResponse({'error': 'Error al crear la subcategoría'}, status=400)

def obtener_subcategorias(request, categoria_nombre):
    subcategorias = SubCategoria.objects.filter(categoria_principal=categoria_nombre)
    data = [{'id': sc.id, 'nombre': sc.sub_categoria} for sc in subcategorias]
    return JsonResponse(data, safe=False)