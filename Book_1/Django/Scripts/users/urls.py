# определяем схемы URL для юзверей

from django.urls import path, include

app_name="users" # присвоили здесь users, чтобы django мог отличить эти URL адреса от других, которые принадлежат другим приложениям
urlpatterns=[
    # включить URL авторизации по умолчанию
    path ('', include('django.contrib.auth.urls')),
]