from django.db import models
from enum import Enum

class PInfo(Enum):
    "PointInformation"
    X="X"
    Y="Y"
    Z="Z"

class Point(models.Model):
    _X=models.FloatField()
    _Y=models.FloatField()
    _Z=models.FloatField()

    @property
    def X(self) -> float:return self._X
    @X.setter
    def X(self,point:float) -> None:self._X=point
    
    @property
    def Y(self) -> float:return self._Y
    @Y.setter
    def Y(self,point:float) -> None:self._Y=point

    @property
    def Z(self) -> float:return self._Z
    @Z.setter
    def Z(self,point:float) -> None:self._Z=point

    def __init__(self,x:float or None=1,y:float or None=1,z:float or None=1,pointDict:dict=None):
        if pointDict!=None and type(pointDict)==dict:
            self._X=pointDict[PInfo.X.value]
            self._Y=pointDict[PInfo.Y.value]
            self._Z=pointDict[PInfo.Z.value]
        else:
            self._X=x
            self._Y=y
            self._Z=z
    
    

    def to_Dict(self) -> dict:
        return {
            PInfo.X.value:self._X,
            PInfo.Y.value:self._Y,
            PInfo.Z.value:self._Z
        }
    
    
