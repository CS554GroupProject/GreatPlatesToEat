class ingredients_object:
    def map_ingredient_entry(ingredient_entry: str) -> str:
        if ingredient_entry.strip() == "":
            return ""

        ingredient_entry_as_list = ingredient_entry.split(" ")

        first_item = ingredient_entry_as_list.pop(0)

        ingredient_entry_as_list.append(first_item)

        mapped_ingredient_entry = ""

        i = 0

        while i < len(ingredient_entry_as_list):
            mapped_ingredient_entry = (
                mapped_ingredient_entry + " " + ingredient_entry_as_list[i]
            )
            i = i + 1

        return mapped_ingredient_entry.strip()

    def map_ingredient_entries(ingredients: list[str]) -> list:
        mapped_ingredients: list[str] = [""]

        if ingredients[0] == "":
            ingredients.remove("")

        for ingredient in ingredients:
            mapped_ingredient = ingredients_object.map_ingredient_entry(
                ingredient_entry=ingredient
            )

            mapped_ingredients.append(mapped_ingredient)

        mapped_ingredients.remove("")
        return mapped_ingredients

    def return_list_of_ingredients(ingredients: list[str], response: str) -> list:
        ingredients_to_get: list[str] = [""]

        if ingredients[0] == "":
            ingredients.remove("")

        for ingredient in ingredients:
            if response.find(ingredient) != -1:
                ingredients_to_get.append(ingredient)

        ingredients_to_get.remove("")

        return ingredients_to_get
