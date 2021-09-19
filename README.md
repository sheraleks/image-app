# Image app
Веб сервис, который может:
- определить каких пикселей на картинке больше, белых или черных
- подсчитать число пикселей на картинке по заданному hex-коду цвета.

# Использованный стек
- python 3.9.4

# Структура проекта
```
├── image_app                  # API сервис, который получает изображения и возвращает результат
│   ├── config.py
│   ├── __init__.py            # настройка json-логирования
│   ├── web                    
│   │   ├── __init__.py
│   │   ├── middlewares.py
│   │   ├── schemas.py
│   │   ├── utils.py
│   │   ├── app.py
│   │   └── routes.py
│   └── pixels                 # логика по работе с изображениями
│       ├── __init__.py
│       ├── schemas.py
│       ├── custom_fields.py
│       └── views.py
├── demo_app                   # фронтэнд "лайт": отправляет запросы к основному сервису и выводит результат
│   ├── __init__.py
│   ├── demo
│   │   ├── __init__.py
│   │   └── views.py
│   ├── web
│   │   ├── __init__.py
│   │   ├── app.py
│   │   └── routes.py
│   └── templates
│       └── index.html
├── tests
│   ├── image_app
│   │   ├── custom_color_test.py
│   │   ├── black_white_test.py
│   │   └── __init__.py
│   ├── __init__.py
│   └── test_files
│       ├── white_image.png
│       ├── black_image.jpg
│       └── green_image.png
├── config                     # основной конфиг проекта
│   └── config.yml
├── .gitignore
├── README.md
├── main.py 
├── requirements.txt
└── Makefile
```

# Запуск сервиса
Для удобства работы с сервисом был сделан makefile со следующими командами:
```
venv            создание виртуального окружения
install         установка зависимостей
test            запуск тестов
run             запуск сервиса
```
Например, make venv

Предварительно необходимо задать в файле config/config.yml необходимые параметры порта и максимального размера файла.

Документация:
```
- http://0.0.0.0:{port}/api/docs         # Swagger UI с описанием API
- http://0.0.0.0:{port}/api/docs/json    # Swagger в формате json
```
API-сервис:
```
- http://0.0.0.0:{port}/api/black_white  # определяет преобладающий цвет (белый/черный)
- http://0.0.0.0:{port}/api/custom_color # считает число пикселей заданного цвета
```
Фронтэнд-лайт:
```
- http://0.0.0.0:{port}/demo/black_white 
- http://0.0.0.0:{port}/demo/custom_color
```