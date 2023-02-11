from .BaseView import BaseView

class ConvertRadianToDegree(BaseView):
    '''
    put radians and return degree
    :param {"radians":float} 
    :param aid:float 
    :return:{degree:float}
    '''
    @BaseView.validationOneData
    def geo(self,data):
        result= self.geometricOperation.radyaniDereceyeCevirme(data["radians"])
        return self.response({"degree":result})
    
    def post(self, request, format=None):
        serializer=self.radianSerializer(data=request.data)
        if serializer.is_valid():
            return self.geo(serializer.data)
        else:
            return self.response(serializer.errors,status=self.status.HTTP_400_BAD_REQUEST)