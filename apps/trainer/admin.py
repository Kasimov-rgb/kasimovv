from django.contrib import admin
from apps.trainer.models import Trainer
from apps.trainer.forms import TrainerForm


@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    form = TrainerForm
    list_display = ['name', 'specialization', 'salary']
    list_filter = ['specialization']
    search_fields = ['name', 'specialization']
