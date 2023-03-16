
class Response:
    
    @staticmethod
    def SuccessData(data:list[dict],statusCode:int) -> dict:
        return {"data":data,"statusCode":statusCode,"errors":{}}
    
    @staticmethod
    def SuccessCode(statusCode:int) -> dict:
        return {"data":{},"statusCode":statusCode,"errors":{}}
    
    @staticmethod
    def FailErrors(errors:list[str],statusCode:int) -> dict:
        return {"data":{},"statusCode":statusCode,"errors":errors}
    
    @staticmethod
    def FailError(errorMessage:str,statusCode:int)-> dict:
        return {"data":{},"statusCode":statusCode,"errors":errorMessage}
    
