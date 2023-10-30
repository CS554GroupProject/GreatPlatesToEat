from django.urls import path
from .views import ItemListCreate

urlpatterns = [
    path("items/", views.ItemListCreate.as_view(), name="item-list-create"),
<<<< JAlsaiari-patch-3 
  path("log_request/", views.log_request, name='log_request'), 
  =======
  >>>>>>>> main
]