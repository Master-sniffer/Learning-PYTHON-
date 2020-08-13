from django import forms
from .models import Topic

class TopicForm(forms.ModelForm): # идет наследие от forms -> ModelForm
    class Meta: # этот класс сообщает на какой модели должна базироваться форма и какие поля на ней должны быть
        model=Topic # идет создание Topic
        fields=['text'] # тут будет текст
        labels={'text': ''} # эта строка приказывает джанго не генерировать подпись для текстового поля