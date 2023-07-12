from .BaseView import BaseView
from geooperation_api.models.Response import Response
from django.http import JsonResponse
class WherePointsOnLine(BaseView):
    '''
    put tree points and return where p3 in line consisting of p2 and p1
    :param [{"X":float,"Y":float,"Z":float},{"X":float,"Y":float,"Z":float},{"X":float,"Y":float,"Z":float}] 
    :param aid:list 
    :return:{"location": str}
    '''
    @BaseView.validationTreeData
    def geo(self,data):
        result= self.geometricOperation.NoktaDogrununNeresindeBul(
            self.point(pointDict=dict(data[0])),
            self.point(pointDict=dict(data[1])),
            self.point(pointDict=dict(data[2])))
        self.logger.info(f"Run WherePointsOnLine p1:{dict(data[0])} p2:{dict(data[1])} p3:{dict(data[2])}")
        return JsonResponse(Response.SuccessData(result,200),status=200)
    
    def post(self, request, format=None):
        serializer=self.pointSerializer(data=request.data,many=True)
        if serializer.is_valid():
            return self.geo(serializer.data)
        else:
            return JsonResponse(Response.FailError(serializer.errors,400),status=400)