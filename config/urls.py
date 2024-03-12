"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from .views import yview as hello # 1. import the view and giving alter name
# from .views import hello_view, home_view
# from .views import list_todo, retrieve_todo, update_todo, delete_todo
# from .views import create_todo

# from .userviews import list_user, retrieve_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todos', include("todos.urls")),
    # path('myview/', hello), # 2. define the url path and fun
    # path('', home_view), 
    # path('helloview/', hello_view), 
    # path('todos/', list_todo), 
    # path('todos/<int:todoId>/', retrieve_todo), 
    # path('todos/<int:todoId>/update/', update_todo), 
    # path('todos/<int:todoId>/delete/', delete_todo), 
    # path('todos/create/', create_todo),
    # path('todos/create/', create_todo, name='create_todo'),

    # # users
    # path('users/', list_user),
    # path('users/<int:userId>/', retrieve_user),
    # path('users/<int:userId>/', retrieve_user),
]
