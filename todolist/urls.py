from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('task',views.TaskView.as_view()),
    path('task/<int:pk>', views.TaskDetailView.as_view()),
    
    
]