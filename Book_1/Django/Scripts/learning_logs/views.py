from django.shortcuts import render # функция render генерирует ответ на основании данных, полученных от представлений
from .models import Topic

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
