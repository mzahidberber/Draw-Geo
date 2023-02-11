from .BaseView import BaseView
class FindDegreeLineTwoPoints(BaseView):
    '''
    put two points and return line degree
    :param [{"X":float,"Y":float,"Z":float},{"X":float,"Y":float,"Z":float}] 
    :param aid:list 
    :return:{degree:float}
    '''
    @BaseView.validationTwoData
    def geo(self,data):
        result= self.geometricOperation.dogruAciBul(
            self.point(pointDict=dict(data[0])),
            self.point(pointDict=dict(data[1])))
        return self.response({"degree":result})
    
    def post(self, request, format=None):
        serializer=self.pointSerializer(data=request.data,many=True)
        if serializer.is_valid():
            return self.geo(serializer.data)
        else:
            return self.response(serializer.errors,status=self.status.HTTP_400_BAD_REQUEST)