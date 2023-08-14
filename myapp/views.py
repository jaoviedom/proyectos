from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from .forms import CreateNewTask

def index( request ):
    title = "Django Project!!"
    return render(request, 'index.html', {
        'title': title
    })

def hello( request, username ):
    print(username)
    return HttpResponse('Hello %s' % username)

def about( request ):
    return HttpResponse('<h1>About us</h1>')

def operation( request, number ):
    result = (number + 100) * 2
    return HttpResponse('<h2>El resultado de (%s + 100) * 2 es %s </h2>' % (number, result))

# Listando todos los proyectos
def projects( request ):
    title = 'Projects'
    projects = list(Project.objects.values())
    return render(request, 'projects.html', {
        'title': title,
        'projects': projects
    })

# Listar una tarea
def tasks( request ):
    # task = Task.objects.get(id=id)
    # task = get_object_or_404(Task, id=id)
    # return HttpResponse("<h1>Task: %s</h1>" % task.title)
    tasks = Task.objects.all()
    return render( request, 'tasks.html', {
        'tasks': tasks
    })

def create_task( request ):
    if request.method == 'GET':    
        return render( request, 'create_task.html', {
            'form': CreateNewTask()
        })
    else: 
        title = request.POST['title']
        description = request.POST['description']
        project_id = 1
        Task.objects.create(title=title, description=description, project_id=project_id)
        return redirect('/tasks')