from django.db import models

from geooperation_api.models import Point, Radius,Angle

class PointRadiusAngle(models.Model):
    point=Point()
    radius=Radius()
    angle=Angle()