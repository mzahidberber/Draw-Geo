
from .BaseView import BaseView
from geooperation_api.models.Response import Response
from django.http import JsonResponse
import logging

class FindPointOnCircle(BaseView):
    '''
    put two points and length return point
    :param [{"X":float,"Y":float,"Z":float},{"X":float,"Y":float,"Z":float}] and lenght:float
    :param aid:list 
    :return:{"X":float,"Y":float,"Z":float}
    '''
    # @BaseView.validationTwoData
    def geo(self,data):
        result= self.geometricOperation.findPointOnCircle(
            self.point(pointDict=dict(data[0]["point"])),data[0]["radius"],data[0]["angle"])
        self.logger.info(f"Run FindPointOnCircle {dict(data[0])}")
        return JsonResponse(Response.SuccessData(result.to_Dict(),200),status=200)
    
    # @method_decorator(ratelimit(key="ip",rate="2/s",method='POST'))
    def post(self, request, format=None):
        serializer=self.pointRadiusAngleSerializer(data=request.data,many=True)
        if serializer.is_valid():
            return self.geo(serializer.data)
        else:
            return JsonResponse(Response.FailError(serializer.errors,400),status=400)
