from django.http import HttpResponse,JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render , redirect

from .models import Project , Task
from .forms import CreateNewTask , CreateNewProject

def index(request):
    
    title = 'Welcome to Django Course!!'
    
    return render(request, 'index.html', {
        'title':title
    })
    # return HttpResponse("Index page")
    
def about(request):
    # return HttpResponse('About')
    username = 'nico'
    return render(request, 'about.html', {
        'username': username
    })

def hello(request, username):        
    return HttpResponse("<h2>Hello %s</h2>" %username)

def hola(request,id):
    print(type(id))
    return HttpResponse("<h2>Hola %s</h>2"%id)


#----------------------------------------------

def projects(request):    
    #projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request,'projects/projects.html', {
        'projects':projects
    })
    # return JsonResponse(projects, safe=False)

def tasks(request):
    #task = Task.objects.get(id = id)
    #task = get_object_or_404(Task, id=id)
    tasks = Task.objects.all()
    return render(request,'tasks/tasks.html', {
        'tasks' : tasks
    })
    # return JsonResponse('task: %s' % task.title, safe=False)
    
# def create_task(request):
#     if request.method == 'GET':
#         return render(request, 'create_task.html', {
#             'form': CreateNewTask()
#         })
#     else:
#         Task.objects.create(
#             title=request.POST['title'],
#             description=request.POST['description'], project_id=2)
#         return redirect('tasks')
def create_task(request):
    if request.method == 'GET':
        return render(request, 'tasks/create_task.html', {
            'form': CreateNewTask()
        })
    else:
        Task.objects.create(
             title=request.POST['title'], description=request.POST['description'], project_id=2)
        return redirect('tasks')
    
def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html' , {
            "form": CreateNewProject()
        })
    else:
        # project = Project.objects.create(name=request.POST["name"])
        Project.objects.create(name=request.POST["name"])        
        return redirect('projects')
        
def project_detail(request , id):    
    #project = Project.objects.get(id = id)
    project = get_object_or_404(Project, id=id)
    tasks = Task.objects.filter(project_id=id)
    return render(request, 'projects/detail.html', {
        'project': project,
        'tasks': tasks
    })