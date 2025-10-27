# Практическая работа №4 - Собственные Dockerfile

## Цель работы
Создать собственные Dockerfile для различных программ на Python, Java, Dart и HTML-сайта, а затем собрать контейнеры и протестировать их работу.

## Структура проекта
В архиве содержатся следующие программы:
- **calc-py** - Калькулятор на Python
- **calc-java** - Калькулятор на Java
- **dart-calc** - Калькулятор на Dart
- **game-java** - Игра "Угадай число" на Java
- **rpsgame-py** - Игра "Камень-ножницы-бумага" на Python
- **site** - HTML-сайт с несколькими страницами

---

## 1. Python Calculator (calc-py)

### Описание программы
Простой калькулятор на Python с интерактивным меню для выполнения арифметических операций (сложение, вычитание, умножение, деление).

### Dockerfile
```dockerfile
FROM python:alpine

LABEL version="1.0.1"
LABEL description="Python Calculator"
WORKDIR /app

COPY calc.py .

CMD ["python", "calc.py"]
```

### Инструкции по сборке и запуску

#### Сборка образа
```bash
cd calc-py
docker build -t calc-python .
```

#### Запуск контейнера
```bash
docker run -it --name my-calc-python calc-python
```

---

## 2. Java Calculator (calc-java)

### Описание программы
Калькулятор на Java, выполняющий базовые арифметические операции с двумя числами.

### Dockerfile
```dockerfile
FROM openjdk:17-alpine

LABEL version="1.0.1"
LABEL description="Java Calculator"
WORKDIR /app

COPY calc.java .

RUN javac calc.java

CMD ["java", "calc"]
```

### Инструкции по сборке и запуску

#### Сборка образа
```bash
cd calc-java
docker build -t calc-java .
```

#### Запуск контейнера
```bash
docker run -it --name my-calc-java calc-java
```

---

## 3. Dart Calculator (dart-calc)

### Описание программы
Калькулятор на Dart для выполнения арифметических операций.

### Dockerfile
```dockerfile
FROM dart:stable

LABEL version="1.0.1"
LABEL description="Dart Calculator"
WORKDIR /app

COPY calc.dart .

CMD ["dart", "run", "calc.dart"]
```

### Инструкции по сборке и запуску

#### Сборка образа
```bash
cd dart-calc
docker build -t calc-dart .
```

#### Запуск контейнера
```bash
docker run -it --name my-calc-dart calc-dart
```

---

## 4. Java Guessing Game (game-java)

### Описание программы
Игра "Угадай число" на Java, где компьютер загадывает число от 1 до 100, а пользователь пытается его угадать.

### Dockerfile
```dockerfile
FROM openjdk:17-alpine

LABEL version="1.0.1"
LABEL description="Java Guessing Game"
WORKDIR /app

COPY game.java .

RUN javac game.java

CMD ["java", "game"]
```

### Инструкции по сборке и запуску

#### Сборка образа
```bash
cd game-java
docker build -t game-java .
```

#### Запуск контейнера
```bash
docker run -it --name my-game-java game-java
```

---

## 5. Rock Paper Scissors Game (rpsgame-py)

### Описание программы
Классическая игра "Камень-ножницы-бумага" на Python, где игрок играет против компьютера.

### Dockerfile
```dockerfile
FROM python:alpine

LABEL version="1.0.1"
LABEL description="Rock Paper Scissors Game"
WORKDIR /app

COPY RockPaperScissorsGame.py .

CMD ["python", "RockPaperScissorsGame.py"]
```

### Инструкции по сборке и запуску

#### Сборка образа
```bash
cd rpsgame-py
docker build -t rpsgame-python .
```

#### Запуск контейнера
```bash
docker run -it --name my-rpsgame rpsgame-python
```

---

## 6. HTML Website (site)

### Описание
Статический HTML-сайт с несколькими страницами (index, about, contact, frog). Используется nginx для раздачи контента.

### Dockerfile
```dockerfile
FROM nginx:alpine

LABEL version="1.0.1"
LABEL description="Static HTML Website"

COPY . /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
```

### Инструкции по сборке и запуску

#### Сборка образа
```bash
cd site
docker build -t my-website .
```

#### Запуск контейнера
```bash
docker run -d -p 8080:80 --name my-site my-website
```

**Доступ к сайту:** Откройте браузер и перейдите по адресу `http://localhost:8080`

---

## Дополнительная информация

### Параметры команд Docker

- `docker build -t <имя> .` - Сборка Docker-образа с именем из Dockerfile в текущей директории
  - `-t` (tag) - Позволяет присвоить имя образу

- `docker run <параметры> <образ>` - Запуск контейнера из образа
  - `-it` - Запуск в интерактивном режиме с терминалом
  - `-d` - Запуск в фоновом режиме (detached mode)
  - `-p 8080:80` - Проброс портов (внешний:внутренний)
  - `--name <имя>` - Присвоить имя контейнеру

### Проверка работы контейнеров

Для проверки списка контейнеров:
```bash
docker ps -a
```

Для проверки списка образов:
```bash
docker images
```

Для просмотра информации о контейнере:
```bash
docker inspect <имя-контейнера>
```

### Остановка и удаление контейнеров

```bash
docker stop <имя-контейнера>
docker rm <имя-контейнера>
```

