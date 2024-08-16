import logging
import os
from datetime import datetime


def setup_logger(name, log_level=logging.INFO):
    # Определите форматтер
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Создайте директорию для логов, если ее нет
    log_dir = 'logs'
    os.makedirs(log_dir, exist_ok=True)

    # Определите имя файла для логов
    log_filename = os.path.join(log_dir, f"bot-{datetime.now().strftime('%Y-%m-%d')}.log")

    # Создайте обработчик для записи в файл
    file_handler = logging.FileHandler(log_filename)
    file_handler.setFormatter(formatter)

    # Создайте обработчик для вывода в консоль (если нужно)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # Настройте логгер
    logger = logging.getLogger(name)
    logger.setLevel(log_level)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
