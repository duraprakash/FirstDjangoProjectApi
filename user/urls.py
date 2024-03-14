from django.urls import path
from .views import list_user, retrieve_user, update_user, delete_user
from .views import list_db_user, retrieve_db_user, update_db_user, delete_db_user

urlpatterns = [
    # # temp
    # path('', list_user),
    # path('<int:userId>/', retrieve_user),
    # path('<int:userId>/update/', update_user),
    # path('<int:userId>/delete/', delete_user),

    # db
    path('', list_db_user),
    path('<int:userId>/', retrieve_db_user),
    path('<int:userId>/update/', update_db_user),
    path('<int:userId>/delete/', delete_db_user),


]