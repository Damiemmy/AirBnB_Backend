import json
from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import ConversationMessage

class ChatConsumer(AsyncWebsocketConsumer):
    pass