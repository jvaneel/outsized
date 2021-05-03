from rest_framework import serializers
from outsized.core.models.stakeholders import Project_Stakeholders


class StakeholdersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project_Stakeholders
        fields = "__all__"
