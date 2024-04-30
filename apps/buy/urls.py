from django.urls import path
from apps.buy.views import update_card

urlpatterns = [
    path('update_card/', update_card, name='update_card'),
]
