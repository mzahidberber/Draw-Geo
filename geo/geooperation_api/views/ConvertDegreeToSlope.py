from .BaseView import BaseView
from geooperation_api.models.Response import Response
from django.http import JsonResponse
class ConvertDegreeToSlope(BaseView):
    '''
    put degree and return to slope radians
    :param {"degree":float} 
    :param aid:float 
    :return:{slope:float}
    '''
    @BaseView.validationOneData
    def geo(self,data):
        result= self.geometricOperation.acidanEgimBulma(data["degree"])
        return JsonResponse(Response.SuccessData(result,200),status=200)
    
    def post(self, request, format=None):
        serializer=self.degreeSeralizer(data=request.data)
        if serializer.is_valid():
            return self.geo(serializer.data)
        else:
            return JsonResponse(Response.FailError(serializer.errors,400),status=400)