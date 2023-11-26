class shopping_list_generator:
    def return_list_of_ingredients_to_get(ingredients: list, response: str) -> list:
        ingredients_to_get: list = []

        for ingredient in ingredients:
            if response.find(ingredient) != -1:
                ingredients_to_get.append(ingredient)

        return ingredients_to_get
