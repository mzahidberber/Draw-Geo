from .BaseView import BaseView
from geooperation_api.models.Response import Response
from django.http import JsonResponse
class FindCenterPointToLine(BaseView):
    '''
    put two points and return line center point
    :param [{"X":float,"Y":float,"Z":float},{"X":float,"Y":float,"Z":float}] 
    :param aid:list 
    :return:{"X":float,"Y":float,"Z":float}
    '''
    @BaseView.validationTwoData
    def geo(self,data):
        result= self.geometricOperation.cizgiOrtaNokta(
            self.point(pointDict=dict(data[0])),
            self.point(pointDict=dict(data[1])))
        return JsonResponse(Response.SuccessData(result.to_Dict(),200),status=200)
    
    def post(self, request, format=None):
        serializer=self.pointSerializer(data=request.data,many=True)
        if serializer.is_valid():
            return self.geo(serializer.data)
        else:
            return JsonResponse(Response.FailError(serializer.errors,400),status=400)