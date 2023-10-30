from django.urls import path
from . import views

urlpatterns = [
    path("items/", views.ItemListCreate.as_view(), name="item-list-create"),
    path("apiapp", views.Home.home()),
    path("log_request/", views.log_request, name="log_request"),
]
