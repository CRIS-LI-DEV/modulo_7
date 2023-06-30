
from django.contrib import admin
from django.urls import path
from app1.views import *
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login_view/',Login_View.as_view(),name="LOGIN"),
    path('logout_view/',logout_view,name="LOGOUT"),
    path('perfil/',login_required(perfil),name="PERFIL"),
    path('inicio/',inicio,name="INICIO"),
    path('',inicio,name="INICIO"),
    path('registro_tareas/',registro_tareas,name="INICIO"),

]
