# Используем официальный образ Python 3.10
FROM python:3.12

# Устанавливаем рабочую директорию в контейнере
WORKDIR /autotrading

# Копируем файл requirements.txt в контейнер
COPY req.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r req.txt

# Копируем все файлы проекта в рабочую директорию контейнера
COPY . .

# Устанавливаем переменные окружения (если необходимо)
# ENV KEY=VALUE

# Команда для запуска вашего скрипта
CMD ["python", "my3_websocket_binance.py"]