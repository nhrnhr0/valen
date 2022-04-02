from django.shortcuts import render

# Create your views here.
import json
import os

import requests
from django.http import JsonResponse
from django.views import View
from django.conf import settings


TELEGRAM_URL = "https://api.telegram.org/bot"


# https://api.telegram.org/bot<token>/setWebhook?url=<url>/webhooks/tutorial/
class TelegramBotView(View):
    def post(self, request, *args, **kwargs):
        t_data = json.loads(request.body)
        t_message = t_data["message"]
        t_chat = t_message["chat"]
        
        print(t_data)

        return JsonResponse({"ok": "POST request processed"})

    @staticmethod
    def send_message(message, chat_id):
        data = {
            "chat_id": chat_id,
            "text": message,
            "parse_mode": "Markdown",
        }
        response = requests.post(
            f"{TELEGRAM_URL}{settings.TELEGRAM_BOT_TOKEN}/sendMessage", data=data
        )