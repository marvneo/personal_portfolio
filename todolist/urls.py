from django.contrib import admin
from django.urls import path
from todolist.views import todo_add, todoapp_index, todo_delete

urlpatterns = [
    path("", todoapp_index, name="todo_index"),
    path("addTodoItem/", todo_add, name="addTodoItem"),
    path("deleteTodoItem/<int:i>/",todo_delete, name="deleteTodoItem")

]