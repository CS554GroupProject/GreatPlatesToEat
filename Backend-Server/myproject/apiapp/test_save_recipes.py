"""
tests for RecipeManager class
"""

from .save_recipes import RecipeManager


def test_build_recipe():
    """test function for build recipe"""
    # Arrange
    test_name = "Recipe Name"
    test_desc = "Description"
    test_list = "Ingredients"
    test_key = "Keyvalue"
    test_username = "NickScalzone"

    # Act
    test_recipe_manager = RecipeManager()
    test_string = test_recipe_manager.build_recipe(
        test_name, test_desc, test_list, test_key, test_username
    )

    # Assert
    print(test_string)
    assert (
        test_string
        == '{"name": "Recipe Name", "description": "Description", "ingredients": "Ingredients", "key": "Keyvalue", "username": "NickScalzone"}'
    )
