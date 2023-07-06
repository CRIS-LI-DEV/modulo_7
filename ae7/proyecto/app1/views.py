from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from app1.forms import *
from app1.models import *
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

# Create your views here.


class Login_View(View):
    template_name = 'login.html'

    def get(self, request):
        formulario = LoginUsuario()
        context = {'formulario': formulario}
        # return HttpResponse('prueba')
        return render(request, self.template_name, context)

    def post(self, request):
        formulario = LoginUsuario(request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data['usuario']
            password = formulario.cleaned_data['clave']
            print(usuario)
            print(password)
            user = authenticate(request, username=usuario, password=password)
            print(user)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/perfil/')
                   # return HttpResponse("FUNCIONO")
                else:
                    messages.error(request, 'USUARIO NO ACTIVO')
                    return redirect("/login_view/")
            else:
                messages.error(request, 'DATOS INCORRECTOS')
                return redirect("/login_view/")


def logout_view(request):

    print('logout')
    logout(request)
    return redirect('/')


def perfil(request):

    return redirect("/registro_tareas/")


def inicio(request):
    return render(request, 'inicio.html')


def registro_tareas(request):
    template = "registro_tarea.html"
    registro_tareas_form = RegistroTareasForm()
    context = {'formulario': registro_tareas_form}
    return render(request, template, context)


class RegistroTareas(View):
    template_name = "registro_tarea.html"

    def get(self, request):
        formulario = RegistroTareasForm()
        filtro = Filtro()

        context = {'formulario': formulario, 'lista': Tarea.objects.filter(user_id=request.user.id).order_by('-vencimiento'),
                   'filtro': filtro
                   }
        return render(request, self.template_name, context)

    def post(self, request):

        formulario = RegistroTareasForm(request.POST)
        if formulario.is_valid():
            usuario = User.objects.get(id=request.user.id)
            estado = Estado.objects.get(nombre=formulario['estado'].value())
            categoria = Categoria.objects.get(
                nombre=formulario['categoria'].value())
            vencimiento = formulario['vencimiento'].value()
            descripcion = formulario['descripcion'].value()
            nombre = formulario['nombre'].value()

            tarea = Tarea(user=usuario, estado=estado, categoria=categoria,
                          vencimiento=vencimiento, descripcion=descripcion, nombre=nombre)
            tarea.save()
            return HttpResponse(f" {formulario['nombre'].value()}  {formulario['vencimiento'].value()}    {formulario['categoria'].value()} ")


def funcion_filtro(request):
    template = "registro_tarea.html"
    filtro = Filtro(request.POST)
    if filtro.is_valid():
        nombre_estado = filtro['estado'].value()
        nombre_categoria = filtro['categoria'].value()

        if nombre_categoria == "TODAS" and nombre_estado == "TODAS":

            tareas = Tarea.objects.filter(user_id=request.user.id)

        elif nombre_estado == "TODAS":

            tareas = Tarea.objects.filter(
                categoria=Categoria.objects.get(nombre=nombre_categoria), user_id=request.user.id)

        elif nombre_categoria == "TODAS":
            tareas = Tarea.objects.filter(
                estado=Estado.objects.get(nombre=nombre_estado), user_id=request.user.id)

        else:
            estado = Estado.objects.get(nombre=nombre_estado)
            categoria = Categoria.objects.get(nombre=nombre_categoria)
            tareas = Tarea.objects.filter(
                estado=estado, categoria=categoria, user_id=request.user.id)

        print(tareas)
        registro_tareas_form = RegistroTareasForm()
        filtro = Filtro()
        context = {'lista': tareas,
                   'formulario': registro_tareas_form, 'filtro': filtro}

        return render(request, template, context)


def tarea(request, id_tarea):
    # request.session['id_tarea'] = id_tarea
    template = "temp_tarea.html"
    formulario = RegistroTareasForm()
    observaciones_form = ObservacionForm()
    observaciones = Observacion.objects.filter(tarea_id=id_tarea)
    context = {'tarea': Tarea.objects.get(
        id=id_tarea), 'formulario': formulario, 'ob_form': observaciones_form, 'observaciones': observaciones}
    return render(request, template, context)


def eliminar_tarea(request, id_tarea):
    tarea = Tarea.objects.get(id=id_tarea)
    tarea.delete()
    return redirect('/registro_tareas/')


def completar_tarea(request, id_tarea):
    tarea = Tarea.objects.get(id=id_tarea)
    estado = Estado.objects.get(id=2)
    tarea.estado = estado
    tarea.save()
    return redirect('/registro_tareas/')


def editar_tarea(request, id_tarea):
    if request.method == 'POST':

        tarea = Tarea.objects.get(id=id_tarea)
        formulario = RegistroTareasForm(request.POST)
        if formulario.is_valid():
            estado = Estado.objects.get(
                nombre=formulario.cleaned_data['estado'])
            categoria = Categoria.objects.get(
                nombre=formulario.cleaned_data['categoria'])

            tarea.nombre = formulario.cleaned_data['nombre']
            tarea.descripcion = formulario.cleaned_data['descripcion']
            tarea.vencimiento = formulario.cleaned_data['vencimiento']
            tarea.estado = estado
            tarea.categoria = categoria
            tarea.save()
            
            return redirect('/registro_tareas/')

    return HttpResponse(id_tarea)


def agregar_observacion(request):
    ob_form = ObservacionForm(request.POST)
    id_tarea = request.session['id_tarea']
    tarea = Tarea.objects.get(id=id_tarea)
    observacion = Observacion(
        observacion=ob_form['observacion'].value(), tarea=tarea)
    observacion.save()
    direccion = '/tarea/' + str(id_tarea)
    return redirect(direccion)


def editar_ob(request, id_ob, id_tarea):
    if request.method == 'POST':
        formulario = ObservacionForm(request.POST)
        if formulario.is_valid():
            ob = Observacion.objects.get(id=id_ob)
            nueva_ob = formulario.cleaned_data['observacion']
            print(nueva_ob)
            ob.observacion = nueva_ob
            ob.save()
            direccion = "/tarea/"+str(id_tarea)
            return redirect(direccion)


def borrar_ob(request, id_ob, id_tarea):

    ob = Observacion.objects.get(id=id_ob)
    ob.delete()
    direccion = "/tarea/"+str(id_tarea)
    return redirect(direccion)
