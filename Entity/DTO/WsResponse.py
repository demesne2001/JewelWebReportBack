from pydantic import BaseModel,Field

class CommonResult:
    def __init__(self):
        self.Message = []
        self.HasError = False

class CommanChartFilterResult(CommonResult):
    def __init__(self):
        super().__init__()
        self.lstResult:[] 