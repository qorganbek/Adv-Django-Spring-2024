from django.shortcuts import render
from . import forms

student = ['Ali', 'Aidos', 'Nurkhat']


def index(request):
    return render(request, 'index.html', {'students': student})


def add(request):
    form = forms.Student(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            name = form.cleaned_data['name']
            student.append(name)
        else:
            raise Exception("Data is not valid!")

    return render(request, 'form.html', {'form': form})
