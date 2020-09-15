from django.urls import path
from .views import NfceList, NfceCreate

urlpatterns = [
    path('', NfceList.as_view(), name='list_nfce'),
    path('create', NfceCreate.as_view(), name='create_nfce'),
]