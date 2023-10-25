from rest_framework import generics
from .models import Item, User, UserRequest
from .serializers import ItemSerializer
from .third_party_interfaces import ChatInteractions

class ItemListCreate(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class GetResponse:
    """class to get responses"""
    
    def recipe_suggestion(self, prompt:str):
        """This function takes in a prompt and returns a response"""
        user_request = ChatInteractions()
        response = None
        response = user_request.get_completion(prompt)
        return response
    
class Home:
    """Class to interact with the home page"""
    def home(request):
        return 0


def log_request(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            user_request = UserRequest.objects.create(
                user=request.user,  # Assuming the user is authenticated
                request=form.cleaned_data['request_text'],
            )
            return redirect('dashboard')
    else:
        form = RequestForm()

    return render(request, 'log_request.html', {'form': form})
