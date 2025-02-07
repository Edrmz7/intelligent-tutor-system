from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
      path('', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),  # Logout
    path('home/', views.inicio, name='home'),
    path('api-chat/', views.ChatView.as_view(), name='api-chat'),
    path('tutor/', views.tutor, name='tutor'),
    path('exam/', views.exam, name='exam'),
    path('register/', views.UserRegisterView.as_view(), name='user-register'),
]
