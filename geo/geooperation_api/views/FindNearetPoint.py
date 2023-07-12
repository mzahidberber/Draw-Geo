from .BaseView import BaseView
from geooperation_api.models.Response import Response
from django.http import JsonResponse
class FindNearetPoint(BaseView):
    '''
    put point and points return neareast point
    :param {"point":"X":float,"Y":float,"Z":float,"points":[{"X":float,"Y":float,"Z":float},{"X":float,"Y":float,"Z":float},...]
    :param aid:list 
    :return:{"X":float,"Y":float,"Z":float}
    '''
    
    def geo(self,data):
        result= self.geometricOperation.enyakinNoktayiBul(
            self.point(pointDict=dict(data["point"])),
            list(map(lambda x :self.point(pointDict=dict(x)),data["points"])))
        self.logger.info(f"Run FindNearetPoint point:{dict(data['point'])} points:{data['points']}")
        return JsonResponse(Response.SuccessData(result.to_Dict(),200),status=200)
    
    def post(self, request, format=None):
        serializer=self.pointAndListSerializer(data=request.data)
        if serializer.is_valid():
            return self.geo(serializer.data)
        else:
            return JsonResponse(Response.FailError(serializer.errors,400),status=400)