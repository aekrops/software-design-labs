from ..serializers.conversation import ConversationSerializer, MessageSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets, status
from ..models import Conversation, Message


class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer

    @action(detail=True, methods=["POST"])
    def send_message(self, request, pk):
        text = request.data['text']
        conversation = self.get_object()
        message = Message.objects.create(conversation=conversation, text=text)
        serializer = MessageSerializer(message, many=False)
        return Response({'message': 'Message was sent', 'result': serializer.data}, status=status.HTTP_201_CREATED)


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
