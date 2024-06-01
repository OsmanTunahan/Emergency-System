import requests

class NotificationService:
    @staticmethod
    def send_telegram_message(bot_token, chat_id, message):
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        payload = {
            'chat_id': chat_id,
            'text': message,
            'parse_mode': 'HTML'
        }
        response = requests.post(url, data=payload)
        return response.json()

    @staticmethod
    def send_discord_message(webhook_url, message):
        payload = {
            'content': message
        }
        response = requests.post(webhook_url, json=payload)
        return response.json()