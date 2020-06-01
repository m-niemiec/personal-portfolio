from django.urls import path
from . import views


urlpatterns = [
    path('my_python/', views.my_python, name='my_python'),
    path('view_note/<int:note_id>', views.view_note, name='view_note'),
]
