from .BaseView import BaseView
from geooperation_api.models.Response import Response
from django.http import JsonResponse
class FindDegreeToBetweenTwoLines(BaseView):
    '''
    put two slopes and return degree to between two line 
    :param [{slope:float},{slope:float}]
    :param aid:float 
    :return:{degree:float}
    '''
    @BaseView.validationTwoData
    def geo(self,data):
        result= self.geometricOperation.ikiDogruArasiAciBulma(data[0]["slope"],data[1]["slope"])
        return JsonResponse(Response.SuccessData(result,200),status=200)
    
    def post(self, request, format=None):
        serializer=self.slopeSerializer(data=request.data,many=True)
        if serializer.is_valid():
            return self.geo(serializer.data)
        else:
            return JsonResponse(Response.FailError(serializer.errors,400),status=400)