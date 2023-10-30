""" Views file contains the functions that interact with the views in the program"""

from rest_framework import generics
from rest_framework.response import Response
from .third_party_interfaces import ChatInteractions
from .models import *
from .serializers import *


class ItemListCreate(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class GetResponse:
    """class to get responses - scalzone"""

    def recipe_suggestion(self, prompt: str):
        """This function takes in a prompt and returns a response - scalzone"""
        user_request = ChatInteractions()
        response = None
        response = user_request.get_completion(prompt)
        return response


def log_request(request):
    if request.method == "POST":
        form = RequestForm(request.POST)
        if form.is_valid():
            user_request = UserRequest.objects.create(
                user=request.user,  # Assuming the user is authenticated
                request=form.cleaned_data['request_text'],
            )
            return redirect('dashboard')
    else:
        form = RequestForm()

    return render(request, "log_request.html", {"form": form})
