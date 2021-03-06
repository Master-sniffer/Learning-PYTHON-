#работаем со схемой url для learning logs
from django.urls import path # path - необходима для связывания URL с представлениями

from . import views # views - импортируется из каталога, в котором находится данный файл

app_name='learning_logs' # эта переменная поможет django отличать этот файл от других файлов с таким же названием
urlpatterns=[ # в этом модуле - эта переменная представляет собой список страниц, которые могут запрашиваться из приложения learning logs
    #домашняя страница
    path ('', views.index, name='index'), # схема URL представляет собой вызов функции path с 3 аргументами. Первый аргумент содержит строку, которая помогает django лучше маршрутизировать текущий запрос. Django получает запрашиваемый URL и пытается отобразить его на представление. Для этого Django ищет среди всех определенных схем ту, которая соответствует текущему запросу. Пустая строка в данном случае - базовый URL адрес
    # второй аргумент path определяет вызываемую функцию из views.py . Когда запрашиваемый URL адрес соответствует регулярному выражению (1-й аргумент в path), django вызывает index из views.py . 
    # Третий аргумент определяет имя index для ЭТОЙ схемы URL, чтобы на нее можно было ссылаться в других частях кода. Каждый раз, когда нам надо будет предоставить домашнюю страницу, мы будем прописывать index, вместо URL
    path('topics/', views.topics, name='topics'),
    path('topics/<int:topic_id>/', views.topic, name='topic'), # topic_id - что же это ? Получается, когда мы вызываем один из топиков, мы говорим django, что они (страницы с топиками) относятся к topics, а не к чему-то другому. Дальше мы пишем id темы. Если вы прогоните БД по темам, то вы увидите, что у тем разные ID. Так, при заходе в тему chess, вы будете видеть в адресной строке http://127.0.0.1:8000/topics/1 
    #Страница для добавления новой темы
    path('new_topic/', views.new_topic, name='new_topic'),
    path ('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    path ('edit_entry/<int:entry_id>/', views.edit_entry , name='edit_entry'),
    
]
