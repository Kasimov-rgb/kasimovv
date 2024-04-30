from django.urls import path
from apps.trainer.views import TrainerListView, TrainerAddView

urlpatterns = [
    path('', TrainerListView.as_view(), name='trainer_list'),
    path('add/', TrainerAddView.as_view(), name='add_trainer'),
]
