from .recipes import recipe_storer_validator


def recipe_storer_validate_all_data_present():
    recipe_record_to_store = {
        Name: "A",
        Desc: "A",
        IngList: ["A"],
        Key: "A",
        "Created By": "A",
    }
    valid = recipe_storer_validator.validate(recipe_record_to_store)

    assert valid == True
