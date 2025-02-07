from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import g4f
import json


# Create your views here.

def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, username=email, password=password)  # Usar email

        if user:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Usuario o contraseña incorrectos")

    return render(request, "login.html")

def inicio(request):
    return render(request, 'inicio.html')

def tutor(request):
    return render(request, 'tutor.html')

def exam(request):
    return render(request, 'exam.html')

def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "Usuario registrado con éxito", "user": UserSerializer(user).data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# backend
class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


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

