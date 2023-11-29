"""
This file contains the recipe manager class, which manages saving and retrieving
the recipes from the database.
"""
import json


class RecipeManager:
    """
    Recipe Manger class contains all of the functions related to saving and retrieving recipes
    from the recipe database. At this time, the database is just  a .json file called recipe_database.json.
    ~scalzone
    """

    def build_recipe(self, name, desc, ingredient_list, key, currentUser):
        """
        This function builds a recipe object to be saved
        """
        recipe = {
            "name": name,
            "description": desc,
            "ingredients": ingredient_list,
            "key": key,
            "username": currentUser,
        }
        recipe_to_save = json.dumps(recipe)
        return recipe_to_save

    def is_empty(self, to_check):
        """
        This function checks to see if the .json file is empty
        """
        try:
            with open(to_check, "r", encoding="utf-8") as file:
                data = json.load(file)
                return not bool(data)
        except (json.JSONDecodeError, FileNotFoundError):
            return True

    def save_recipe(self, recipe_to_save, database_address):
        """
        This function writes the recipe to the database.

        """
        if self.is_empty(database_address):
            with open(database_address, "w", encoding="utf-8") as myfile:
                # myfile.write(recipe_to_save)
                json.dump(recipe_to_save, myfile, indent=2)
                return True
        else:
            with open(database_address, "r+", encoding="utf-8") as myfile:
                existing_data = json.load(myfile)
                if not isinstance(existing_data, list):
                    existing_data = [existing_data]
                existing_data.append(recipe_to_save)
                myfile.seek(0)
                json.dump(existing_data, myfile, indent=2)
                return True

    def retrieve_recipe(self, database_address):
        """
        This function retrieves a recipe based on the username
        and the recipe name.
        """

        try:
            with open(database_address, "r", encoding="utf-8") as myfile:
                recipes = json.load(myfile)
                if isinstance(recipes, dict):
                    return recipes
                else:
                    recipe_dict = {recipes[i] for i in range(0, len(recipes))}
                    return recipe_dict
                    # return (list(recipe_dict)[recipe_to_return])

        except (json.JSONDecodeError, FileNotFoundError):
            print(f"Error reading JSON file at {database_address}")


# Manual Testing
"""
address_key = 'recipe_database.json'
test_recipe = '{"recipe 3": "Recipe test contents 1", "user": "DefaultUser"}'
database_address = address_key
    
test_recipe_manager = RecipeManager()
if test_recipe_manager.is_empty(database_address):
    print("True")
else:
    print("False")

#test_save = test_recipe_manager.save_recipe(test_recipe, database_address)
test_return = test_recipe_manager.retrieve_recipe(database_address)
print(test_return)
"""
