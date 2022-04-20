import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync

class ChatConsumer(AsyncWebsocketConsumer):
    # Called on connection.
    async def connect(self):
        self.room_group_name = 'test'
        
        # Joins the room group.
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        # Accepts the WebSocket connection.
        await self.accept()

    async def disconnect(self, message):
        # When the socket disconnects.
        print('disconnected', message)

    # Receive message from WebSocket.
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Sends the Event to a group.
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )
    # Receive message from room group.
    async def chat_message(self, event):
        message = event['message']

        # Send message to Websocket.
        await self.send(text_data=json.dumps({
            'type': 'chat',
            'message': message
        }))