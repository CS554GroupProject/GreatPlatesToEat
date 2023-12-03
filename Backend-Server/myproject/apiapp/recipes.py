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
        self.manager.save_recipe(recipe_record, recipes_database_address)

        return True


class RecipeStorerProcessor:
    def __init__(self, validator: RecipeStorerValidator, storer: RecipeStorerStorer):
        self.validator = validator
        self.storer = storer

    def process(self, data: dict) -> str:
        message: str = ""

        valid = self.validator.validate(data)
        stored = self.storer.store(data.get("Query"))

        if stored == True:
            message = "Recipe successfully stored"
        else:
            message = "Something went wrong"

        return message


class RecipeRequesterFromDatabase:
    def __init__(self, manager: RecipeManager):
        self.manager = manager

    def request_recipes_for_current_user(self, current_user: str):
        recipe_entries_to_return: list = [{}]

        recipes = self.request_all_data()

        for recipe in recipes:
            if len(recipe.keys()) < 4:
                SystemError("A recipe entry must contain 4 properties")
            user_in_recipe_entry = list(recipe.values())[0]
            if user_in_recipe_entry == current_user:
                recipe_entries_to_return.append(recipe)

        recipe_entries_to_return.remove({})
        return recipe_entries_to_return

    def request_all_data(self):
        recipes = self.manager.retrieve_recipe(recipes_database_address)

        if recipes is None:
            SystemError("Something went wrong")

        return recipes


# https://www.geeksforgeeks.org/constructors-in-python/
# https://stackoverflow.com/questions/31678827/what-is-a-pythonic-way-for-dependency-injection
# https://www.geeksforgeeks.org/python-classes-and-objects/?ref=lbp
