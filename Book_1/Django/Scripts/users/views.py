from django.shortcuts import render , redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    #регаем нового юзверя
    if request.method != 'POST':
        #вывод пустой формы реги
        form=UserCreationForm()
    else:
        #Обработка заполненной формы
        form=UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user=form.save() # идет сохранение данных юзера в БД
            #Выполнение входа и перенаправка на домашнюю страницу
            login (request, new_user)
            return redirect ('learning_logs:index')
        # вывод пустой или недействительной формы
    context={'form': form}
    return render (request, 'registration/register.html', context)