from .request_mapper import map_request


def test_negative2_recipes_request_string():
    number_of_recipes = -2
    fake_request: str = "Give me a recipe for apple pie."

    fake_request_result_expected: list = []

    fake_request_result_actual = (
        map_request.return_number_strings_to_gpt_based_on_request(
            number_of_recipes, fake_request
        )
    )

    assert type(fake_request_result_actual) == list
    assert len(fake_request_result_actual) == 0


def test_negative1_recipes_request_string():
    number_of_recipes = -1
    fake_request: str = "Give me a recipe for apple pie."

    fake_request_result_expected: list = []

    fake_request_result_actual = (
        map_request.return_number_strings_to_gpt_based_on_request(
            number_of_recipes, fake_request
        )
    )

    assert type(fake_request_result_actual) == list
    assert len(fake_request_result_actual) == 0


def test_0_recipes_request_string():
    number_of_recipes = 0
    fake_request: str = "Give me a recipe for apple pie."

    fake_request_result_expected: list = []

    fake_request_result_actual = (
        map_request.return_number_strings_to_gpt_based_on_request(
            number_of_recipes, fake_request
        )
    )

    assert type(fake_request_result_actual) == list
    assert len(fake_request_result_actual) == 0


def test_1_recipe_request_string():
    number_of_recipes = 1
    fake_request: str = "Give me a recipe for apple pie."

    fake_request_result_expected: list = ["Give me a recipe for apple pie."]

    fake_request_result_actual = (
        map_request.return_number_strings_to_gpt_based_on_request(
            number_of_recipes, fake_request
        )
    )

    assert type(fake_request_result_actual) == list
    assert len(fake_request_result_actual) == 1
    assert fake_request_result_actual[0] == fake_request_result_expected[0]


def test_2_recipes_request_strings():
    number_of_recipes = 2

    fake_request: str = "Make me an apple pie."

    fake_request_result_expected: list = [
        "Make me an apple pie.",
        "Make me another apple pie.",
    ]

    fake_request_result_actual = (
        map_request.return_number_strings_to_gpt_based_on_request(
            number_of_recipes, fake_request
        )
    )

    assert type(fake_request_result_actual) == list
    assert len(fake_request_result_actual) == 2
    assert fake_request_result_actual[0] == fake_request_result_expected[0]
    assert fake_request_result_actual[1] == fake_request_result_expected[1]


def test_3_recipes_request_strings():
    number_of_recipes = 3

    fake_request: str = "Make me an apple pie."

    fake_request_result_expected: list = [
        "Make me an apple pie.",
        "Make me another apple pie.",
        "Make me another apple pie.",
    ]

    fake_request_result_actual = (
        map_request.return_number_strings_to_gpt_based_on_request(
            number_of_recipes, fake_request
        )
    )

    assert type(fake_request_result_actual) == list
    assert len(fake_request_result_actual) == 3
    assert fake_request_result_actual[0] == fake_request_result_expected[0]
    assert fake_request_result_actual[1] == fake_request_result_expected[1]
    assert fake_request_result_actual[2] == fake_request_result_expected[2]
