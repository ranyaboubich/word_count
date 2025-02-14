from django.urls import path
from .views import analyze_phrase

urlpatterns = [
    path('analyze/', analyze_phrase, name='analyze_phrase'),
]