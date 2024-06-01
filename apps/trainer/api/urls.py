from django.urls import path
from rest_framework.routers import DefaultRouter
from apps.trainer.api import views

router = DefaultRouter()
router.register('', views.TrainerViewSet, basename="trainers_api")

urlpatterns = [
    path('create/<int:pk>/', views.TrainerUpdateDeleteRetrieveAPIView.as_view(), name='trainers'),
]

urlpatterns += router.urls
