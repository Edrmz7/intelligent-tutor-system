from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserRegisterSerializer
from django.shortcuts import render
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.decorators.cache import never_cache
from django.contrib import messages
from .models import User, Exam
import g4f
import json

@never_cache
def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect("home") 
        else:
            messages.error(request, "Correo o contraseña incorrectos.")
    
    return render(request, "login.html")  # Asegura que siempre se renderiza la plantilla


def home(request):
    # Verificar si el usuario está autenticado
    if request.user.is_authenticated:
        # Consultar si el usuario ya tiene un examen registrado
        examen_realizado = Exam.objects.filter(user=request.user).exists()
    else:
        examen_realizado = False

    return render(request, 'inicio.html', {'examen_realizado': examen_realizado})

def tutor(request):
    return render(request, 'tutor.html')

def exam(request):
    return render(request, 'exam.html')

# views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import User, Exam

@login_required
def perfil_usuario(request):
    user = request.user  # Obtén el usuario autenticado
    try:
        # Si el usuario tiene un examen realizado, obtenemos los detalles de su examen más reciente
        examen = Exam.objects.filter(user=user).order_by('-date').first()
    except Exam.DoesNotExist:
        examen = None  # Si no tiene examen, asignamos None

    context = {
        'user': user,
        'examen': examen,
    }

    return render(request, 'info.html', context)



@csrf_exempt
def update_user_exam(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            score = data.get("score")
            level = data.get("level")
            user = request.user  # Asegúrate de que el usuario esté autenticado

            if not user.is_authenticated:
                return JsonResponse({"error": "Usuario no autenticado"}, status=401)

            # Marcar el examen como completado
            user.examen = True
            user.level = level
            user.save()

            # Crear un nuevo registro en la tabla Exam
            Exam.objects.create(user=user, exam_name="Examen de programación", score=score)

            return JsonResponse({"message": "Examen actualizado correctamente"})
        except json.JSONDecodeError:
            return JsonResponse({"error": "Error en el formato JSON"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    
    return JsonResponse({"error": "Método no permitido"}, status=405)


class ChatView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def post(self, request):
        try:
            data = json.loads(request.body)
            messages = data.get("messages", [])
            
            response = g4f.ChatCompletion.create(
                model=g4f.models.default,
                messages=messages
            )
            
            return JsonResponse({"response": response})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

class UserRegisterView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Usuario registrado correctamente"},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)