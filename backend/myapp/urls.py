from django.urls import path
from .views import index, perform_task

urlpatterns = [
    path('', index, name='index'),
    path('perform_task/', perform_task, name='perform_task'),
]
