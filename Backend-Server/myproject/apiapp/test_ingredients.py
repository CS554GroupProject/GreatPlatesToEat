from .ingredients import ingredients_object


def test_map_ingredient_entry_ingredient_entry_empty():
    ingredient_entry: str = ""

    mapped_ingredient_entry = ingredients_object.map_ingredient_entry(
        ingredient_entry=ingredient_entry
    )

    assert mapped_ingredient_entry == ""


def test_map_ingredient_entry_ingredient_entry_has_a_space():
    ingredient_entry: str = " "

    mapped_ingredient_entry = ingredients_object.map_ingredient_entry(
        ingredient_entry=ingredient_entry
    )

    assert mapped_ingredient_entry == ""


def test_map_ingredient_entry_1_word_in_ingredient_entry():
    ingredient_entry: str = "cheese"

    mapped_ingredient_entry = ingredients_object.map_ingredient_entry(
        ingredient_entry=ingredient_entry
    )

    assert mapped_ingredient_entry == "cheese"


def test_map_ingredient_entry_2_words_in_ingredient_entry():
    ingredient_entry: str = "cheese blue"

    mapped_ingredient_entry = ingredients_object.map_ingredient_entry(
        ingredient_entry=ingredient_entry
    )

    assert mapped_ingredient_entry == "blue cheese"


def test_map_ingredient_entry_3_words_in_ingredient_entry():
    ingredient_entry: str = "flour all purpose"

    mapped_ingredient_entry = ingredients_object.map_ingredient_entry(
        ingredient_entry=ingredient_entry
    )

    assert mapped_ingredient_entry == "all purpose flour"


def test_map_no_ingredient_entries():
    ingredients: list[str] = [""]

    mapped_ingredients = ingredients_object.map_ingredient_entries(
        ingredients=ingredients
    )

    assert mapped_ingredients == []


def test_map_1_ingredient_entries():
    ingredients: list[str] = ["cheese blue"]

    mapped_ingredients = ingredients_object.map_ingredient_entries(
        ingredients=ingredients
    )

    assert mapped_ingredients == ["blue cheese"]


def test_map_2_ingredient_entries():
    ingredients: list[str] = ["eggs", "cheese blue"]

    mapped_ingredients = ingredients_object.map_ingredient_entries(
        ingredients=ingredients
    )

    assert mapped_ingredients == ["eggs", "blue cheese"]


def test_return_list_of_ingredients_list_has_no_ingredients():
    response: str = "needs eggs"

    ingredients: list[str] = [""]

    ingredients_to_get = ingredients_object.return_list_of_ingredients(
        ingredients=ingredients, response=response
    )

    assert ingredients_to_get == []


def test_return_list_of_ingredients_list_has_1_ingredient_in_response():
    response: str = "needs eggs"

    ingredients: list[str] = ["eggs"]

    ingredients_to_get = ingredients_object.return_list_of_ingredients(
        ingredients=ingredients, response=response
    )

    assert ingredients_to_get == ["eggs"]


def test_return_list_of_ingredients_list_has_1_ingredient_ingredient_not_in_response():
    response: str = "needs eggs"

    ingredients: list[str] = ["blue cheese"]

    ingredients_to_get = ingredients_object.return_list_of_ingredients(
        ingredients=ingredients, response=response
    )

    assert ingredients_to_get == []


def test_return_list_of_ingredients_list_has_2_ingredients_ingredients_in_response():
    response: str = "needs organic eggs and blue cheese"

    ingredients: list[str] = ["eggs", "blue cheese"]

    ingredients_to_get = ingredients_object.return_list_of_ingredients(
        ingredients=ingredients, response=response
    )

    assert ingredients_to_get == ["eggs", "blue cheese"]


def test_return_list_of_ingredients_list_has_2_ingredients_last_ingredient_in_list_not_in_response():
    response: str = "needs eggs"

    ingredients: list[str] = ["eggs", "blue cheese"]

    ingredients_to_get = ingredients_object.return_list_of_ingredients(
        ingredients=ingredients, response=response
    )

    assert ingredients_to_get == ["eggs"]


# https://www.geeksforgeeks.org/getting-started-with-testing-in-python/
