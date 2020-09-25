from django.urls import path
from .views import EstoqueList



urlpatterns = [
    path('', EstoqueList.as_view(), name='list_estform'),
]