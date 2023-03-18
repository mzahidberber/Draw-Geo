from .BaseView import BaseView
from geooperation_api.models.Response import Response
from django.http import JsonResponse
class ConvertRadianToDegree(BaseView):
    '''
    put radians and return degree
    :param {"radians":float} 
    :param aid:float 
    :return:{degree:float}
    '''
    @BaseView.validationOneData
    def geo(self,data):
        result= self.geometricOperation.radyaniDereceyeCevirme(data["radians"])
        return JsonResponse(Response.SuccessData(result,200),status=200)
    
    def post(self, request, format=None):
        serializer=self.radianSerializer(data=request.data)
        if serializer.is_valid():
            return self.geo(serializer.data)
        else:
            return JsonResponse(Response.FailError(serializer.errors,400),status=400)