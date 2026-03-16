from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import Conversation
from .serializers import ConversationListSerializer,ConversationDetailSerializer
from rest_framework_simplejwt.tokens import AccessToken
from useraccount.models import User


@api_view(['GET'])
def conversation_list(request):
    user = request.user if request.user.is_authenticated else None

    try:
        token=request.META['HTTP_AUTHORIZATION'].split('Bearer ')[1]
        token=AccessToken(token)
        user_id=token.payload['user_id']
        user=User.objects.get(pk=user_id)
    except Exception as e:
        print("TOKEN ERROR:", e)   
        user=None
    
    print('user,', user)
    print("USER:", user)
    serializer=ConversationListSerializer(request.user.conversations.all(),many=True)
    return JsonResponse(serializer.data,safe=False)

@api_view(['GET'])
def conversations_detail(request,pk):
    conversation=request.user.conversations.get(pk=pk)
    conversation_serializer=ConversationDetailSerializer(conversation, many=False)
    return JsonResponse({
        'conversation': conversation_serializer
    },safe=False)
    