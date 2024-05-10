from DAL import DBConfig
from Entity.DTO.WsInput import SchedulechartInput,ScheduleDetailInput,ScheduleAllDetailInput,SchedulePartyDetailInput
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

def GetChartDetailWise(input:ScheduleDetailInput):
    result=CommanChartFilterResult()
    try:
        param=""
        param=DBConfig.spParam(input)
        result.lstResult=DBConfig.CDBExecuteDataReader(param,"WR_Schedule_GetDetailChart","GetChartDetailWise")
    except  Exception as E:
        print(E)
        result.HasError=True
        result.Message.append(E)
    return result 

def GetChartAllOverDetails(input:ScheduleAllDetailInput):
    result=CommanChartFilterResult()
    try:
        param=""
        param=DBConfig.spParam(input)
        result.lstResult=DBConfig.CDBExecuteDataReader(param,"WR_ScheduleID_GetAllDetail","GetChartAllOverDetails")
    except  Exception as E:
        print(E)
        result.HasError=True
        result.Message.append(E)
    return result 

def GetChartPartyOverDetails(input:SchedulePartyDetailInput):
    result=CommanChartFilterResult()
    try:
        param=""
        param=DBConfig.spParam(input)
        result.lstResult=DBConfig.CDBExecuteDataReader(param,"Wr_Schedule_GetPartyDetailOverview","GetChartAllOverDetails")
    except  Exception as E:
        print(E)
        result.HasError=True
        result.Message.append(E)
    return result 