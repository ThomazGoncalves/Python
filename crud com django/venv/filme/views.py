from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from .models import Genero, Filme
from django.urls import reverse_lazy

# Create your views here.


###### CREATE ######

class Filme_new(CreateView):
    model = Filme
    fields = ['filme','quantidade','genero','preco']
    template_name = 'filme_new.html'
    success_url = reverse_lazy('filmelist')


###### READ ######

class Filme_list(ListView):
    model = Filme
    template_name = 'filme_list.html'


###### UPDATE ######

class Filme_edit(UpdateView):
    model = Filme
    fields = ['filme','quantidade','genero','preco']
    template_name = 'filme_edit.html'
    success_url = reverse_lazy('filmelist')

###### DELETE ######

class Filme_delete(DeleteView):
    model = Filme
    template_name = 'filme_delete.html'
    success_url = reverse_lazy('filmelist')



