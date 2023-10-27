# Project Design Document

## Project Design

### Our project will have a frontend developed using React(Javascript/CSS/HTML), a backend developed using Django(Python), and will connect the two with the Django Rest API. 

### The user will begin by entering what type of food they are thinking they'd like to make. This input will travel from the user input window, through the Rest API to the back end, where it will be filtered through the prompt filtering functions to create a prompt that asks for a recipe in response. The prompt will be sent to the Chat GPT API, which will return a response. The response will be returned to the user, who will confirm if the recipe is what they'd like to cook. Upon confirmation, the recipe will be saved to the user's account.