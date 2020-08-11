from django.contrib import admin # Эта строка обозначает, что файл models надо искать в том же каталоге, где и админ

from .models import Topic, Entry

admin.site.register(Topic) # Сообщает, что управление должно идти через административный сайт
admin.site.register(Entry)
