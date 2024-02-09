# yourapp/routing.py

from django.urls import path
from .consumers import ProgressConsumer

websocket_urlpatterns = [
    path('ws/progress/', ProgressConsumer.as_asgi()),
    # Add more WebSocket URL patterns as needed
]
