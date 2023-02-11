from rest_framework import serializers
from geooperation_api.models import Radians

class RadiansSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    radians=serializers.FloatField()

    def create(self, validated_data):
        return Radians.objects.create(**validated_data)