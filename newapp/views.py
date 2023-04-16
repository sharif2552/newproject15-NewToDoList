from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Task


# Create your views here.
def home(request):
    return render(request, 'index.html')

def add_task(request):
    if request.method== "POST":
        name = request.POST['name']
        newtask= Task(name=name)
        newtask.save()
        return redirect('/')
    elif request.method =='GET':
            return render(request,'index.html')
        
    else:
            return HttpResponse("Error!")
    

def all_task(request):
    task = Task.objects.all()
    context={
        'tasks': task
    }
    return render(request,'index.html',context)


def delete_task(request, task_id=0):
     if task_id:
          try:
               task_remove = Task.objects.get(id=task_id)
               task_remove.delete()
               return redirect("/")
          except:
               return HttpResponse("Enter valid one")
          
def strike(request, task_id=0):
    if task_id:
        task = Task.objects.get(id=task_id)
        task.completed = not task.completed
        task.save()
    return redirect('/')


     