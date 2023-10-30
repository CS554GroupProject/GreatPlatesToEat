
from django.urls import path
from .views import PlatesView


urlpatterns = [
    path("plates/", PlatesView.as_view(), name="great-plates-to-eat"),
]
