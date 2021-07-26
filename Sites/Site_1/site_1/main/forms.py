from .models import Task
from django.forms import TextInput, ModelForm, widgets, Textarea

class TaskForm(ModelForm):
    class Meta: 
        model=Task
        fields=["title", 'text']
        widgets={"title":TextInput(attrs={'class': 'form-control', "placeholder" : "enter the name" }), "text":widgets.Textarea(attrs={'class': 'form-control', "placeholder" : "enter the text" })}