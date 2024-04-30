from django.shortcuts import render, redirect
from django.views import View
from apps.trainer.models import Trainer
from apps.trainer.froms import TrainerForm


class TrainerListView(View):
    def get(self, request):
        trainers = Trainer.objects.all()
        return render(request, 'trainer/trainer_list.html', {'trainers': trainers})


class TrainerAddView(View):
    def get(self, request):
        form = TrainerForm()
        return render(request, 'trainer/add_trainer.html', {'form': form})

    def post(self, request):
        form = TrainerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('trainer_list')
        return render(request, 'trainer/add_trainer.html', {'form': form})
