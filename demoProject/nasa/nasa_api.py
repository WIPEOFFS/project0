import os
import requests

from logger_setup import setup_logger

logger = setup_logger('nasa_api_logger')


def fetch_nasa_apod():
    logger.info("Начинается вызов API NASA.")
    api_key = os.getenv('NASA_API_KEY', 'DEMO_KEY')
    url = f'https://api.nasa.gov/planetary/apod?api_key={api_key}'

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        explanation = data.get('explanation')
        image_url = data.get('url')
        hd_image_url = data.get('hdurl')


        logger.info("Данные успешно получены из NASA.")
    except requests.exceptions.RequestException as e:
        logger.error(f"Ошибка при вызове NASA API: {e}")


if __name__ == '__main__':
    fetch_nasa_apod()
