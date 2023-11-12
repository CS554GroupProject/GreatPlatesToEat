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
           'name': name,
           'description': desc,
           'ingredients': ingredient_list,
           'key':key,
           'username': currentUser
       }
       recipe_to_save = json.dumps(recipe)
       return recipe_to_save
        
    def save_recipe(self, recipe_to_save, database_address):
        """
        This function writes the recipe to the database.

        """
        with open(database_address, 'w', encoding="utf-8") as myfile:
            myfile.write(recipe_to_save)
            return True
                
    def retrieve_recipe(self, database_address):
        """
        This function retrieves a recipe based on the username
        and the recipe name.
        """
        
        with open(database_address, 'r', encoding="utf-8") as myfile:
            recipes = json.load(myfile)
            
            return recipes
                