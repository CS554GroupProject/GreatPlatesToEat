from .request_mapper import map_request

def test_add_1_recipe_string_to_gpt_request_insert_inside_with_a_before_recipe():
    number_of_recipes = 1

    fake_request: str = "Give me a recipe for apple pie."

    fake_request_result_expected: str = "Give me 1 recipe for apple pie."

    fake_request_result_actual = map_request.add_number_recipes_string_to_gpt_request(number_of_recipes, fake_request)

    assert fake_request_result_actual == fake_request_result_expected

def test_add_2_recipes_string_to_gpt_request_insert_inside_with_a_before_recipe():
    number_of_recipes = 2
    fake_request: str = "Give me a recipe for apple pie."

    fake_request_result_expected: str = "Give me 2 recipes for apple pie."

    fake_request_result_actual = map_request.add_number_recipes_string_to_gpt_request(number_of_recipes, fake_request)

    assert fake_request_result_actual == fake_request_result_expected

def test_add_1_recipe_string_to_gpt_request_insert_inside_no_a_before_recipe():
    number_of_recipes = 1

    fake_request: str = "Give me recipe for apple pie."

    fake_request_result_expected: str = "Give me 1 recipe for apple pie."

    fake_request_result_actual = map_request.add_number_recipes_string_to_gpt_request(number_of_recipes, fake_request)

    assert fake_request_result_actual == fake_request_result_expected

def test_add_2_recipes_string_to_gpt_request_insert_inside_no_a_before_recipe():
    number_of_recipes = 2
    fake_request: str = "Give me recipe for apple pie."

    fake_request_result_expected: str = "Give me 2 recipes for apple pie."

    fake_request_result_actual = map_request.add_number_recipes_string_to_gpt_request(number_of_recipes, fake_request)

    assert fake_request_result_actual == fake_request_result_expected


def test_add_1_recipe_string_to_gpt_request_append():
    number_of_recipes = 1

    fake_request: str = "Make me an apple pie."

    fake_request_result_expected: str = "Make me an apple pie. Give me 1 recipe."

    fake_request_result_actual = map_request.add_number_recipes_string_to_gpt_request(number_of_recipes, fake_request)

    assert fake_request_result_actual == fake_request_result_expected

def test_add_2_recipes_string_to_gpt_request_append():
    number_of_recipes = 2

    fake_request: str = "Make me an apple pie."

    fake_request_result_expected: str = "Make me an apple pie. Give me 2 recipes."

    fake_request_result_actual = map_request.add_number_recipes_string_to_gpt_request(number_of_recipes, fake_request)

    assert fake_request_result_actual == fake_request_result_expected
