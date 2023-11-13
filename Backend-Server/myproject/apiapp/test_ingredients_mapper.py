from .ingredients_mapper import ingredients_file_mapper


def test_map_ingredient_entry_ingredient_entry_empty():
    ingredient_entry: str = ""

    mapped_ingredient_entry = ingredients_file_mapper.map_ingredient_entry(
        ingredient_entry=ingredient_entry
    )

    assert mapped_ingredient_entry == ""


def test_map_ingredient_entry_ingredient_entry_has_a_space():
    ingredient_entry: str = " "

    mapped_ingredient_entry = ingredients_file_mapper.map_ingredient_entry(
        ingredient_entry=ingredient_entry
    )

    assert mapped_ingredient_entry == ""


def test_map_ingredient_entry_1_word_in_ingredient_entry():
    ingredient_entry: str = "cheese"

    mapped_ingredient_entry = ingredients_file_mapper.map_ingredient_entry(
        ingredient_entry=ingredient_entry
    )

    assert mapped_ingredient_entry == "cheese"


def test_map_ingredient_entry_2_words_in_ingredient_entry():
    ingredient_entry: str = "cheese blue"

    mapped_ingredient_entry = ingredients_file_mapper.map_ingredient_entry(
        ingredient_entry=ingredient_entry
    )

    assert mapped_ingredient_entry == "blue cheese"


def test_map_ingredient_entry_3_words_in_ingredient_entry():
    ingredient_entry: str = "flour all purpose"

    mapped_ingredient_entry = ingredients_file_mapper.map_ingredient_entry(
        ingredient_entry=ingredient_entry
    )

    assert mapped_ingredient_entry == "all purpose flour"


def test_map_no_ingredient_entries():
    ingredients: list = []

    mapped_ingredients = ingredients_file_mapper.return_mapped_ingredient_entries(
        ingredients=ingredients
    )

    assert mapped_ingredients == []


def test_map_1_ingredient_entries():
    ingredients: list = ["cheese blue"]

    mapped_ingredients = ingredients_file_mapper.return_mapped_ingredient_entries(
        ingredients=ingredients
    )

    assert mapped_ingredients == ["blue cheese"]


def test_map_2_ingredient_entries():
    ingredients: list = ["eggs", "cheese blue"]

    mapped_ingredients = ingredients_file_mapper.return_mapped_ingredient_entries(
        ingredients=ingredients
    )

    assert mapped_ingredients == ["eggs", "blue cheese"]
    
# https://www.geeksforgeeks.org/getting-started-with-testing-in-python/
