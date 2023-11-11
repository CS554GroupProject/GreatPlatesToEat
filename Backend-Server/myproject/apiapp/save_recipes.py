"""
This file contains the recipe manager class, which manages saving and retrieving
the recipes from the database.
"""
import json

class RecipeManager:
    """
    Recipe Manger class contains all of the functions related to saving and retrieving recipes
    from the recipe database. At this time, the database is just a .txt file called 
    recipe_database.txt. Or maybe to a .json file called recipe_database.json. I'm not good at 
    this.
    """
    def build_recipe(self, name, desc, list, key, currentUser):
       """
       This function builds a recipe object to be saved
       """ 
       recipe = {
           'name': name,
           'description': desc,
           'ingredients': list,
           'key':key,
           'username': currentUser
       }
       recipe_to_save = json.dumps(recipe)
       return recipe_to_save
        
    def save_recipe(self, recipe_to_save, database_name):
        """
        This function writes the recipe to the database.

        Args:
            name (_type_): _description_
            desc (_type_): _description_
            list (_type_): _description_
            key (_type_): _description_
            currentUser (_type_): _description_
            database_name (_type_): _description_
        """
        database_name = 'recipe_database.json'
        with open(database_name, 'w') as myfile:
            myfile.write(recipe_to_save)
                
    def retrieve_recipe(self, curretUser, name):
        """
        This function retrieves a recipe based on the username
        and the recipe name.

        Args:
            curretUser (_type_): _description_
            name (_type_): _description_
        """
        
        
        
        

#  const onSaveRecipeCard = (event, name, desc, list, key) => {
 #   console.log(
 #     `Name: ${name} Desc: ${desc} IngList: ${list} Key: ${key} Created by: ${currentUser}`
  #  );
   # // send some request to backend to save it
 # };        