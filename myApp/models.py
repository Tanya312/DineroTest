# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

PROJECT_TYPES = (
	('R&D', 'Research & Development'),
	('WA', 'Web Application'),
	('DeOP', 'Devops'),
	('AI', 'Artificial Intelligence'),
	('DM', 'Data Mining'),
)

class Projects(models.Model):
	project_name = models.CharField(max_length=200, unique=True)
	start_date = models.DateField(null=True, blank=True)
	end_date = models.DateField(null=True, blank=True)
	project_type = models.CharField(max_length=5, choices=PROJECT_TYPES, default="R&D")
	team_assigned = models.CharField(max_length=100, null=True, blank=True)
	completion_status = models.IntegerField(default=0)
	
	def __str__(self):
		return self.project_name