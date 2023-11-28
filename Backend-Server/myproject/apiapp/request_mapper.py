class map_request:
    def add_number_recipes_string_to_gpt_request(
        number_of_recipes: int, request: str
    ) -> str:
        if request.find("recipe") == -1:
            if number_of_recipes == 1:
                return request + " Give me 1 recipe."
            else:
                return request + " Give me " + str(number_of_recipes) + " recipes."
        else:
            if number_of_recipes == 1:
                if request.find("a recipe") != -1:
                    request = request.replace("a recipe", "1 recipe")
                else:
                    request = request.replace("recipe", "1 recipe")
            else:
                if request.find("a recipe") != -1:
                    request = request.replace(
                        "a recipe", str(number_of_recipes) + " recipes"
                    )
                elif request.find("recipes") != -1:
                    request = request.replace(
                        "recipes", str(number_of_recipes) + " recipes"
                    )
                else:
                    request = request.replace(
                        "recipe", str(number_of_recipes) + " recipes"
                    )
        return request
