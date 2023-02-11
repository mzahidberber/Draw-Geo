from rest_framework import serializers
from geooperation_api.models import Slope

class SlopeSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    slope=serializers.FloatField()

    def create(self, validated_data):
        return Slope.objects.create(**validated_data)