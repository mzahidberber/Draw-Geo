from .BaseView import BaseView
from geooperation_api.models.Response import Response
from django.http import JsonResponse
class WherePointZone(BaseView):
    '''
    put origin and point and return where point in zone
    :param [{"X":float,"Y":float,"Z":float},{"X":float,"Y":float,"Z":float}] 
    :param aid:list 
    :return:{"zone": int}
    '''
    @BaseView.validationTwoData
    def geo(self,data):
        result= self.geometricOperation.noktaHangiBolgedeBul(
            self.point(pointDict=dict(data[0])),
            self.point(pointDict=dict(data[1])))
        return JsonResponse(Response.SuccessData(result,200),status=200)
    
    def post(self, request, format=None):
        serializer=self.pointSerializer(data=request.data,many=True)
        if serializer.is_valid():
            return self.geo(serializer.data)
        else:
            return JsonResponse(Response.FailError(serializer.errors,400),status=400)