from django.shortcuts import render, redirect


# importamos la clase View
from django.views import View
from .models import *
from .forms import *
from django.views.generic import DeleteView
from django.urls import reverse_lazy




# Create your views here.
class AlumnoView(View):
    
    def get(self,request):
        listaAlumnos = TblAlumno.objects.all()
        formAlumno = AlumnoForm()
        context = {
            'alumnos' : listaAlumnos,
            'formAlumno': formAlumno
        }
        return render(request,'index.html',context)

    def post(self, request, pk = None):
        
    
        formAlumno = AlumnoForm(request.POST)
        if formAlumno.is_valid():
            formAlumno.save()
            return redirect('/')
        
class EliminarAlumnoView(View):
    def post(self, request, pk):
        # Eliminar el objeto correspondiente al ID proporcionado
        TblAlumno.objects.filter(pk=pk).delete()
        return redirect('/') 
    
class PorfesorView(View):
    
    def get(self,request):
        listaProfesores = TblProfesor.objects.all()
        formProfesor = ProfesorForm()
        context = {
            'profesores' : listaProfesores,
            'formProfesor': formProfesor
        }
        return render(request,'profesores.html',context)

    def post(self, request, pk = None):
        
    
        formProfesor = ProfesorForm(request.POST)
        if formProfesor.is_valid():
            formProfesor.save()
            return redirect('web:profesor')
        
class EliminarProfesorView(View):
    def post(self, request, pk):
        # Eliminar el objeto correspondiente al ID proporcionado
        TblProfesor.objects.filter(pk=pk).delete()
        return redirect('web:profesor') 

