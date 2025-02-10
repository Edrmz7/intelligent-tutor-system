from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views


urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),  # Logout
    path('home/', views.home, name='home'),
    path('api-chat/', views.ChatView.as_view(), name='api-chat'),
    path('tutor/', views.tutor, name='tutor'),
    path('exam/', views.exam, name='exam'),
    path('register/', views.UserRegisterView.as_view(), name='user-register'),
    path("update-user-exam/", views.update_user_exam, name="update-user-exam"),
     path("info-user/", views.perfil_usuario, name="info-user"),
]