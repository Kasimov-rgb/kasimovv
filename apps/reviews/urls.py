from django.urls import path

from apps.reviews.views import delete_reviews, update_reviews

urlpatterns = [
    path('delete_reviews/<int:pk>', delete_reviews, name='delete_reviews'),
    path('update_reviews/<int:pk>', update_reviews, name='update_reviews'),
]