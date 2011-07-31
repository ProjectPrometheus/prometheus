from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    Id = models.PositiveIntegerField(primary_key = True)
    name = models.CharField(max_length = 250, unique = True)
    summary = models.TextField()
    createDate = models.DateTimeField('date created', auto_now = True)
    completeDate = models.DateTimeField('completion date', blank = True)
    private = models.BooleanField(default = True)
    controlType = ((u'M', u'Manager'),
                   (u'B', u'Board'),
                   (u'C', u'Cloud Source'))

class Milestone(models.Model):
    Id = models.PositiveIntegerField(primary_key = True)
    title = models.CharField(max_length = 250, unique = True)
    description = models.TextField()
    projectId = models.ForeignKey(Project)
    createDate = models.DateTimeField('date created', auto_now = True)
    due = models.DateField('due date', blank = True)
    completeDate = models.DateField('date completed', blank = True)
    
class ProjectMember(models.Model):
    projectId = models.ForeignKey(Project)
    userId = models.ForeignKey(User)
    unique_together = ("projectId", "userId")
    memberType = ((u'P', u'Project Manager'),
                  (u'S', u'Staff'),
                  (u'O', u'Open Contributor'),
                  (u'B', u'Board Member'),
                  (u'C', u'Cloud Sourcer'))
