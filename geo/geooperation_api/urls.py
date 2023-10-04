from django.urls import path,re_path
from geooperation_api.views import Geo,FindTwoPointsLength,FindCenterAndRadius,FindToSlopeLine
from geooperation_api.views import FindDegreeLineSlope,FindDegreeLineTwoPoints,ConvertDegreeToSlope
from geooperation_api.views import ConvertRadianToDegree,ConvertDegreeToRadians
from geooperation_api.views import FindCenterPointToLine,FindDegreeToBetweenTwoLines
from geooperation_api.views import FindDotProductToTwoPoints,FindDifferenceTwoPoints
from geooperation_api.views import WherePointsOnLine,FindInsectionPointToTwoLines
from geooperation_api.views import FindPointLength,WherePointZone,FindPointOnCircle
from geooperation_api.views import FindNearetPoint,FindStartAndStopAngle,findStartAndStopAngleTwoPoint

urlpatterns=[
    path('',Geo.as_view()),
    path('findTwoPointsLength/',FindTwoPointsLength.as_view()),
    path('findCenterAndRadius/',FindCenterAndRadius.as_view()),
    path('findToSlopeLine/',FindToSlopeLine.as_view()),
    path('findDegreeLineSlope/',FindDegreeLineSlope.as_view()),
    path('findDegreeLineTwoPoints/',FindDegreeLineTwoPoints.as_view()),
    path('convertDegreeToSlope/',ConvertDegreeToSlope.as_view()),
    path('convertRadianToDegree/',ConvertRadianToDegree.as_view()),
    path('convertDegreeToRadians/',ConvertDegreeToRadians.as_view()),
    path('findCenterPointToLine/',FindCenterPointToLine.as_view()),
    path('findDegreeToBetweenTwoLines/',FindDegreeToBetweenTwoLines.as_view()),
    path('findDotProductToTwoPoints/',FindDotProductToTwoPoints.as_view()),
    path('findDifferenceTwoPoints/',FindDifferenceTwoPoints.as_view()),
    path('wherePointOnLine/',WherePointsOnLine.as_view()),
    path('findInsectionPointToTwoLines/',FindInsectionPointToTwoLines.as_view()),
    path('findPointLength/',FindPointLength.as_view()),
    path('wherePointZone/',WherePointZone.as_view()),
    path('findNearetPoint/',FindNearetPoint.as_view()),
    path('findStartAndStopAngle/',FindStartAndStopAngle.as_view()),
    path('findStartAndStopAngleTwoPoint/',findStartAndStopAngleTwoPoint.as_view()),
    path('findPointOnCircle/',FindPointOnCircle.as_view()),
]