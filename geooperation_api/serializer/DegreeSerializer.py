from rest_framework import serializers
from geooperation_api.models import Degree

class DegreeSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    degree=serializers.FloatField()

    def create(self, validated_data):
        return Degree.objects.create(**validated_data)