from .BaseView import BaseView

class ConvertDegreeToRadians(BaseView):
    '''
    put degree and return radians
    :param {"degree":float} 
    :param aid:float 
    :return:{radians:float}
    '''
    @BaseView.validationOneData
    def geo(self,data):
        result= self.geometricOperation.dereceyiRadyanaCevirme(data["degree"])
        return self.response({"radians":result})
    
    def post(self, request, format=None):
        serializer=self.degreeSeralizer(data=request.data)
        if serializer.is_valid():
            return self.geo(serializer.data)
        else:
            return self.response(serializer.errors,status=self.status.HTTP_400_BAD_REQUEST)