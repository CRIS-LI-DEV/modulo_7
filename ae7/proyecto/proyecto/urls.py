
from django.contrib import admin
from django.urls import path
from app1.views import *
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login_view/',Login_View.as_view(),name="LOGIN"),
    path('logout_view/', login_required(logout_view), name="LOGOUT"),
    path('perfil/',login_required(perfil),name="PERFIL"),
    path('inicio/',inicio,name="INICIO"),
    path('',inicio,name="INICIO"),
    path('registro_tareas/', login_required(RegistroTareas.as_view()), name="INICIO"),
    path('filtro/', login_required(funcion_filtro), name="FILTRO"),
    path('tarea/<int:id_tarea>', login_required(tarea), name="TAREA"),
    path('eliminar_tarea/<int:id_tarea>', login_required(eliminar_tarea), name="ELIMINAR_TAREA"),
    path('completar_tarea/<int:id_tarea>', login_required(completar_tarea), name="COMPLETAR_TAREA"),
    path('editar_tarea/<int:id_tarea>',login_required(editar_tarea),name="EDITAR_TAREA"),
    path('agregar_observacion/',login_required(agregar_observacion),name="OBSERVACION"),
    path('editar_ob/<int:id_ob>/<int:id_tarea>',  login_required(editar_ob),  name="OBSERVACION-EDITAR"),
    path('borrar_ob/<int:id_ob>/<int:id_tarea>', login_required(borrar_ob),  name="BORRAR-EDITAR")
   


]
