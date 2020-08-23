from django.shortcuts import render, redirect # функция render генерирует ответ на основании данных, полученных от представлений
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import Http404

def index(request): #request нужен, чтобы сайт не запускался каждый раз впустую
    #Домашняя страница
    return render(request, 'learning_logs/index.html') # Путь к файлу, который отвечает за внешку. функция render использует два аргумента -> исходный объект запроса и шаблон
    # порядок, как все происходит : если URL запроса совпадает с только что определенной схемой, тогда django в файле views.py ищет функцию index() 

@login_required # проверяет, зареган ли юзверь
def topics(request):
    topics = Topic.objects.filter(owner=request.user).order_by('date_added') # request.owner - приказывает django достать только те объекты Topic , у которых атрибут owner соответствует текущему пользователю
    context= {'topics' : topics}
    return render (request, "learning_logs/topics.html" , context)

@login_required
def topic (request, topic_id):
    topic= Topic.objects.get(id=topic_id) # ЭТО ВСЕ МОЖНО ПРОПИСАТЬ В ОБОЛОЧКЕ DJANGO
    if topic.owner != request.user:
        raise Http404
    entries= topic.entry_set.order_by('-date_added') # ЭТО ВСЕ МОЖНО ПРОПИСАТЬ В ОБОЛОЧКЕ DJANGO
    context= {'topic' : topic, 'entries' : entries}
    return render (request, 'learning_logs/topic.html' , context)


@login_required
def new_topic(request):
    # Идет определение новой темы
    if request.method !='POST':
        # Данные не отправлялись , поэтому создается пустая форма
        form=TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic=form.save(commit=False) # Новая тема должна быть изменена перед сохранением в БД, поэтому мы пишем commit=False 
            new_topic.owner=request.user # Атрибуту owner присваевается текущий юзверь 
            new_topic.save() # Теперь тема содержит все данные, которые нам нужны , после чего мы берем и сохраняем ее в БД
            return redirect('learning_logs:topics')
    # вывод пустой или недействительной формы 
    context={'form' : form}
    return render (request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    topic=Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form=EntryForm()
    else:
        form=EntryForm(data=request.POST)
        if form.is_valid():
            new_entry= form.save(commit=False) # мы создали объект, но пока не сохранили его в Базе данных 
            new_entry.topic= topic
            new_entry.save() # сохранение в базе данных 
            return redirect ('learning_logs:topic', topic_id=topic_id)
    context={'topic':topic, 'form':form}
    return render (request, "learning_logs/new_entry.html", context)

@login_required
def edit_entry(request, entry_id):
    entry=Entry.objects.get(id=entry_id)
    topic=entry.topic
    if topic.owner != request.user:
        raise Http404
    if request.method != 'POST':
        form=EntryForm(instance=entry) # говорит джанго, чтобы он создал форму на основании информации, которая уже имеется
    else:
        form=EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect ('learning_logs:topic', topic_id=topic.id)
    context= {'entry': entry, 'topic': topic, 'form':form}
    return redirect (request, "learning_logs/edit_entry.html", context )