from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse
from .models import todo

# Create your views here.

def getTodos():
    return todo.objects.order_by("createdat")


def index(req):
    todos = getTodos()
    return render(req, 'todo/index.html', {'todos': todos})


def addTodo(req):
    newTask = req.POST["task"]
    if not newTask:
        return render(req, 'todo/index.html', {'todos': getTodos(),'err_msg':'Task cannot be empty'})
    
    newTodo = todo(task=newTask,status='pending',createdat=timezone.now())
    newTodo.save()
    return HttpResponseRedirect(reverse('todo:index'))
    

def editForm(req, id):
    try:
        todoItem = todo.objects.get(pk=id)
    except todo.DoesNotExist:
        return render(req, 'todo/index.html', {'todos': getTodos(),'err_msg':'Todo not found'})
    else:
        return render(req, 'todo/edit_todo.html', {'todo':todoItem, 'checkComplete':setSelected(todoItem.status)})



def editTodo(req, id):
    editedTask = req.POST['task']
    editedStatus = req.POST['status']
    if not editedTask and not editedStatus:
        return render(req, 'todo/index.html', {'todos': getTodos(),'err_msg':'An error occured'})
    
    try:
        todoItem = todo.objects.get(pk=id)
    except todo.DoesNotExist:
        return render(req, 'todo/index.html', {'todos': getTodos(),'err_msg':'An error occured'})
    else:
        todoItem.task = editedTask
        todoItem.status = editedStatus
        todoItem.save()
        return HttpResponseRedirect(reverse('todo:index'))



def confirmDelete(req, id):
    try:
        todoItem = todo.objects.get(pk=id)
    except todo.DoesNotExist:
        return render(req, 'todo/index.html', {'todos': getTodos(),'err_msg':'Todo not found'})
    else:
        return render(req, 'todo/index.html', {'todos': getTodos(),'todo':todoItem, 'action':'confirmdelete'})
        # return render(req, 'todo/alert.html', {'todo':todoItem})




def deleteTodo(req, id):
    try:
        todoItem = todo.objects.get(pk=id)
    except todo.DoesNotExist:
        return render(
            req,
            "todo/index.html",
            {
                "todos": getTodos(),
                "err_msg": "Cannot delete. Todo item not found",
            },
        )
    else:
        todoItem.delete()
        return HttpResponseRedirect(reverse('todo:index'))

    


def setSelected(status):
    if str(status).lower() == 'completed':
        return 'selected'
    else:
        return ''