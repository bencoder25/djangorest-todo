from todos.views import CreateTodoAPIView
from django.urls import path

urlpatterns=[
    path('create', CreateTodoAPIView.as_view(), name="create-todo")
]