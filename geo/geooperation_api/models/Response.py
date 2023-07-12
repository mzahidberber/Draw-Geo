import logging

class Response:
    
    
    @staticmethod
    def SuccessData(data,statusCode:int) -> dict:
        logging.getLogger().info(f"RETURN data: {data} status: {statusCode}")
        return {"data":data,"statusCode":statusCode,"error":None}
    
    @staticmethod
    def SuccessCode(statusCode:int) -> dict:
        logging.getLogger().info(f"RETURN data: None status: {statusCode}")
        return {"data":None,"statusCode":statusCode,"error":None}
    
    
    @staticmethod
    def FailError(errors:str or list[str],statusCode:int)-> dict:
        logging.getLogger().info(f"RETURN data: None status: {statusCode} error: {errors}")
        return {"data":None,"statusCode":statusCode,"error":errors}
    
