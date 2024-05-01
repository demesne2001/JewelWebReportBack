from Entity.DTO.WsInput import CardandChartInput
from Entity.DTO.WsResponse import CommanChartFilterResult
from DAL import DBConfig
from Service import CommanScript

def GetSalesEfficiencyCard(input:CardandChartInput):
    result=CommanChartFilterResult()
    try:
        param=""
        param=DBConfig.CommonParam(input)
        result.lstResult=DBConfig.ExecuteDataReader(param,"","")
    except  Exception as E:
        result.HasError=True
        result.Message.append(E)
    return result 


def GetReturnTrendCard(input:CardandChartInput):
    result=CommanChartFilterResult()
    try:
        param=""
        param=DBConfig.CommonParam(input)
        result.lstResult=DBConfig.ExecuteDataReader(param,"","")
    except  Exception as E:
        result.HasError=True
        result.Message.append(E)
    return result 
 

def GetSalesWeightCard(input:CardandChartInput):
    result=CommanChartFilterResult()
    try:
        param=""
        param=DBConfig.CommonParam(input)
        result.lstResult=DBConfig.ExecuteDataReader(param,"","")
    except  Exception as E:
        result.HasError=True
        result.Message.append(E)
    return result
 

def GetCollectionCard(input:CardandChartInput):
    result=CommanChartFilterResult()
    try:
        param=""
        param=DBConfig.CommonParam(input)
        result.lstResult=DBConfig.ExecuteDataReader(param,"","")
    except  Exception as E:
        result.HasError=True
        result.Message.append(E)
    return result
 

def GetStockAnalysisCard(input:CardandChartInput):
    result=CommanChartFilterResult()
    try:
        param=""
        param=DBConfig.CommonParam(input)
        result.lstResult=DBConfig.ExecuteDataReader(param,"","")
    except  Exception as E:
        result.HasError=True
        result.Message.append(E)
    return result

def GetCardValue(input:CardandChartInput):
    print('Service')
    result=CommanChartFilterResult()
    try:
        param=""
        print('input',input)
        param=DBConfig.CommonParam(input)
        if(len(param)>0):
            param+=f",@Grouping='{input.Grouping}'"
        else:
            param+=f"@Grouping='{input.Grouping}'"
        print('param',param)
        result.lstResult=DBConfig.CDBExecuteDataReader(param,"Wr_Dashboard_GetCard","GetCardValue")
    except  Exception as E:        
        CommanScript.ErrorLog("GetCardValue",DBConfig.spParam(input),"Wr_Dashboard_GetCard",E)
        result.HasError=True
        result.Message.append(str(E))
    return result




