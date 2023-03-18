from .BaseView import BaseView
from geooperation_api.models.Response import Response
from django.http import JsonResponse

class ConvertDegreeToRadians(BaseView):
    '''
    put degree and return radians
    :param {"degree":float} 
    :param aid:float 
    :return:{"data":float,"statusCode":int,"error":null  }
    '''
    @BaseView.validationOneData
    def geo(self,data):
        result= self.geometricOperation.dereceyiRadyanaCevirmeAsync(data["degree"])
        return JsonResponse(Response.SuccessData(result,200),status=200)
    
    def post(self, request, format=None):
        serializer=self.degreeSeralizer(data=request.data)
        if serializer.is_valid():
            return self.geo(serializer.data)
        else:
            return JsonResponse(Response.FailError(serializer.errors,400),status=400)