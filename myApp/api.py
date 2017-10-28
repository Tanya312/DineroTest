from tastypie.resources import ModelResource, ALL
from myApp.models import Projects

class ProjectResource(ModelResource):
	class Meta:
		queryset = Projects.objects.all()
		resource_name = 'project'
		filtering = {
			'project_name': ALL,
			'team_assigned': ALL,
			'start_date': ['exact', 'lt', 'lte', 'gte', 'gt'],
			'end_date': ['exact', 'lt', 'lte', 'gte', 'gt'],
		}