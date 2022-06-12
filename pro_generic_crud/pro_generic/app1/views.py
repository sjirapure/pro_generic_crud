from django.shortcuts import render,redirect
from .models import Employee

from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView
from django.urls import reverse_lazy

# Create your views here.

class ShowEmp(ListView):
    model = Employee
    
    
class AddEmp(CreateView):
    model = Employee
    fields = '__all__'
    success_url = reverse_lazy('show_url')
    
class UpdateEmp(UpdateView):
    model = Employee
    fields = '__all__'
    success_url = reverse_lazy('show_url')
    
    
class DeleteEmp(DeleteView):
    model = Employee
    fields = '__all__'
    success_url = reverse_lazy('show_url')
    context_object_name = 'obj'
    
   
    
