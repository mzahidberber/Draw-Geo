from .BaseView import BaseView

class FindInsectionPointToTwoLines(BaseView):
    '''
    put four points and return lines intersection point
    :param [{"X":float,"Y":float,"Z":float},{"X":float,"Y":float,"Z":float},{"X":float,"Y":float,"Z":float},{"X":float,"Y":float,"Z":float}] 
    :param aid:list 
    :return:{"X":float,"Y":float,"Z":float}
    '''
    @BaseView.validationFourData
    def geo(self,data):
        result= self.geometricOperation.ikiDogrununKesisimNoktasiBulma(
            self.point(pointDict=dict(data[0])),
            self.point(pointDict=dict(data[1])),
            self.point(pointDict=dict(data[2])),
            self.point(pointDict=dict(data[3])))
        return self.response(result.to_Dict())
    
    def post(self, request, format=None):
        serializer=self.pointSerializer(data=request.data,many=True)
        if serializer.is_valid():
            return self.geo(serializer.data)
        else:
            return self.response(serializer.errors,status=self.status.HTTP_400_BAD_REQUEST)