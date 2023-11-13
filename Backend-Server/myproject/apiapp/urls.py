from django.urls import path
from .views import request_user_input_for_gpt, log_request

urlpatterns = [
    path("", request_user_input_for_gpt),
    path("log_request/", log_request, name='log_request'),
]
