from rest_framework import serializers
from geooperation_api.serializer import PointSerializer
from geooperation_api.models import Point


class PointAndListSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    point=PointSerializer()
    points=PointSerializer(many=True)

    def create(self, validated_data):
        return Point.objects.create(**validated_data)