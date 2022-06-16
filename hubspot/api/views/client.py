from ..serializers.conversation import ConversationSerializer
from ..models import Client, Conversation, User
from ..serializers.client import ClientSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets, status
import random


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    @action(detail=True, methods=["POST"])
    def start_conversation(self, request, pk):
        operators = list(User.objects.all())
        operator = random.choice(operators)
        client = self.get_object()
        conversation = Conversation.objects.create(user=operator, client=client)
        serializer = ConversationSerializer(conversation, many=False)
        return Response({"message": "Conversation started", 'result': serializer.data}, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=["POST"])
    def change_phone_number(self, request, pk):
        phone_number = request.data['phone_number']
        client = self.get_object()
        if client.set_phone_number(phone_number):  # INTERFACE INJECTION
            client.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
