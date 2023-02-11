from .BaseView import BaseView

class FindDegreeToBetweenTwoLines(BaseView):
    '''
    put two slopes and return degree to between two line 
    :param [{slope:float},{slope:float}]
    :param aid:float 
    :return:{degree:float}
    '''
    @BaseView.validationTwoData
    def geo(self,data):
        result= self.geometricOperation.ikiDogruArasiAciBulma(data[0]["slope"],data[1]["slope"])
        return self.response({"degree":result})
    
    def post(self, request, format=None):
        serializer=self.slopeSerializer(data=request.data,many=True)
        if serializer.is_valid():
            return self.geo(serializer.data)
        else:
            return self.response(serializer.errors,status=self.status.HTTP_400_BAD_REQUEST)