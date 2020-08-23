from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model): #Наследуем от самого Джанго, которая будет определять базовый функционал модели
    #Начинается тема, которую изучает юзверь
    text=models.CharField(max_length=200) # CharField - это блок данных, который содержит текст. Обычно такой атрибут юзается, чтобы хранить имя\заголовок и тд. Когда мы определяем этот атрибут, мы должны вписать в него, сколько место нам нужно будет для этого атрибута в БД ( Базе Данных). В нашем случае, мы будем хранить макс 200 символов
    date_added= models.DateTimeField(auto_now_add=True) # DateTimeField - это атрибут, который отвечает за время. auto_add_now приказывает django , чтобы он юзал текущее время и дату
    owner=models.ForeignKey(User, on_delete=models.CASCADE) # Это некий внешний ключ к модели User . Если юзер будет удален, то и все темы, связанные с ним будут удалены

    def __str__(self): # это метод, который будет возвращать строку , которая хранится в text 
        return self.text 


class Entry(models.Model):
    topic=models.ForeignKey(Topic, on_delete=models.CASCADE)  # on_delete - означает, что при удалении темы, все записи к этой теме должны быть удалены. ForeignKey связывает весь текст с определенной записью в базе данных
    text=models.TextField() # тут пользователь может писать сток инфы, сколько хочет
    date_added=models.DateTimeField(auto_now_add=True)

    class Meta: # доп инфа по управлению моделью 
        verbose_name_plural='entries' # при обращении более чем к одной записи, мы будем видеть entries , а не Entrys

    def __str__(self):
        return f"{self.text[:50]}..." # Инфы может быть слишком много, поэтому мы выводим только первые 50 символов