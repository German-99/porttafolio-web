from django.urls import path
from .views import blog, project_detail

app_name = "blog"

urlpatterns = [

path('' ,blog, name='blogs'),
path('<int:project_id>', project_detail, name = 'project_detail')
]