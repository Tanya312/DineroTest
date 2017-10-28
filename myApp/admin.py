# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Projects

# Register your models here.



class ProjectAdmin(admin.ModelAdmin):
	search_fields = ['project_name']
	list_display = ('project_name', 'start_date', 'end_date')
	list_filter = ['project_name', 'start_date', 'end_date', 'team_assigned']
	
admin.site.register(Projects, ProjectAdmin)
