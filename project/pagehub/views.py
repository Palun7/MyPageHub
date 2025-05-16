from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .models import PageHub, SubCategoria, CategoriaPrincipal
from django.conf import settings
from django.shortcuts import get_object_or_404
from collections import defaultdict


def categoria_view(request, categoria_id):
    categoria_obj = get_object_or_404(CategoriaPrincipal, id=categoria_id)
    pages_qs = PageHub.objects.filter(categoria_principal=categoria_obj)

    pages_por_subcategoria = defaultdict(list)
    for page in pages_qs:
        sub = page.sub_categoria.sub_categoria if page.sub_categoria else "Sin subcategoría"
        pages_por_subcategoria[sub].append(page)

    return render(request, 'pagehub/categoria.html', {
        'pages_por_subcategoria': dict(pages_por_subcategoria),
        'categoria': categoria_obj.nombre,
        'MEDIA_URL': settings.MEDIA_URL
    })

class index(View):
    def get(self, request):
        categorias = CategoriaPrincipal.objects.filter(user=request.user).values('id', 'nombre')
        return render(request, 'pagehub/index.html', {'categorias': categorias})

class PageHubView(View):
    def get(self, request):
        if 'json' in request.GET:
            categorias = list(CategoriaPrincipal.objects.filter(user=request.user).values('id', 'nombre'))
            sub_categorias = list(SubCategoria.objects.all().values('id', 'sub_categoria'))
            return JsonResponse({
                'categorias': categorias,
                'sub_categorias': list(sub_categorias),
            })
        return render(request, 'pagehub/cargar_page.html')

    def post(self, request):
        try:
            nombre = request.POST.get('nombre')
            link = request.POST.get('link')
            categoria_id = request.POST.get('categoria')
            descripcion = request.POST.get('descripcion')
            sub_categoria_id = request.POST.get('sub_categoria')
            foto = request.FILES.get('foto')
            user = request.user

            categoria = get_object_or_404(CategoriaPrincipal, id=categoria_id)
            sub_categoria = get_object_or_404(SubCategoria, id=sub_categoria_id)

            PageHub.objects.create(
                nombre=nombre,
                link=link,
                categoria_principal=categoria,
                descripcion=descripcion,
                foto=foto,
                sub_categoria=sub_categoria,
                user=user,
            )

            return JsonResponse({'success': 'PageHub creada con éxito'})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

class Cargar_Sub(View):
    def get(self, request):
        categorias = list(CategoriaPrincipal.objects.all().values('id', 'nombre'))
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

            categoria = get_object_or_404(CategoriaPrincipal, id=categoria_principal)

            SubCategoria.objects.create(
                categoria_principal=categoria,
                sub_categoria=sub_categoria,
            )

            return JsonResponse({'success': 'Sub-categoría creada con éxito'})

        except Exception as e:
            return JsonResponse({'error': 'Error al crear la subcategoría'}, status=400)

def obtener_subcategorias(request, categoria_nombre):
    subcategorias = SubCategoria.objects.filter(categoria_principal=categoria_nombre)
    data = [{'id': sc.id, 'nombre': sc.sub_categoria} for sc in subcategorias]
    return JsonResponse(data, safe=False)

class CargarCategoria(View):
    def get(self, request):
        return render(request, 'pagehub/cargar_categoria.html')

    def post(self, request):
        try:
            nombre = request.POST.get('categoria')
            user = request.user
            print(nombre)
            if CategoriaPrincipal.objects.filter(nombre=nombre).exists():
                return JsonResponse({'error': 'La categoría ya existe'}, status=400)

            CategoriaPrincipal.objects.create(nombre=nombre, user=user)
            return JsonResponse({'success': 'Categoría creada con éxito'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)