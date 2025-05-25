import requests
from decouple import config


def send_telegram_file(file_path: str, token: str, chat_id: str) -> None:
    url = f"https://api.telegram.org/bot{token}/sendDocument"
    with open(file_path, 'rb') as file:
        response = requests.post(url, data={"chat_id": chat_id}, files={"document": file})


def send_telegram_message(message: str) -> None:
    token = config("TG_TOKEN", default="1234")
    chat_id = config("TG_CHAT_ID", default="1234")

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    params = {"chat_id": chat_id, "text": message}

    response = requests.post(url, data=params)
