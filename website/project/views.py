# Views for a Prometheus Project

# Django Specific Imports
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response
from django.views.decorators.http import require_http_methods

# Project Specific Imports
from project.models import Project, ProjectMember
# from task.models import Task

# The landing page for all projects home page.
# Shows a list of the top project / random projects
def index(request):
    return render_to_response('project/index.html', {})

# The "Home Page" or "Dashboard" of an individual project
require_http_methods(["GET"])
def dash(request, project_id):
    project = get_object_or_404(Project, pk = project_id)
    return render_to_response('project/dash.html', {'proj': project})

require_http_methods(["GET"])
def edit(request, project_id):
    # IF this person has the authority to edit this project THEN

    # ELSE redirect to permission error page
    project = get_object_or_404(Project, pk = project_id)
    return render_to_response('project/edit.html', {'proj': project})
    
require_http_methods(["GET"])
def search(request, search):
    return HttpResponse()

require_http_methods(["GET"])
def milestones(request, project_id):
    p_miles = get_list_or_404(Milestone, projectId = project_id)
    return render_to_response('project/milstones.html', {'miles': p_miles})

# require_http_methods(["GET"])
# def tasks(request, project_id):
#    p_tasks = get_list_or_404(Task, projectId = project_id)
#    return render_to_response('project/tasks.html', {'tasks': p_tasks})

require_http_methods(["GET"])
def add(request):
    return render_to_response('project/add.html', {})
