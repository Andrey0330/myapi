from django.urls import path
from .views import WomenAPIView
urlpatterns = [
    path('v1/womenList', WomenAPIView.as_view())
]