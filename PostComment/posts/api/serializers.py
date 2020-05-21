from rest_framework import serializers

from posts.models import Collaborate_Messaging_A00




class FUMSerializer(serializers.ModelSerializer):

    class Meta:
        model = Collaborate_Messaging_A00

        fields = [
            'Collaborate_Messaging_A00_Rec',
            'messageType',
            'parentPostId',
            'message',
            'dateTimeStamp',
        ]


class MessageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collaborate_Messaging_A00

        fields = [
            'Collaborate_Messaging_A00_Rec',
            'messageType',
            'parentPostId',
            'message',
            'dateTimeStamp',
        ]



class MessageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collaborate_Messaging_A00

        fields = [
            'messageType',
            'parentPostId',
            'message',
            'dateTimeStamp',
        ]
