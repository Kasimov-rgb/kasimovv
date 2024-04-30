from django.shortcuts import render, redirect
from django.views import View
from apps.bmi.froms import PersonForm
from apps.bmi.models import Person


class BMIHelpView(View):
    def get(self, request):
        return render(request, 'bmi_calculator/bmi_help.html')


class CalculateBMIView(View):
    def get(self, request):
        form = PersonForm()
        return render(request, 'bmi_calculator/calculate_bmi.html', {'form': form})

    def post(self, request):
        form = PersonForm(request.POST)
        if form.is_valid():
            person = form.save()
            return redirect('bmi_result', person_id=person.id)
        return render(request, 'bmi_calculator/calculate_bmi.html', {'form': form})


class BMIResultView(View):
    def get(self, request, person_id):
        person = Person.objects.get(id=person_id)
        bmi = person.calculate_bmi()
        return render(request, 'bmi_calculator/bmi_result.html', {'person': person, 'bmi': bmi})
