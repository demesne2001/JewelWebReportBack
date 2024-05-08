from DAL import DBConfig
from Entity.DTO.WsInput import SchedulechartInput
from Entity.DTO.WsResponse import CommanChartFilterResult



def GetChartWise(input:SchedulechartInput):
    result=CommanChartFilterResult()
    try:
        param=""
        param=DBConfig.spParam(input)
        result.lstResult=DBConfig.CDBExecuteDataReader(param,"WR_Schedule_GetChart","GetChartWise")
    except  Exception as E:
        print(E)
        result.HasError=True
        result.Message.append(E)
    return result 

def GetCardWise(input:SchedulechartInput):
    result=CommanChartFilterResult()
    try:
        param=""
        param=DBConfig.spParam(input)
        result.lstResult=DBConfig.CDBExecuteDataReader(param,"WR_Schedule_GetCard","GetCardWise")
    except  Exception as E:
        print(E)
        result.HasError=True
        result.Message.append(E)
    return result 