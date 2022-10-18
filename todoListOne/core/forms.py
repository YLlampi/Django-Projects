from django.forms import ModelForm, TextInput, DateInput, DateTimeInput
from .models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'date']

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control form-control-lg border-0 add-todo-input bg-transparent',
                'placeholder': 'Add New...',
            }),
            'date': DateTimeInput(attrs={
                'type': 'date',
            })
        }


class UpdateForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'


