from django.urls import path
from .views import ItemListCreate

urlpatterns = [
    path("items/", views.ItemListCreate.as_view(), name="item-list-create"),
]
