from .BaseView import BaseView

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
        return self.response({"location":result})
    
    def post(self, request, format=None):
        serializer=self.pointSerializer(data=request.data,many=True)
        if serializer.is_valid():
            return self.geo(serializer.data)
        else:
            return self.response(serializer.errors,status=self.status.HTTP_400_BAD_REQUEST)