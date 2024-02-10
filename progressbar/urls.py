from django.urls import path
from . import views

urlpatterns = [
     path('pagedisp/', views.show_page, name='showPage'),
    path('btnclick/', views.taskDispatcher, name='taskDispatcher'),
    path('check-progress/<str:task_id>/', views.check_progress, name='check-progress')
    
]