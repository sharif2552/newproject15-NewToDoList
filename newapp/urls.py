
from django.urls import path 
from . import views


urlpatterns = [
    path('',views.all_task),
    path('add_task/',views.add_task),
    path('delete_task/',views.delete_task),
    path('delete_task/<int:task_id>',views.delete_task),
    path('strike',views.all_task),
    path('strike/<int:task_id>',views.strike),
]
