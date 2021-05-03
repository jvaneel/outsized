from rest_framework import serializers
from outsized.core.models.clients import Master_Clients


class ClientsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Master_Clients
        fields = "__all__"
