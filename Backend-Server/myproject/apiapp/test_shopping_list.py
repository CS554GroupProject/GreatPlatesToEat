from .shopping_list import shopping_list_generator

def test_return_list_of_ingredients_to_get_list_has_no_ingredients():
    response: str = "needs eggs"

    ingredients: list = []

    ingredients_to_get = shopping_list_generator.return_list_of_ingredients_to_get(
        ingredients=ingredients, response=response
    )

    assert ingredients_to_get == []


def test_return_list_of_ingredients_list_to_get_has_1_ingredient_in_response():
    response: str = "needs eggs"

    ingredients: list = ["eggs"]

    ingredients_to_get = shopping_list_generator.return_list_of_ingredients_to_get(
        ingredients=ingredients, response=response
    )

    assert ingredients_to_get == ["eggs"]


def test_return_list_of_ingredients_to_get_list_has_1_ingredient_ingredient_not_in_response():
    response: str = "needs eggs"

    ingredients: list = ["blue cheese"]

    ingredients_to_get = shopping_list_generator.return_list_of_ingredients_to_get(
        ingredients=ingredients, response=response
    )

    assert ingredients_to_get == []


def test_return_list_of_ingredients_to_get_list_has_2_ingredients_ingredients_in_response():
    response: str = "needs organic eggs and blue cheese"

    ingredients: list = ["eggs", "blue cheese"]

    ingredients_to_get = shopping_list_generator.return_list_of_ingredients_to_get(
        ingredients=ingredients, response=response
    )

    assert ingredients_to_get == ["eggs", "blue cheese"]


def test_return_list_of_ingredients_to_get_list_has_2_ingredients_last_ingredient_in_list_not_in_response():
    response: str = "needs eggs"

    ingredients: list = ["eggs", "blue cheese"]

    ingredients_to_get = shopping_list_generator.return_list_of_ingredients_to_get(
        ingredients=ingredients, response=response
    )

    assert ingredients_to_get == ["eggs"]