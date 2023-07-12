from rest_framework import serializers
from geooperation_api.serializer import PointSerializer,AngleSerializer,RadiansSerializer
from geooperation_api.models import PointRadiusAngle


class PointRadiusAngleSerialier(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    point=PointSerializer()
    radius=serializers.FloatField()
    angle=serializers.FloatField()

    def create(self, validated_data):
        return PointRadiusAngle.objects.create(**validated_data)