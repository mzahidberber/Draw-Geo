from .BaseView import BaseView
from geooperation_api.models.Response import Response
from django.http import JsonResponse
# from django_ratelimit.decorators import ratelimit
# from django.utils.decorators import method_decorator
class FindStartAndStopAngle(BaseView):
    '''
    put two points and length return point
    :param [{"X":float,"Y":float,"Z":float},{"X":float,"Y":float,"Z":float}] and lenght:float
    :param aid:list 
    :return:{"X":float,"Y":float,"Z":float}
    '''
    @BaseView.validationFourData
    def geo(self,data):
        result= self.geometricOperation.baslagicBitisAcisiBul(
            self.point(pointDict=dict(data[0])),
            self.point(pointDict=dict(data[1])),
            self.point(pointDict=dict(data[2])),
            self.point(pointDict=dict(data[3])),
            )
        return JsonResponse(Response.SuccessData({"startAngle":result[0],"stopAngle":result[1]},200),status=200)
    
    # @method_decorator(ratelimit(key="ip",rate="2/s",method='POST'))
    def post(self, request, format=None):
        serializer=self.pointSerializer(data=request.data,many=True)
        if serializer.is_valid():
            return self.geo(serializer.data)
        else:
            return JsonResponse(Response.FailError(serializer.errors,400),status=400)