from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from geooperation_api.models import Point
from geooperation_api.serializer import PointSerializer,SlopeSerializer,DegreeSerializer,PointAndListSerializer,RadiansSerializer
from geooperation_api.geometric.GeometricOperations import GeometricOperation
from abc import ABC,abstractmethod
# from adrf.views import APIView


class BaseView(APIView,ABC):
    response=Response
    status=status
    point=Point
    slopeSerializer=SlopeSerializer
    pointSerializer=PointSerializer
    degreeSeralizer=DegreeSerializer
    radianSerializer=RadiansSerializer
    geometricOperation=GeometricOperation
    pointAndListSerializer=PointAndListSerializer

    @abstractmethod
    def geo(self,data):pass

    @staticmethod
    def validationOneData(func):
        "Validation data elements count and is one return func or isnt one return error response"
        def __inner(cls,data:list or None):
            if(len(data)==1):
                return func(cls,data)
            else:
                return Response({"error":"value"},status=status.HTTP_400_BAD_REQUEST)
        return __inner

    @staticmethod
    def validationTwoData(func):
        "Validation data elements count and is two return func or isnt two return error response"
        def __inner(cls,data:list or None):
            if(len(data)==2):
                return func(cls,data)
            else:
                return Response({"error":"put 2 elements"},status=status.HTTP_400_BAD_REQUEST)
        return __inner
    
    @staticmethod
    def validationTreeData(func):
        "Validation data elements count and is tree return func or isnt tree return error response"
        def __inner(cls,data:list or None):
            if(len(data)==3):
                return func(cls,data)
            else:
                return Response({"error":"put 3 elements"},status=status.HTTP_400_BAD_REQUEST)
        return __inner
    
    @staticmethod
    def validationFourData(func):
        "Validation data elements count and is tree return func or isnt tree return error response"
        def __inner(cls,data:list or None):
            if(len(data)==4):
                return func(cls,data)
            else:
                return Response({"error":"put 3 elements"},status=status.HTTP_400_BAD_REQUEST)
        return __inner

    @staticmethod
    def validateSeriazer(func):
        def inner(cls,serializer):
            if serializer.is_valid():
                return func(cls,serializer)
            else:
                return Response({"error":"error"},status=status.HTTP_400_BAD_REQUEST)
        return inner
    
    
    