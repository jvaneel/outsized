from outsized.core.serializers.stakeholders import  StakeholdersSerializer
from outsized.core.models.stakeholders import Project_Stakeholders
from rest_framework import viewsets, permissions


class StakeholderViewSet(viewsets.ModelViewSet):
    queryset = StakeholdersSerializer.objects.all()
    serializer_class = Project_Stakeholders
    permission_classes = (permissions.AllowAny,)
