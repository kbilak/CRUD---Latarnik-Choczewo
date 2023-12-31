# import json

# from asgiref.sync import async_to_sync
# from channels.generic.websocket import WebsocketConsumer
# from django.conf import settings

# class ChatConsumer(WebsocketConsumer):
#     def connect(self):
#         self.room_name = 'chat'
#         self.room_group_name = 'chat'
#         async_to_sync(self.channel_layer.group_add)(
#             self.room_group_name, self.channel_name
#         )

#         self.accept()

#     def disconnect(self, close_code):
#         # Leave room group
#         async_to_sync(self.channel_layer.group_discard)(
#             self.room_group_name, self.channel_name
#         )

#     # Receive message from WebSocket
#     def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json["message"]

#         ## Send message to room group
#         async_to_sync(self.channel_layer.group_send)(
#             self.room_group_name, {"type": "chat.message", "message": message}
#         )
#         print(message, 'ddd')

#     # Receive message from room group
#     # def chat_message(self, event):
#     #     async_to_sync(self.channel_layer.group_send)(
#     #         'chat', {"type": "chat.message", "message": event}
#     #     )
#         # print(event, channel_name)
#         # self.channel_layer.group_send(
#         #     channel_name,
#         #     {
#         #         'type': 'chat.message',
#         #         'message': event,
#         #     }
#         # )

    
#     async def chat_message(self, event):
#         """
#         Called when someone has messaged our chat.
#         """
#         # Send a message down to the client
#         await self.send_json(
#             {
#                 "msg_type": 0,
#                 "room": 'chat',
#                 "message": 'loool',
#             },
#         )

# import json

# from asgiref.sync import async_to_sync
# from channels.generic.websocket import WebsocketConsumer


# class ChatConsumer(WebsocketConsumer):
#     def connect(self):
#         self.room_name = 'chat'
#         self.room_group_name = f"chat_{self.room_name}"

#         # Join room group
#         async_to_sync(self.channel_layer.group_add)(
#             self.room_group_name, self.channel_name
#         )

#         self.accept()

#     def disconnect(self, close_code):
#         # Leave room group
#         async_to_sync(self.channel_layer.group_discard)(
#             self.room_group_name, self.channel_name
#         )

#     # Receive message from WebSocket
#     def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json["message"]

#         # Send message to room group
#         async_to_sync(self.channel_layer.group_send)(
#             self.room_group_name, {"type": "chat.message", "message": message}
#         )

#     # Receive message from room group
#     def chat_message(self, event):
#         print(event)
#         message = event["message"]

#         # Send message to WebSocket
#         self.send(text_data=json.dumps({"message": message}))
#         print(message)

# import json
# from channels.generic.websocket import WebsocketConsumer

# class ChatConsumer(WebsocketConsumer):
#     async def connect(self):
#         # Accept the WebSocket connection
#         self.room_name = 'chat'
#         self.accept()

#     def disconnect(self, close_code):
#         # Clean up if needed upon disconnect
#         pass

#     def send_notification(self, event):
#         # Send notification to the WebSocket client
#         self.send(text_data=json.dumps(event))