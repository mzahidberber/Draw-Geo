from .BaseView import BaseView
from geooperation_api.models.Response import Response
from django.http import JsonResponse
class FindDegreeLineSlope(BaseView):
    '''
    put slope and return to degree line
    :param [{"X":float,"Y":float,"Z":float},{"X":float,"Y":float,"Z":float}] 
    :param aid:list 
    :return:{degree:float}
    '''
    @BaseView.validationOneData
    def geo(self,data):
        result= self.geometricOperation.dogruAciBulma(data["slope"])
        self.logger.info(f"Run FindDegreeLineSlope slope:{data['slope']}")
        return JsonResponse(Response.SuccessData(result,200),status=200)
    
    def post(self, request, format=None):
        serializer=self.slopeSerializer(data=request.data)
        if serializer.is_valid():
            return self.geo(serializer.data)
        else:
            return JsonResponse(Response.FailError(serializer.errors,400),status=400)