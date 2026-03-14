from rest_framework import serializers
from .models import Conversation,ConversationMessage
from useraccount.serializers import UserDetailSerializer


class ConversationListSerializer(serializers.ModelSerializer):
    user=UserDetailSerializer(many=True, read_only=True)
    class Meta:
        model= Conversation
        fields= ['id','users','modified_at',]

class ConversationMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model= Conversation
        fields= '__all__'

