from channels.generic.websocket import WebsocketConsumer
import json
from asgiref.sync import async_to_sync

class VitalsConsumer(WebsocketConsumer):
    def connect(self):
        async_to_sync(self.channel_layer.group_add)(
            'vitals',
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            'vitals',
            self.channel_name
        )
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['vitals']

        self.send(text_data=json.dumps({
            'vitals': message
        }))
    
    def vitals_alarm(self, vital_data):
        self.send(
            text_data = vital_data["text"]
        )