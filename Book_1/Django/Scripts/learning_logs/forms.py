from django import forms
from .models import Topic, Entry

class TopicForm(forms.ModelForm): # идет наследие от forms -> ModelForm
    class Meta: # этот класс сообщает на какой модели должна базироваться форма и какие поля на ней должны быть
        model=Topic # идет создание Topic
        fields=['text'] # тут будет текст
        labels={'text': ''} # эта строка приказывает джанго не генерировать подпись для текстового поля

class EntryForm(forms.ModelForm):
    class Meta:
        model=Entry
        fields=['text']
        labels={'text': "Entry"} # полю text назначается пустая запись
        widgets={'text': forms.Textarea(attrs={'cols': 80})} # это элемент формы html. Включая это поле, можно переопределить виджеты, которые Django выбрал изначально. Прописывая forms.Textarea , мы настраиваем виджет ввода для поля text, чтобы ширина текстовой области составляла 80 столбцов, вместо 40 (40 - значение по умолчанию) 