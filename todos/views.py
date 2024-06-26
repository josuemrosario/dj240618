from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import ToDo

# Create your views here.

def home(request):
    # return HttpResponse('<h1>view Home</h1>')
    return render(request, "todos\home.html")

# A funcao a seguir será trocada por uma Class Based View
''' 
def todoListar(request):  # function Based View (view baseada em funcoes)
    # tarefas = [{
    #     'id':'1',
    #     'Tarefa':'comprar fraldas'
    # }]
    tarefas = ToDo.objects.all()  # busca todos os dados do banco
    return render(request, "todos/todolistar.html",{'tarefas':tarefas})
'''

class todoListarView(ListView):
    model = ToDo #classe deve usar o modelo ToDo (.\todos\models.py)


class todoCriarView(CreateView):
    model = ToDo
    fields = ["titulo","dtFinalizacao"]  # Uma lista de campos que o usuario pode alterar
    success_url = reverse_lazy('todo_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_pagina'] = 'Criar Tarefa'
        return context

class todoAtualizarView(UpdateView):
    model = ToDo
    fields = ["titulo","dtFinalizacao"]  # Uma lista de campos que o usuario pode alterar
    success_url = reverse_lazy('todo_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_pagina'] = 'Atualizar Tarefa'
        return context
    
class todoDeletarView(DeleteView):
    model = ToDo

