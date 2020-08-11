#работаем со схемой url для learning logs
from django.urls import path # path - необходима для связывания URL с представлениями

from . import views # views - импортируется из каталога, в котором находится данный файл

app_name='learning_logs' # эта переменная поможет django отличать этот файл от других файлов с таким же названием
urlpatterns=[ #
    #домашняя страница
    path ('', views.index, name='index'),
]