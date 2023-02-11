from rest_framework import serializers
from geooperation_api.models import Point

class PointSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    X=serializers.FloatField(allow_null=True)
    Y=serializers.FloatField(allow_null=True)
    Z=serializers.FloatField(allow_null=True)

    def create(self, validated_data):
        return Point.objects.create(**validated_data)