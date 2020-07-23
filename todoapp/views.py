from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import Todo
from .form import Todoform,Newtodoform

# Create your views here.
def index(request):
    form=Newtodoform()
    todo_list= Todo.objects.order_by('id')
    context={'todo_list':todo_list,'form':form}
    return render(request, 'todoapp/index.html', context)

@require_POST
def add(request):
    form = Newtodoform(request.POST)
    if form.is_valid():
        # new_todo = Todo(text=form.cleaned_data['text'])
        new_todo = form.save()
    
    return redirect('index')

def finished(request,todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.completed = True
    todo.save()

    return redirect('index')

def delcomp(request):
    todo = Todo.objects.filter(completed__exact=True)
    todo.delete()

    return redirect('index')

def delall(request):
    todo=Todo.objects.all()
    todo.delete()
    return redirect('index')