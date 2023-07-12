from rest_framework import serializers
from geooperation_api.models import Angle

class AngleSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    angle=serializers.FloatField()

    def create(self, validated_data):
        return Angle.objects.create(**validated_data)