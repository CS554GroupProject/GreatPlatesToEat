class ingredients_file_mapper:
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

    def return_mapped_ingredient_entries(ingredients: list) -> list:
        mapped_ingredients: list = []

        for ingredient in ingredients:
            mapped_ingredient = ingredients_file_mapper.map_ingredient_entry(
                ingredient_entry=ingredient
            )

            mapped_ingredients.append(mapped_ingredient)

        return mapped_ingredients
