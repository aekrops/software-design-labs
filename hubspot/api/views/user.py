from ..serializers.user import UserSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets, status
from ..models import User, Conversation


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('first_name')
    serializer_class = UserSerializer

    @action(detail=True, methods=["POST"])
    def assign_operator(self, request, pk):
        operator_id, conversation_id = request.data['operator_id'], request.data['conversation_id']
        if (conversation := Conversation.objects.get(conversation_id)) is not None:
            conversation.user = get_object_or_404(User, pk=operator_id)  # PROPERTY INJECTION
            conversation.save()
            return Response({'message': 'Operator reassigned'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Conversation not exists'}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request, *args, **kwargs):
        request_data = request.data.copy()
        request_serializer = self.get_serializer(data=request_data)
        request_serializer.is_valid(raise_exception=True)
        request_obj = request_serializer.save()
        user_id = int(request_data.pop('user')[0])
        request_obj.user = User.objects.get(id=user_id)
        request_obj.save()
        return Response(request_serializer.data, status=status.HTTP_201_CREATED)
