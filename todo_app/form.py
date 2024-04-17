from django import forms
from .models import Tasks


class Task_list(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = "__all__"
        widgets = {
            "task": forms.TextInput(
                attrs={
                    "placeholder": "What do you need to do?",
                    "class": "task-input",
                    "label": '',
                },
            ),
        }
