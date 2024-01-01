from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.addTodo, name='add'),
    path('edit/<int:id>', views.editTodo, name='edit'),
    path('editform/<int:id>', views.editForm, name='editform'),
    path('confirmdelete/<int:id>', views.confirmDelete, name='confirmdelete'),
    path('delete/<int:id>', views.deleteTodo, name='delete'),
]