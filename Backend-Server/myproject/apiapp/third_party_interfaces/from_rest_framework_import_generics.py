from rest_framework import generics
from rest_framework.response import Response
from .third_party_interfaces import ChatInteractions
from .models import UserRequest
from .serializers import RequestForm
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
import json
from django.contrib.auth.models import User


class GetResponse:
    """class to get responses - scalzone"""

    def recipe_suggestion(self, prompt: str):
        """This function takes in a prompt and returns a response - scalzone"""
        user_request = ChatInteractions()
        response = user_request.get_completion(prompt)
        return response


def log_request(request):
    if request.method == "POST":
        form = RequestForm(request.POST)
        if form.is_valid():
            create_user_request(request.user.username, form.cleaned_data)
            return redirect("dashboard")
    else:
        form = RequestForm()

    return render(request, "log_request.html", {"form": form})


def create_user_request(username, form_data):
    # Get the User instance using the provided username
    user_instance, created = User.objects.get_or_create(username=username)

    # Create a UserRequest tied to the User instance
    UserRequest.objects.create(
        user=user_instance,
        request=form_data["request_text"],
        recipes_to_receive=form_data["recipes_to_receive"],
    )


def is_proper_key(key: str) -> bool:
    if key != "Query":
        return False
    return True


def hello(data: HttpRequest) -> HttpResponse:
    user_text_key_value_pair = str(data.body, "UTF-8")

    user_text_key_value_pair = json.loads(user_text_key_value_pair)

    if len(user_text_key_value_pair) != 1:
        return HttpResponse("JSON object must only have 1 key-value pair")

    # The key where the message lies when the request is made
    key = list(user_text_key_value_pair.keys())[0]

    if is_proper_key(key=key) is False:
        return HttpResponse("Improper key name for key-value pair")

    user_text = user_text_key_value_pair[key]

    mapped_data = GetResponse.recipe_suggestion(self=GetResponse, prompt=user_text)
    return HttpResponse(mapped_data)
