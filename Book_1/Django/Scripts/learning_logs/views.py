from django.shortcuts import render, redirect # функция render генерирует ответ на основании данных, полученных от представлений
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.urls import reverse

def index(request): #request нужен, чтобы сайт не запускался каждый раз впустую
    #Домашняя страница
    return render(request, 'learning_logs/index.html') # Путь к файлу, который отвечает за внешку. функция render использует два аргумента -> исходный объект запроса и шаблон
    # порядок, как все происходит : если URL запроса совпадает с только что определенной схемой, тогда django в файле views.py ищет функцию index() 

def topics(request):
    topics = Topic.objects.order_by('date_added')
    context= {'topics' : topics}
    return render (request, "learning_logs/topics.html" , context)

def topic (request, topic_id):
    topic= Topic.objects.get(id=topic_id) # ЭТО ВСЕ МОЖНО ПРОПИСАТЬ В ОБОЛОЧКЕ DJANGO
    entries= topic.entry_set.order_by('-date_added') # ЭТО ВСЕ МОЖНО ПРОПИСАТЬ В ОБОЛОЧКЕ DJANGO
    context= {'topic' : topic, 'entries' : entries}
    return render (request, 'learning_logs/topic.html' , context)

def new_topic(request):
    # Идет определение новой темы
    if request.method !='POST':
        # Данные не отправлялись , поэтому создается пустая форма
        form=TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')
    # вывод пустой или недействительной формы 
    context={'form' : form}
    return render (request, 'learning_logs/new_topic.html', context)

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

def edit_entry(request, entry_id):
    entry=Entry.objects.get(id=entry_id)
    topic=entry.topic
    if request.method != 'POST':
        form=EntryForm(instance=entry) # говорит джанго, чтобы он создал форму на основании информации, которая уже имеется
    else:
        form=EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect ('learning_logs:topic', topic_id=topic.id)
    context= {'entry': entry, 'topic': topic, 'form':form}
    return redirect (request, 'learning_logs/edit_entry.html', context )