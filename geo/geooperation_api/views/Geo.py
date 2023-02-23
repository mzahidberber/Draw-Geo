from .BaseView import BaseView
from rest_framework.response import Response

class Geo(BaseView):
    """
    point = {"X":float,"Y":float,"Z":float}
    params:
        findTwoPointsLength          (point,point)               -> length:float
        findCenterAndRadius          (point,point,point)         -> centerPoint:Point,radius:float
        findToSlopeLine              (point,point)               -> slope:float
        findDegreeLineSlope          (slope:float)               -> degree:float
        findDegreeLineTwoPoints      (point,point)               -> degree:float
        convertDegreeToSlope         (degree:float)              -> slope:float
        convertRadianToDegree        (radian:float)              -> degree:float
        convertDegreeToRadians       (degree:float)              -> radian:float
        findCenterPointToLine        (point,point)               -> point
        findDegreeToBetweenTwoLines  (slope:float,slope:float)   -> degree:float
        findDotProductToTwoPoints    (point,point)               -> dotProduct:float
        findDifferenceTwoPoints      (point,point)               -> point
        wherePointOnLine             (point,point,point)         -> location:str
        findInsectionPointToTwoLines (point,point,point,point)   -> point
        findPointLength              (point,point,length:float)  -> point
        wherePointZone               (point,point)               -> zone:int
        findNearetPoint              (point,points:list[point])  -> point
    """
    def geo(self,data):pass
    
    def get(self, request, format=None):return Response()