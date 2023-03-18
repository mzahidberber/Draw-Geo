
class Response:
    
    
    @staticmethod
    def SuccessData(data,statusCode:int) -> dict:
        return {"data":data,"statusCode":statusCode,"errors":None}
    
    @staticmethod
    def SuccessCode(statusCode:int) -> dict:
        return {"data":None,"statusCode":statusCode,"errors":None}
    
    
    @staticmethod
    def FailError(errors:str or list[str],statusCode:int)-> dict:
        return {"data":None,"statusCode":statusCode,"errors":errors}
    
