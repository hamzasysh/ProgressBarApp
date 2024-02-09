# progressbar/consumers.py

import json
from channels.generic.websocket import WebsocketConsumer

class ProgressConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def update_progress(self, event):
        print('inside update')
        progress = event['progress']
        self.send(text_data=json.dumps({'progress': progress}))
