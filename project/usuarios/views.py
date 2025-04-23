import json
from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Usuario, validate_image
from django.forms import ValidationError


class index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'usuarios/index.html')

    def post(self, request):
        try:
            if request.content_type == 'application/json':
                data = json.loads(request.body)
                action = data.get('action')
            else:
                action = request.POST.get('action')

            if action == 'register':
                return self.register_user(request)
            elif action == 'login':
                return self.login_user(request, data)
            else:
                return JsonResponse({'error': 'Acción no válida'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Formato de solicitud inválido'}, status=400)

    def register_user(self, request):
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            nombre = request.POST.get('nombre')
            apellido = request.POST.get('apellido')
            mail = request.POST.get('mail')
            foto = request.FILES.get('foto')

            if User.objects.filter(username=username).exists():
                return JsonResponse({'error': 'El usuario ya existe'}, status=400)

            if Usuario.objects.filter(mail=mail).exists():
                return JsonResponse({'error': 'El mail ya está cargado'}, status=400)

            if foto:
                try:
                    validate_image(foto)
                except ValidationError as e:
                    return JsonResponse({'error': str(e)}, status=400)

            username = User.objects.create_user(username=username, password=password)
            Usuario.objects.create(
                username=username,
                nombre=nombre,
                apellido=apellido,
                mail=mail,
                foto=foto
            )
            return JsonResponse({'success': f'{username} se ha registrado con éxito'})
        except Exception:
            return JsonResponse({'error': 'Error al intentar registrar, verifique los datos'}, status=500)

    def login_user(self, request, data):
        try:
            username = data.get('username')
            password = data.get('password')

            if not username or not password:
                return JsonResponse({'error': 'Usuario y contraseña son requeridos'}, status=400)

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return JsonResponse({'success': f'{username} ha iniciado sesión'})
            else:
                return JsonResponse({'error': 'Usuario o contraseña incorrectos'}, status=401)
        except Exception:
            return JsonResponse({'error': 'Error interno del servidor al iniciar sesión'}, status=500)
