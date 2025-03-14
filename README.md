### Установка и запуск проекта

Чтобы запустить проект как докер контейнер, необходимо:
    1. Установить docker
    2. Заполнить переменные окружения валидными значениями. (Для запуска докер контейнера- заполнять файл docker.env, для локального запуска- .env)
    3. Перейти в браузере по адресу http://localhost:8000/api

Если необходим локальный запуск проекта- без использования докер контейнеров, то следует:
    1. Установить зависимости проекта из файла requirements.txt
    2. Заполнить файл .env корректными данными
    3. Перейти в браузере по адресу http://localhost:8000/api


### Основные компоненты и архитектура проекта

1. Директория проекта (animals)
    *   Настройка проекта (подключение приложения, конфигурация работы БД)- settings.py
    *   Настройка маршрутизации для приложения (Добавление параметра пути /api)- urls.py

2. Директория приложения (dogs)
    *   Описание моделей для ORM- models.py
    *   Создание сериализаторов для парсинга данных между объектами ORM и форматами JSON- serializers.py
    *   Представления ViewSet для совмещения методов объекта в один класс- views.py
    *   Создание роутеров для реализации маршрутизации представлений- urls.py

3. Корневая директория проекта
    *   Головной файл Django проекта- manage.py
    *   Файл получения переменных окружения из .env файла- config.py
    *   Файл с зависимостями для проекта- requirements.txt
    *   Файлы для поднятия docker образов- dockerfile, docker-compose


### Примеры использования API

1. Маршруты для работы с объектами Dog
    *   GET /api/dogs/ – Получить список всех собак.
    *   POST /api/dogs/ – Создать новую собаку.
    *   GET /api/dogs/{id}/ – Получить информацию о конкретной собаке.
    *   PUT /api/dogs/{id}/ – Полное обновление информации о собаке.
    *   PATCH /api/dogs/{id}/ – Частичное обновление информации о собаке.
    *   DELETE /api/dogs/{id}/ – Удалить собаку.

2. Маршруты для работы с объектами Breed
    *   GET /api/breeds/ – Получить список всех пород.
    *   POST /api/breeds/ – Создать новую породу.
    *   GET /api/breeds/{id}/ – Получить информацию о конкретной породе.
    *   PUT /api/breeds/{id}/ – Полное обновление информации о породе.
    *   PATCH /api/breeds/{id}/ – Частичное обновление информации о породе.
    *   DELETE /api/breeds/{id}/ – Удалить породу.
