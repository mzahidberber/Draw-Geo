from rest_framework import serializers
from geooperation_api.models import Radius

class RadiusSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    radius=serializers.FloatField()

    def create(self, validated_data):
        return Radius.objects.create(**validated_data)