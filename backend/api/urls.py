# api/urls.py
from django.urls import path
from .views import process_speech, get_query_history,get_notes

urlpatterns = [
    path('process_speech/', process_speech, name='process_speech'),
    path('get_query_history/', get_query_history, name='get_query_history'),
    path('api/notes/', get_notes, name='get_notes'),
]
