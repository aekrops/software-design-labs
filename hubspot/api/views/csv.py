from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets, status
from ..serializers import ClientSerializer
from ..models import Client
import csv


class UploadDataViaCSV(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = Client

    @action(detail=True, methods=["POST"])
    def upload_data(self, request, pk):
        file = request.data['clients_data']
        rows = [row.decode("utf-8") for row in file]
        clients = csv.reader(rows, delimiter=',')
        for client in clients:
            if client:
                print(client)
                request_data = format_data(client)
                print(request_data)
                create_records(dict(request_data))  # METHOD INJECTION
        return Response("Records uploaded", status=status.HTTP_201_CREATED)


def format_data(clients):
    return {
        "email": clients[1],
        "phone_number": clients[2]
    }


def create_records(request_data):
    client_serializer = ClientSerializer(data=request_data)
    client_serializer.is_valid(raise_exception=True)
    client_serializer.save()


