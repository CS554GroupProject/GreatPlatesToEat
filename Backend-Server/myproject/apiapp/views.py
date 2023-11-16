""" Views file contains the functions that interact with the views in the program"""

from rest_framework import generics
from rest_framework.response import Response
from .third_party_interfaces import ChatInteractions
from .models import *
from .serializers import *
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
import json
from django.shortcuts import render, redirect
from .forms import RequestForm
from .models import UserRequest
from .request_mapper import map_request
from .spreadsheet import files_opener
from .ingredients_mapper import ingredients_file_mapper
from .shopping_list import shopping_list_generator

class GetResponse:
    """class to get responses - scalzone"""

    def recipe_suggestion(self, prompt: str):
        """This function takes in a prompt and returns a response - scalzone"""
        user_request = ChatInteractions()
        response = None
        response = user_request.get_completion(prompt)
        return response

def log_request(request):
    if request.method == "POST":
        form = RequestForm(request.POST)
        if form.is_valid():
            create_user_request(form.cleaned_data)
            return redirect("dashboard")
    else:
        form = RequestForm()

    return render(request, "log_request.html", {"form": form})

def create_user_request(form_data):
    UserRequest.objects.create(
        user_name=form_data["user_name"],
        request=form_data["request_text"],
        recipes_to_receive=form_data["recipes_to_receive"]
    )


def save_recipes(data: HttpRequest) -> HttpResponse:
    # save functionality here
    return HttpResponse(data)


def request_user_input_for_gpt(data: HttpRequest) -> HttpResponse:
    request = str(data.body, "UTF-8")

    request = json.loads(request)

    if len(request) != 1:
        return HttpResponse("JSON object must only have 1 key-value pair")
    
    # The key where the message lies when the request is made
    key_in_request = list(request.keys())[0]

    form_data_from_request = request[key_in_request]
    form_data_from_request = json.loads(form_data_from_request)

    query_key_in_form_data_from_request = list(form_data_from_request.keys())[0]
    user_query_to_gpt = form_data_from_request[query_key_in_form_data_from_request]

    num_requests_key_in_form_data_from_request = list(form_data_from_request.keys())[1]
    num_requests_requested = form_data_from_request[num_requests_key_in_form_data_from_request]

    prompt_to_gpt = map_request.add_number_recipes_string_to_gpt_request(
        number_of_recipes=num_requests_requested, request=user_query_to_gpt
    )

    list_of_possible_ingredients = files_opener.get_list_of_possible_ngredients(
            "./apiapp/ingredients.csv")
    
    mapped_ingredients_file = ingredients_file_mapper.return_mapped_ingredient_entries(ingredients=list_of_possible_ingredients)
    
    recipe_string = GetResponse.recipe_suggestion(self=GetResponse, prompt=prompt_to_gpt)

    shopping_list = shopping_list_generator.return_list_of_ingredients_to_get(mapped_ingredients_file, recipe_string)

    response = {
        "recipes_from_gpt": recipe_string,
        "shopping list": shopping_list
    }

    return HttpResponse(json.dumps(response))

    # https://www.stackhawk.com/blog/django-cors-guide/
    # https://stackoverflow.com/questions/38482059/enabling-cors-cross-origin-request-in-django
    # https://www.delftstack.com/howto/django/django-post-request/
    # https://www.geeksforgeeks.org/how-to-convert-bytes-to-string-in-python/
    # https://www.w3schools.com/python/python_json.asp
    # https://www.w3schools.com/python/ref_dictionary_keys.asp