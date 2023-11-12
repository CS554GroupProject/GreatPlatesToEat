from .spreadsheet import files


def test_get_list_of_possible_ingredients(mocker):
    mock_file = mocker.mock_open()
    filename: str = "unique_indexed_ingredients.csv"
    mocker.patch("builtins.open", mock_file)
    mocker.patch("csv.reader")

    ingredients_list = files.get_list_of_possible_ngredients(filename=filename)
    mock_file.assert_called_once_with(filename, "r")

    assert ingredients_list == [""]


def test_get_list_of_possible_ingredients_list_with_1_element(mocker):
    mock_file = mocker.mock_open()
    filename: str = "unique_indexed_ingredients.csv"
    mocker.patch("builtins.open", mock_file)

    ingredients_list = fake_files.get_list_of_possible_ngredients_file_with_1_element(
        filename=filename
    )
    mock_file.assert_called_once_with(filename, "r")

    assert ingredients_list == ["", ""]


def test_get_list_of_possible_ingredients_list_with_2_elements(mocker):
    mock_file = mocker.mock_open()
    filename: str = "unique_indexed_ingredients.csv"
    mocker.patch("builtins.open", mock_file)

    ingredients_list = fake_files.get_list_of_possible_ngredients_file_with_2_elements(
        filename=filename
    )
    mock_file.assert_called_once_with(filename, "r")

    assert ingredients_list == ["", "", ""]


class fake_files:
    def get_list_of_possible_ngredients_file_with_1_element(filename: str) -> list[str]:
        list_of_ingredients: list[str] = [""]

        with open(filename, "r") as csv_file:
            dialect = "excel"
            delimiter: str = ","

            ingredients_reader = [[""]]

            for ingredient_row in ingredients_reader:
                if len(ingredient_row) != 0:
                    list_of_ingredients.append(ingredient_row[0])
        return list_of_ingredients

    def get_list_of_possible_ngredients_file_with_2_elements(
        filename: str,
    ) -> list[str]:
        list_of_ingredients: list[str] = [""]

        with open(filename, "r") as csv_file:
            dialect = "excel"
            delimiter: str = ","

            ingredients_reader = [[""], [""]]

            for ingredient_row in ingredients_reader:
                if len(ingredient_row) != 0:
                    list_of_ingredients.append(ingredient_row[0])
        return list_of_ingredients


# https://pytest-with-eric.com/pytest-advanced/pytest-mocking/#Mocking-In-Pytest
