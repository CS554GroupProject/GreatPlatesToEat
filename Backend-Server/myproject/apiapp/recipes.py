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
        self.manager.build_recipe(recipe_record)
        self.manager.save_recipe(recipe_record, recipes_database_address)

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

    def request(self, recipe_number: int):
        recipe = self.manager.retrieve_recipe(recipes_database_address, recipe_number)

        return recipe


# https://www.geeksforgeeks.org/constructors-in-python/
# https://stackoverflow.com/questions/31678827/what-is-a-pythonic-way-for-dependency-injection
# https://www.geeksforgeeks.org/python-classes-and-objects/?ref=lbp
