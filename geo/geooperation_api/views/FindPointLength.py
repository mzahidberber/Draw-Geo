from .BaseView import BaseView
from geooperation_api.models.Response import Response
from django.http import JsonResponse
class FindPointLength(BaseView):
    '''
    put two points and length return point
    :param [{"X":float,"Y":float,"Z":float},{"X":float,"Y":float,"Z":float}] and lenght:float
    :param aid:list 
    :return:{"X":float,"Y":float,"Z":float}
    '''
    # @BaseView.validationTwoData
    def geo(self,data,length):
        result= self.geometricOperation.uzunluktakiNoktayiBul(
            self.point(pointDict=dict(data[0])),
            self.point(pointDict=dict(data[1])),length)
        return JsonResponse(Response.SuccessData(result.to_Dict(),200),status=200)
    
    def post(self, request, format=None):
        serializer=self.pointSerializer(data=request.data,many=True)
        if serializer.is_valid():
            length=request.GET.get("length",None)
            if length != None and float(length)!=0:
                return self.geo(serializer.data,float(length))
            else:
                return JsonResponse(Response.FailError(serializer.errors,400),status=400)
        else:
            return JsonResponse(Response.FailError(serializer.errors,400),status=400)