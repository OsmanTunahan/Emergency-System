from app.config import Config
import requests

class NotificationService:
    @staticmethod
    def send_telegram_message(message):
        url = f"https://api.telegram.org/bot{Config.TELEGRAM_BOT_TOKEN}/sendMessage"
        payload = {
            'chat_id': Config.TELEGRAM_CHAT_ID,
            'text': message,
            'parse_mode': 'HTML'
        }
        response = requests.post(url, data=payload)
        return response.json()

    @staticmethod
    def send_discord_message(message):
        payload = {
            'content': message
        }
        response = requests.post(Config.DISCORD_WEBHOOK_URL, json=payload)
        return response.json()