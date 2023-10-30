from django.urls import path
from .views import hello, log_request

urlpatterns = [
    path("", hello),
    path("log_request/", log_request, name="log_request"),
]
