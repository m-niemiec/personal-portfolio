from django.urls import path
from . import views


urlpatterns = [
    path('my_notes/', views.my_notes, name='my_notes'),
]
