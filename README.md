# skymarket

Это сайт с объявлениями. Поддерживает поиск по названию товаров и авторизацию пользователей.

<img src="site.png" alt="site" style="height: 380px;" />


## Как установить

Зависимости указаны в файле `pyproject.toml`, для установки выполните:

```sh
python -m pip install poetry
poetry install
```

Для миграции базы данных выполните:

```sh
skymarket/manage.py migrate
skymarket/manage.py loadall
```


## Запуск

Перейдите в папку `market_postgres` и выполните:

```sh
docker-compose up --build -d  
```

Затем вернитесь в корневую папку и запустите backend командой:

```sh
skymarket/manage.py runserver
```


## Цель проекта

Код написан в образовательных целях.
