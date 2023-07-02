from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from app1.forms import *
from app1.models import *
from django.contrib.auth import login, authenticate , logout
# Create your views here.


class Login_View(View):
    template_name = 'login.html'

    def get(self,request):
        formulario = LoginUsuario()
        context={'formulario': formulario}
        #return HttpResponse('prueba')
        return render(request,self.template_name,context)
    
    def post(self,request):
            formulario =  LoginUsuario(request.POST)           
            if formulario.is_valid():
                usuario= formulario.cleaned_data['usuario']
                password = formulario.cleaned_data['clave']
                print(usuario)
                print(password)
                user = authenticate(request, username=usuario, password=password)
                print(user)
                if user is not None:
                    if user.is_active:
                        login(request,user)
                        return redirect('/perfil/')
                       # return HttpResponse("FUNCIONO")
                    else:
                        return HttpResponse("NO FUNCIONO")
                else:   
                    return HttpResponse("NO FUNCIONO")


def logout_view(request):

    print('logout')
    logout(request)
    return redirect('/')

def perfil(request):

    return redirect("/registro_tareas/")

def inicio(request):
    return render(request,'inicio.html')

def registro_tareas(request):
    template="registro_tarea.html"
    registro_tareas_form = RegistroTareasForm()
    context={'formulario': registro_tareas_form }
    return render(request, template,context)


class RegistroTareas(View):
    template_name = "registro_tarea.html"

    def get(self, request):
        formulario = RegistroTareasForm()
        filtro = Filtro()
        
        context = {'formulario': formulario,'lista': Tarea.objects.all(),
                    'filtro': filtro
        }
        return render(request, self.template_name, context)

    def post(self, request):

        formulario = RegistroTareasForm(request.POST)
        if formulario.is_valid():
            usuario = User.objects.get(id = request.user.id)
            estado = Estado.objects.get(nombre=formulario['estado'].value())
            categoria = Categoria.objects.get(nombre=formulario['categoria'].value())
            vencimiento =  formulario['vencimiento'].value()
            descripcion = formulario['descripcion'].value()
            nombre = formulario['nombre'].value()

            
            tarea = Tarea(user = usuario , estado  = estado, categoria = categoria , vencimiento = vencimiento , descripcion = descripcion, nombre = nombre)
            tarea.save()
            return HttpResponse(f" {formulario['nombre'].value()}  {formulario['vencimiento'].value()}    {formulario['categoria'].value()} ")
                  
                  
def funcion_filtro(request):
    template = "registro_tarea.html"
    filtro = Filtro(request.POST)
    if filtro.is_valid():
        nombre_estado = filtro['estado'].value()
        nombre_categoria = filtro['categoria'].value()
       
        if nombre_categoria =="TODAS" and nombre_estado =="TODAS":
           
           tareas = Tarea.objects.all()
        
        elif nombre_estado == "TODAS":
            
            tareas = Tarea.objects.filter(categoria=Categoria.objects.get(nombre=nombre_categoria))
       
        elif nombre_categoria == "TODAS":
            tareas = Tarea.objects.filter(
                estado=Estado.objects.get(nombre=nombre_estado))

        else :
            estado = Estado.objects.get(nombre=nombre_estado)
            categoria = Categoria.objects.get(nombre=nombre_categoria)
            tareas = Tarea.objects.filter(estado=estado, categoria=categoria)
       
       
       
       
       
       


        print(tareas)
        registro_tareas_form = RegistroTareasForm()
        filtro = Filtro()
        context = {'lista': tareas, 'formulario': registro_tareas_form,'filtro':filtro}
       
        return render(request, template, context)
