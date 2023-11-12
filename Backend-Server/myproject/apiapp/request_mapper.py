class map_request:
    def return_number_strings_to_gpt_based_on_request(
        number_of_recipes: int, request: str
    ) -> list[str]:
        requests_to_send_gpt: list[str] = [""]

        if number_of_recipes <= 0:
            return requests_to_send_gpt

        requests_to_send_gpt.append(request)
        requests_to_send_gpt.remove("")

        i = 2
        while i <= number_of_recipes:
            if request.find(" an ") == -1:
                requests_to_send_gpt.append(request.replace(" a ", " another "))
            elif request.find(" a ") == -1:
                requests_to_send_gpt.append(request.replace(" an ", " another "))

            i = i + 1

        return requests_to_send_gpt


# https://www.w3schools.com/python/python_conditions.asp
# https://www.geeksforgeeks.org/python-string-find/
