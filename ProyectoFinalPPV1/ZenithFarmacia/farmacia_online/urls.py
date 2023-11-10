# farmacia_online/urls.py
from django.urls import path
from .views import home, CustomLoginView

urlpatterns = [
    path('', home, name='home'),
    path('login/', CustomLoginView.as_view(), name='login'),
    # Otros patrones de URL...
]
