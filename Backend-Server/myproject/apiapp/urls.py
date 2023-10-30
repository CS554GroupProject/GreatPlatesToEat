from django.urls import path
# from .views import ItemListCreate
from .views import hello

urlpatterns = [
    # path("items/", views.ItemListCreate.as_view(), name="item-list-create"),
    path("", hello)
]
