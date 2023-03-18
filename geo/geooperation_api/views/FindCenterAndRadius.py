from .BaseView import BaseView
from geooperation_api.models.Response import Response
from django.http import JsonResponse
class FindCenterAndRadius(BaseView):
    '''
    put tree points and return its center and radius 
    :param [{"X":float,"Y":float,"Z":float},{"X":float,"Y":float,"Z":float},{"X":float,"Y":float,"Z":float}] 
    :param aid:list 
    :return:{"radius": float,"centerPoint": {"X": float,"Y": float,"Z": float}}
    '''
    @BaseView.validationTreeData
    def geo(self,data):
        result= self.geometricOperation.merkezveYaricapBul(
            self.point(pointDict=dict(data[0])),
            self.point(pointDict=dict(data[1])),
            self.point(pointDict=dict(data[2])))
        return JsonResponse(Response.SuccessData({"radius":result[1],"centerPoint":result[0].to_Dict()},200),status=200)
    
    def post(self, request, format=None):
        serializer=self.pointSerializer(data=request.data,many=True)
        if serializer.is_valid():
            return self.geo(serializer.data)
        else:
            return JsonResponse(Response.FailError(serializer.errors,400),status=400)