import csv


class files_opener:
    def get_list_of_possible_ngredients(filename: str) -> list:
        list_of_ingredients: list = []

        with open(filename, "r") as csv_file:
            dialect = "excel"
            delimiter: str = ","

            ingredients_reader = csv.reader(
                csv_file, delimiter=delimiter, dialect=dialect
            )

            for ingredient_row in ingredients_reader:
                ingredient_row[0]
                if len(ingredient_row) != 0:
                    list_of_ingredients.append(ingredient_row[0])
        return list_of_ingredients


# https://python-forum.io/thread-7889.html Used to see how to find csv file

# Licence for the spreadsheet, Other, Apache 2.0 open source license. https://www.kaggle.com/datasets/thedevastator/now-with-more-nutrients/data
