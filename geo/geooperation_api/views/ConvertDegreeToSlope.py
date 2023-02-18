from .BaseView import BaseView

class ConvertDegreeToSlope(BaseView):
    '''
    put degree and return to slope radians
    :param {"degree":float} 
    :param aid:float 
    :return:{slope:float}
    '''
    @BaseView.validationOneData
    def geo(self,data):
        result= self.geometricOperation.acidanEgimBulma(data["degree"])
        return self.response({"slope":result})
    
    def post(self, request, format=None):
        serializer=self.degreeSeralizer(data=request.data)
        if serializer.is_valid():
            return self.geo(serializer.data)
        else:
            return self.response(serializer.errors,status=self.status.HTTP_400_BAD_REQUEST)