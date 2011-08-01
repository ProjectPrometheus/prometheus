# Views for a Prometheus Project
from django.contrib.auth.models import User
from project.models import Project, ProjectMember
from task.models import Task
from django.http import HttpResponse

# The landing page for all projects home page.
# Shows a list of the top project / random projects
def index(request):
    return HttpResponse()

# The "Home Page" or "Dashboard" of an individual project
def dash(request, proj_id):
    project = get_object_or_404(Project, pk = proj_id)
    return render_to_response('project/dash.html', {'proj': project})

def edit(request, proj_id):
    # IF this person has the authority to edit this project THEN

    # ELSE redirect to permission error page
    project = get_object_or_404(Project, pk = proj_id)
    return render_to_response('project/edit.html', {'proj': project})
    
def search(request, search):
    return HttpResponse()

def milestones(request, proj_id):
    p_miles = get_list_or_404(Milestone, projectId = proj_id)
    return render_to_response('project/milstones.html', {'miles': p_miles})

def tasks(request, proj_id):
    p_tasks = get_list_or_404(Task, projectId = proj_id)
    return render_to_response('project/tasks.html', {'tasks': p_tasks})
