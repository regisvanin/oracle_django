from django.urls import path
from .views import NfceList, NfceCreate, NfceEdit, NfceDelete

urlpatterns = [
    path('', NfceList.as_view(), name='list_nfce'),
    path('create', NfceCreate.as_view(), name='create_nfce'),
    path('edit/<int:pk>/', NfceEdit.as_view(), name='update_nfce'),
    path('delete/<int:pk>/', NfceDelete.as_view(), name='delete_nfce'),
]