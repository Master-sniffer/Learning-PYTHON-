from django.shortcuts import render, redirect # функция render генерирует ответ на основании данных, полученных от представлений
from .models import Topic
from .forms import TopicForm

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