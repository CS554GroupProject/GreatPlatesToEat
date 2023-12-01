from .save_recipes import RecipeManager
from .address_to_recipe_database import recipes_database_address


class RecipeStorerValidator:
    def validate(self, recipe_record: dict) -> bool:
        # validation logic here
        return True


class RecipeStorerStorer:
    def __init__(self, manager: RecipeManager):
        self.manager = manager

    def store(self, recipe_record: dict) -> bool:
        recipe_record_json = self.manager.build_recipe(recipe_record)
        self.manager.save_recipe(recipe_record_json, recipes_database_address)

        return True


class RecipeStorerProcessor:
    def __init__(self, validator: RecipeStorerValidator, storer: RecipeStorerStorer):
        self.validator = validator
        self.storer = storer

    def process(self, data: str) -> str:
        message: str = ""
        valid = self.validator.validate(data)
        stored = self.storer.store(data)

        if stored == True:
            message = "Recipe successfully stored"
        else:
            message = "Something went wrong"

        return message


class RecipeRequesterFromDatabase:
    def __init__(self, manager: RecipeManager):
        self.manager = manager

    def request_recipes_for_current_user(self, current_user: str):
        recipe_entries_to_return: dict = []

        for recipe in recipe:
            if recipe.keys() < 5:
                SystemError("A recipe entry must contain 5 properties")
            current_user_in_recipe_entry = recipe.keys()[4]
            if current_user_in_recipe_entry == current_user:
                recipe_entries_to_return.push(recipe)

        return recipe_entries_to_return

    def request_all_data(self):
        recipes = self.manager.retrieve_recipe(recipes_database_address)

        return recipe


# https://www.geeksforgeeks.org/constructors-in-python/
# https://stackoverflow.com/questions/31678827/what-is-a-pythonic-way-for-dependency-injection
# https://www.geeksforgeeks.org/python-classes-and-objects/?ref=lbp
