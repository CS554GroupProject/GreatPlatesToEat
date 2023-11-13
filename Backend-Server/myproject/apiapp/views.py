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


def is_proper_key(key: str) -> bool:
    if key != "Query":
        return False
    return True


def request_user_input_for_gpt(data: HttpRequest) -> HttpResponse:
    all_recipe_responses: list = []
    user_text_key_value_pairs = str(data.body, "UTF-8")

    user_text_key_value_pairs = json.loads(user_text_key_value_pairs)

    if len(user_text_key_value_pairs) != 1:
        return HttpResponse("JSON object must only have 1 key-value pair")

    # The key where the message lies when the request is made
    key = list(user_text_key_value_pairs.keys())[0]

    if is_proper_key(key=key) is False:
        return HttpResponse("Improper key name for key-value pair")

    user_text = user_text_key_value_pairs[key]

    input_prompts_to_gpt = map_request.add_number_recipes_string_to_gpt_request(
        number_of_recipes=1, request=user_text
    )

    list_of_possible_ingredients = files_opener.get_list_of_possible_ngredients(
            "./apiapp/ingredients.csv")
    
    mapped_ingredients_file = ingredients_file_mapper.return_mapped_ingredient_entries(ingredients=list_of_possible_ingredients)

    string_of_all_recipes = ""
    
    for prompt in input_prompts_to_gpt:
        recipe_string = GetResponse.recipe_suggestion(self=GetResponse, prompt=prompt)
        string_of_all_recipes = string_of_all_recipes + "\n" + recipe_string
        
        all_recipe_responses.append(recipe_string)

    shopping_list_for_all_recipes = shopping_list_generator.return_list_of_ingredients_to_get(mapped_ingredients_file, string_of_all_recipes)

    return HttpResponse(json.dumps(shopping_list_for_all_recipes))

    # https://www.stackhawk.com/blog/django-cors-guide/
    # https://stackoverflow.com/questions/38482059/enabling-cors-cross-origin-request-in-django
    # https://www.delftstack.com/howto/django/django-post-request/
    # https://www.geeksforgeeks.org/how-to-convert-bytes-to-string-in-python/
    # https://www.w3schools.com/python/python_json.asp