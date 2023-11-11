from .save_recipes import RecipeManager

def test_build_recipe():
    #Arrange
    test_name = 'Recipe Name'
    test_desc = 'Description'
    test_list = 'Ingredients'
    test_key = 'Keyvalue'
    test_username = 'NickScalzone'
    
    #Act
    test_recipe_manager = RecipeManager()
    test_string = test_recipe_manager.build_recipe(test_name, test_desc, test_list, test_key, test_username)
    
    #Assert
    assert test_string == "{'name' : 'Recipe Name', 'description' : 'Description', 'ingredients' : 'Ingredients', 'key' : 'Keyvalue', 'username' : 'NickScalzone' }"
    
    
    
#    def build_recipe(self, name, desc, list, key, currentUser):
#       """
#       This function builds a recpie object to be saved
#       """ 
#       recipe = {
#           'name': name,
#           'description': desc,
#           'ingredients': list,
#           'key':key,
#           'username': currentUser
#       }
#       recipe_to_save = json.dumps(recipe)
#       return recipe_to_save