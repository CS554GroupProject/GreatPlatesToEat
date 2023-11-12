class map_request:
    def add_number_recipes_string_to_gpt_request(number_of_recipes: int, request: str) -> str:
        if request.find("recipe") == -1:
            if number_of_recipes == 1:
                return request + " Give me 1 recipe."
            return request + " Give me 2 recipes."
        
        if number_of_recipes == 1:
           return request.replace("a recipe", str(number_of_recipes) + " recipe")
        return request.replace("a recipe", str(number_of_recipes) + " recipes")