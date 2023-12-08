from django.urls import path
from .views import *


urlpatterns = [
    path('', HomeTaskManager.as_view(), name='home'),
    path('category/<int:category_id>/', get_category, name='category'),
    path('priority/<int:priority_id>/', get_priority, name='priority'),
    path('completed/<int:completed_id>/', completed, name='completed_task'),
    path('taskmanager/<int:task_id>/', view_task, name='view_task'),
    path('add_task/', add_task, name='add_task'),
    path('login/', user_login, name='login'),
    path('register/', register, name='register'),
    path('logout/', user_logout, name='logout'),
    path('search/', search, name='search'),
    path('update/<int:task_id>/', TaskUpdate.as_view(), name='update'),
    path('finish/<int:task_id>/', FinishTask.as_view(), name='finish'),
    path('taskmanager/favourite/<int:favourite_id>/', get_favourite, name='favourite'),

    # path('favourite/<int:task_id>/', get_favourite, name='favourite'),
    # path('favourites/list/', favourite_list, name='favourite_list'),
    path('taskmanager/delete/<int:task_id>/', TagDelete.as_view(), name='delete')
]
