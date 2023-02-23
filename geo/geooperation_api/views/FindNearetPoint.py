from .BaseView import BaseView

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
        return self.response(result.to_Dict())
    
    def post(self, request, format=None):
        serializer=self.pointAndListSerializer(data=request.data)
        if serializer.is_valid():
            return self.geo(serializer.data)
        else:
            return self.response(serializer.errors,status=self.status.HTTP_400_BAD_REQUEST)