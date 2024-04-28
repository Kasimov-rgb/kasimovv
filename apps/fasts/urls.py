
from django.urls import path

from apps.fasts.views import index, create_fasts, detail_fasts, delete_fasts, update_fasts

urlpatterns = [
    path('', index, name="homepage"),
    path('create/', create_fasts, name="create_apps"),
    path('apps/<int:pk>', detail_fasts, name="detail_fasts"),
    path('delete/<int:pk>', delete_fasts, name="delete_fasts"),
    path('update/<int:pk>', update_fasts, name="update_fasts"),

]