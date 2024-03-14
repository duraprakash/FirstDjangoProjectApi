
from django.urls import path
from .views import yview as hello # 1. import the view and giving alter name
from .views import hello_view #, home_view
from .views import list_todo, retrieve_todo, update_todo, delete_todo
from .views import create_todo


urlpatterns = [
    path('myview/', hello), # 2. define the url path and fun
    # path('home/', home_view), 
    path('helloview/', hello_view), 
    # CRUD of Todo
    path('', list_todo), 
    path('<int:todoId>/', retrieve_todo), 
    path('<int:todoId>/update/', update_todo), 
    path('<int:todoId>/delete/', delete_todo), 
    path('create/', create_todo),
    # path('create/', create_todo, name='create_todo'),
]
