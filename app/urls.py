from django.urls import path
from .views import TaskList,RegisterPage,LoginPage,logoutPage,CreateTask,TaskUpdate,DeleteTask,TaskDetail

urlpatterns = [
    path('',TaskList.as_view(),name='list-view'),
    path('register/',RegisterPage.as_view(),name='register'),
    path('login/',LoginPage.as_view(),name='login'),
    path('logout/',logoutPage,name='logoutPage'),
    path('create-task/',CreateTask.as_view(),name='create-task'),
    path('update-task/<int:pk>',TaskUpdate.as_view(),name='update-task'),
    path('delete-task/<int:pk>',DeleteTask.as_view(),name='delete-task'),
    path('task-detail/<int:pk>',TaskDetail.as_view(),name='task-detail'),


]