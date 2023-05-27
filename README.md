# Password Generator

Нативный генератор пароля для запуска на ПК. При генерации пароля возможно выбрать его длинну и составляющие:
маленькие буквы, большие буквы, цифры и спец. символы. После генерации, пароль можно скопировать или сохрнаить в файл, в корневую директорию проекта. 

### Настройка окружения:

* Установить интерпритатор python3.
* Установить менеджер зависимостей PIP3.

### Установка и использование:

1. Склонировать репозиторий на свой компьютер, выполнив команду: `git clone`.
2. Открыть проект и установить зависимости, выполнив команду: `pip3 install -r requirements.txt`.
3. Запустить программу командой: `python3 main.py`.

## Дополнительная информация:

В проекте настроен линтер, который запускается командой: `pylint --output-format=colorized --extension-pkg-whitelist=PySide6 -v src/`.

В проекте написаны юнит-тесты, запускаются командой `pytest -v`.

В проекте настроено логгирование, конфигурационный файл для логирования лежит в корневой директории **logging.conf.yml**.
