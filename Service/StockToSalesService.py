from DAL import DBConfig
from Entity.DTO.WsInput import StockToSalesInput
from Entity.DTO.WsResponse import CommanChartFilterResult


def GetStockToSalesChart(input:StockToSalesInput):
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
            result.lstResult=DBConfig.CDBExecuteDataReader(param,"WR_BI_rpt_StockAgainSales_GetChartData","GetStockToSalesChart")
        except  Exception as E:
            print(E)
            result.HasError=True
            result.Message.append(E)
    else:
        result.HasError=True
    return result 