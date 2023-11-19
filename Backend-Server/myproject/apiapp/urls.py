from django.urls import path
from .views import request_user_input_for_gpt, log_request, save_recipes

urlpatterns = [
    path("post_to_gpt/", request_user_input_for_gpt),
    path("log_request/", log_request, name="log_request"),
    path("save_recipe/", save_recipes),
]
