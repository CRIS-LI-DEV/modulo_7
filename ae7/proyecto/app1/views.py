from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from app1.forms import LoginUsuario
from app1.models import Tarea
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

    
    return render(request,'perfil.html')    

def inicio(request):
    return render(request,'inicio.html')