from .BaseView import BaseView

class FindDegreeLineSlope(BaseView):
    '''
    put slope and return to degree line
    :param [{"X":float,"Y":float,"Z":float},{"X":float,"Y":float,"Z":float}] 
    :param aid:list 
    :return:{degree:float}
    '''
    @BaseView.validationOneData
    def geo(self,data):
        result= self.geometricOperation.dogruAciBulma(data["slope"])
        return self.response({"degree":result})
    
    def post(self, request, format=None):
        serializer=self.slopeSerializer(data=request.data)
        if serializer.is_valid():
            return self.geo(serializer.data)
        else:
            return self.response(serializer.errors,status=self.status.HTTP_400_BAD_REQUEST)