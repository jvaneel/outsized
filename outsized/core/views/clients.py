from outsized.core.serializers.clients import ClientsSerializer
from outsized.core.models.clients import Master_Clients
from rest_framework import viewsets, permissions


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Master_Clients.objects.all()
    serializer_class = ClientsSerializer
    permission_classes = (permissions.AllowAny,)
