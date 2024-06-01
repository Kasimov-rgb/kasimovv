from django.urls import path
from rest_framework.routers import DefaultRouter
from apps.reviews.api import views

router = DefaultRouter()
router.register('', views.ReviewViewSet, basename="reviews_api")

urlpatterns = [
    path('create/<int:pk>/', views.ReviewUpdateDeleteRetrieveAPIView.as_view(), name='reviews'),
]

urlpatterns += router.urls
