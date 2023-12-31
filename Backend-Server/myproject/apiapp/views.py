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
from .recipes import (
    RecipeStorerProcessor,
    RecipeStorerValidator,
    RecipeStorerStorer,
    RecipeRequesterFromDatabase,
)
from .save_recipes import RecipeManager
import re


class GetResponse:
    """class to get responses - scalzone"""

    def recipe_suggestion(self, prompt: str):
        """self function takes in a prompt and returns a response - scalzone"""
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
        recipes_to_receive=form_data["recipes_to_receive"],
    )


"""
def get_recipe(data: HttpRequest) -> HttpResponse:
    request = str(data.body, "UTF-8")

    request = json.loads(request)

    storer_manager = RecipeManager()
    requesterFromDatabase = RecipeRequesterFromDatabase(storer_manager)

    if (data is int) == False:
        return HttpResponse("Expected a number for which recipe to return")
    
    recipes = requesterFromDatabase.request(data)

    return HttpResponse(recipes)
"""


""" def get_recipe(request: HttpRequest) -> HttpResponse:
    try:
        data = json.loads(request.body.decode("UTF-8"))
        recipe_id = int(data.get("recipe_id", 0))
    except (json.JSONDecodeError, ValueError):
        return HttpResponse(
            "Invalid data format or recipe_id is not a valid integer", status=400
        )

    if not isinstance(recipe_id, int) or recipe_id < 0:
        return HttpResponse("Expected a non-negative integer for recipe_id", status=400)

    storer_manager = RecipeManager()
    requester_from_database = RecipeRequesterFromDatabase(storer_manager)

    recipes = requester_from_database.request(recipe_id)

    return HttpResponse(json.dumps(recipes), content_type="application/json")
 """


def get_recipe(request: HttpRequest) -> HttpResponse:
    try:
        data = json.loads(request.body.decode("UTF-8"))

        current_user = str(data.get("user"))

        if not isinstance(current_user, str):
            return HttpResponse("Need a username to get recipes", status=500)

        storer_manager = RecipeManager()
        requester_from_database = RecipeRequesterFromDatabase(storer_manager)

        recipes = requester_from_database.request_recipes_for_current_user(
            current_user)

        print(recipes)

        return HttpResponse(json.dumps(recipes), content_type="application/json")
    except (json.JSONDecodeError, ValueError):
        return HttpResponse("Invalid data format or current_user is not a string", status=500)


def save_recipes(data: HttpRequest) -> HttpResponse:
    request = str(data.body, "UTF-8")

    request = json.loads(request)

    validator = RecipeStorerValidator()
    storer_manager = RecipeManager()
    storer = RecipeStorerStorer(storer_manager)
    processor = RecipeStorerProcessor(validator, storer)

    message = processor.process(request)

    return HttpResponse(message)


def extract_ingredients(recipe):
    # Split the string into lines
    lines = recipe.split('\n')

    # Find the start of the ingredients list
    ingredients_start = None
    for i, line in enumerate(lines):
        if 'Ingredients:' in line:
            ingredients_start = i + 1
            break

    if ingredients_start is None:
        return "No ingredients list found."

    # Extract the ingredients
    ingredients = []
    for line in lines[ingredients_start:]:
        # Stop if we reach the end of the ingredients list
        if 'Instructions:' in line:
            break

        # Remove any leading or trailing whitespace
        line = line.strip()

        # Skip empty lines
        if not line:
            continue

        # Extract the ingredient (assuming it's prefixed with a dash and a space)
        match = re.match(r'- (.+)', line)
        if match:
            ingredients.append(match.group(1))

    return ingredients


def request_user_input_for_gpt(data: HttpRequest) -> HttpResponse:
    request = str(data.body, "UTF-8")

    request = json.loads(request)

    if len(request) != 1:
        return HttpResponse("JSON object must only have 1 key-value pair")

    # The key where the message lies when the request is made
    key_in_request = list(request.keys())[0]

    form_data_from_request = request[key_in_request]
    form_data_from_request = json.loads(form_data_from_request)

    query_key_in_form_data_from_request = list(
        form_data_from_request.keys())[0]
    user_query_to_gpt = form_data_from_request[query_key_in_form_data_from_request]

    num_requests_key_in_form_data_from_request = list(
        form_data_from_request.keys())[1]
    num_requests_requested = form_data_from_request[
        num_requests_key_in_form_data_from_request
    ]

    prompt_to_gpt = map_request.add_number_recipes_string_to_gpt_request(
        number_of_recipes=num_requests_requested, request=user_query_to_gpt
    )

    # list_of_possible_ingredients = files_opener.get_list_of_possible_ngredients(
    #     "./ingredients.csv"
    # )

    # mapped_ingredients_file = ingredients_file_mapper.return_mapped_ingredient_entries(
    #     ingredients=list_of_possible_ingredients
    # )

    recipe_string = GetResponse.recipe_suggestion(
        self=GetResponse, prompt=prompt_to_gpt
    )

    # shopping_list = shopping_list_generator.return_list_of_ingredients_to_get(
    #     mapped_ingredients_file, recipe_string
    # )
    recipe_text = extract_ingredients(recipe_string)
    shopping_list = recipe_text

    response = {"response_text": recipe_string,
                "ingredients": shopping_list}

    return HttpResponse(json.dumps(response))

    # https://www.stackhawk.com/blog/django-cors-guide/
    # https://stackoverflow.com/questions/38482059/enabling-cors-cross-origin-request-in-django
    # https://www.delftstack.com/howto/django/django-post-request/
    # https://www.geeksforgeeks.org/how-to-convert-bytes-to-string-in-python/
    # https://www.w3schools.com/python/python_json.asp
    # https://www.w3schools.com/python/ref_dictionary_keys.asp
