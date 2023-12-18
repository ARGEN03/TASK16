## Пример README для Django-приложения с использованием Django REST Framework

## Установка и Запуск

1. Убедитесь, что у вас установлен Django, создайте виртуальное окружение и активируйте его:

    ```bash
    python -m venv venv
    source venv/bin/activate  # Для Windows: venv\Scripts\activate
    ```

2. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

3. Создайте новый проект Django и приложение:

    ```bash
    django-admin startproject config
    cd config
    python manage.py startapp task
    ```

4. В файле `config/settings.py` добавьте приложение и Django REST Framework в `INSTALLED_APPS`:

    ```python
    INSTALLED_APPS = [
        # ...
        'rest_framework',
        'task',
    ]
    ```

5. Откройте файл `task/views.py` и определите функцию представления:

    ```python
    from django.shortcuts import render
    from rest_framework.decorators import api_view
    from rest_framework.response import Response
    from rest_framework import status
    from .models import *
    from .serializers import *

    @api_view(['GET'])
        def my_views(request):
            queryset = PersonalData.objects.all()
            serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data)
    ```

6. Откройте файл `task/urls.py` и определите URL-маршрут для вашей функции представления:

    ```python
    from django.contrib import admin
    from django.urls import path, include
    from myapp.views import my_view

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('my-url/', my_view, name='my-view'),
    ]
    ```

7. Запустите сервер разработки Django:

    ```bash
    python manage.py runserver
    ```

8. Перейдите по адресу [http://127.0.0.1:8000/my-url/](http://127.0.0.1:8000/my-url/) в браузере.

## Сериализаторы

9. Установите Django REST Framework:

    ```bash
    pip install djangorestframework
    ```

10. Откройте файл `task/serializers.py` и определите класс сериализатора:

    ```python
    from rest_framework import serializers
    from .models import *

    class TaskSerializer(serializers.ModelSerializer):
        class Meta:
            model= PersonalData
            fields = '__all__'
            # exclude = ['id', 'title']

        def validate(self, attrs):
            return super().validate(attrs)
    ```

11. В функции представления (`task/views.py`) используйте сериализатор:

    ```python
    from rest_framework.response import Response

   @api_view(['GET'])
    def my_views(request):
        queryset = PersonalData.objects.all()
        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data)
    ```

12. Определите модель PersonalData в файле (`task/models.py`):

    ```python
    Copy code
    from django.db import models

    class PersonalData(models.Model):
        name = models.CharField(max_length=76)
        last_name = models.CharField(max_length=100)
        phone = models.CharField(max_length=60)
        address = models.CharField(max_length=100)

        def __str__(self) -> str:
            return self.name
    ```

13. Создайте миграции и примените их:

    ```bash
    Copy code
    python manage.py makemigrations
    python manage.py migrate
    ```

14. Запустите сервер разработки Django снова:

    ```bash
    python manage.py runserver
    ```

14. Перейдите по адресу [http://127.0.0.1:8000/my-url/](http://127.0.0.1:8000/my-url/) и проверьте, что сериализатор корректно обрабатывает запрос и возвращает ожидаемый ответ.



