from django.urls import path
from rest_framework.routers import DefaultRouter
from apps.schedules.api import views

router = DefaultRouter()
router.register('', views.ScheduleViewSet, basename="schedules_api")

urlpatterns = [
    path('create/<int:pk>/', views.ScheduleUpdateDeleteRetrieveAPIView.as_view(), name='schedules'),
]

urlpatterns += router.urls
