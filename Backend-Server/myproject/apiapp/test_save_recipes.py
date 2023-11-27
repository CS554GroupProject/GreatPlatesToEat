"""
tests for RecipeManager class
"""

from .save_recipes import RecipeManager

# To configure tests, please add correct local address for database.
address_key = "/Users/nicholasscalzone/Documents/COMPUTER SCIENCE CLASSES/CS554/GreatPlatesToEat/test_recipe_database.json"


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


def test_save_recipe():
    """
    Test function to save a recipe
    """
    # Arrange
    test_recipe = '{"recipe2": "Recipe test contents", "user": "DefaultUser"}'
    database_address = address_key

    # Act
    test_recipe_manager = RecipeManager()
    test_save = test_recipe_manager.save_recipe(test_recipe, database_address)

    # Assert
    assert test_save is True


def test_retrieve_recipe():
    """
    Integration test to ensure data is written and can be returned from the database
    """
    # Arrange
    test_recipe = '{"recipe": "Recipe test contents", "user": "DefaultUser"}'
    database_address = address_key

    # Act
    test_recipe_manager = RecipeManager()
    test_recipe_manager.save_recipe(test_recipe, database_address)
    test_return = test_recipe_manager.retrieve_recipe(database_address)

    # Assert
    assert test_return["recipe"] == "Recipe test contents"
    assert test_return["user"] == "DefaultUser"
