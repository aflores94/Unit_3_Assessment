from django.urls import path, include
from .views import *

urlpatterns = [
    path('', WishList.as_view(), name='wish_list'),
    path('add/', WishCreateView.as_view(), name='wish_add'),
    path('delete/<int:pk>/', WishDeleteView.as_view(), name="wish_delete")
]