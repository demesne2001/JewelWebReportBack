from pydantic import BaseModel,Field

class CommonResult:
    def __init__(self):
        self.Message = []
        self.HasError = False

class CommanChartFilterResult(CommonResult):
    def __init__(self):
        super().__init__()
        self.lstResult:[] 
        
class ErrorLog(BaseModel):
    def __init__(self):
        self.ErrorDate:str
        self.ErrorMethod:str
        self.ErrorParam:str        
        self.ErrorSpNAme:str
        self.ErrorException:str
        
class ImageRsult(CommonResult):
    def __init__(self):
        super().__init__()
        self.ImageName:str
        