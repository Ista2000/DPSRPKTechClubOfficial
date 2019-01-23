# chat/consumers.py
from channels.generic.websocket import AsyncWebsocketConsumer
import json
from django.urls import reverse_lazy
from DPSRPKTechClub.settings import BASE_DIR
from asgiref.sync import sync_to_async


class PadConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope['user']

        self.pad_hash = self.scope['url_route']['kwargs']['pad_hash']
        self.pad_group_name = 'pad_%s' % self.pad_hash

        # Join room group
        await self.channel_layer.group_add(
            self.pad_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.pad_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        code = text_data_json['code']
        selection = text_data_json['selection']
        user = text_data_json['user']
        await sync_to_async(self.open_file)()
        await sync_to_async(self.write_file)(code)
        await sync_to_async(self.file_close)()

        # Send message to room group
        await self.channel_layer.group_send(
            self.pad_group_name,
            {
                'type': 'pad_code',
                'code': code,
                'selection': selection,
                'user': user
            }
        )

    # Receive message from room group
    async def pad_code(self, event):
        code = event['code']
        selection = event['selection']
        user = event['user']
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'code': code,
            'selection': selection,
            'user': user
        }))

    def write_file(self, code):
        self.f.write(code)

    def open_file(self):
        self.f = open(BASE_DIR + "\\pads\\padcontent\\" + self.pad_hash, "w+")

    def file_close(self):
        self.f.close()
