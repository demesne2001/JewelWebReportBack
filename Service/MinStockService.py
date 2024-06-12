from Entity.DTO.WsInput import StockToSalesInput,MinSubitemDeatil
from Entity.DTO.WsResponse import CommanChartFilterResult
from DAL import DBConfig

def GetMinStockChart(input:StockToSalesInput):
    result=CommanChartFilterResult()
    if(input.FromDate == ""):
        result.Message.append("Required Field From Date")
    elif(input.Mode <=0):\
        result.Message.append("Required Field Mode")
    elif(input.Mode ==1):
        if(input.MonthType == ""):
            result.Message.append("Required Field MonthType")
    if(len(result.Message)==0):        
        try:
            param=""
            param=DBConfig.spParam(input)
            result.lstResult=DBConfig.CDBExecuteDataReader(param,"WR_mstMinMaxStock_Getchart","GetMinStockChart")
        except  Exception as E:
            print(E)
            result.HasError=True
            result.Message.append(E)
    else:
        result.HasError=True
    return result 


def GetMinStockDeatilChart(input:MinSubitemDeatil):
    result=CommanChartFilterResult()
    if(input.FromDate == ""):
        result.Message.append("Required Field From Date")
    elif(input.SubItemID <=0):\
        result.Message.append("Required Field Sub  Item")
    elif(input.ToDate ==""):
         result.Message.append("Required Field To  Date")
    if(len(result.Message)==0):        
        try:
            param=""
            param=DBConfig.spParam(input)
            result.lstResult=DBConfig.CDBExecuteDataReader(param,"WR_Bi_MstMinStock_GetDetailchart","GetMinStockDeatilChart")
        except  Exception as E:
            print(E)
            result.HasError=True
            result.Message.append(E)
    else:
        result.HasError=True
    return result 