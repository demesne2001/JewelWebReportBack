from Entity.DTO.WsInput import CardandChartInput
from DAL import DBConfig
from Entity.DTO.WsResponse import CommanChartFilterResult

def GetBranchWise(input:CardandChartInput):
    result=CommanChartFilterResult()
    try:
        param=""
        param=DBConfig.CommonParam(input)
        result.lstResult=DBConfig.ExecuteDataReader(param,"","")
    except  Exception as E:
        print(E)
        result.HasError=True
        result.Message.append(E)
    return result 
 


def GetStateWise(input:CardandChartInput):
    result=CommanChartFilterResult()
    try:
        param=""
        param=DBConfig.CommonParam(input)
        result.lstResult=DBConfig.ExecuteDataReader(param,"","")
    except  Exception as E:
        result.HasError=True
        result.Message.append(E)
    return result 
 


def GetCityWise(input:CardandChartInput):
    result=CommanChartFilterResult()
    try:
        param=""
        param=DBConfig.CommonParam(input)
        result.lstResult=DBConfig.ExecuteDataReader(param,"","")
    except  Exception as E:
        result.HasError=True
        result.Message.append(E)
    return result 
 
 

def GetRegionWise(input:CardandChartInput):
    result=CommanChartFilterResult()
    try:
        param=""
        param=DBConfig.CommonParam(input)
        result.lstResult=DBConfig.ExecuteDataReader(param,"","")
    except  Exception as E:
        result.HasError=True
        result.Message.append(E)
    return result 
 

def GetItemWise(input:CardandChartInput):
    result=CommanChartFilterResult()
    try:
        param=""
        param=DBConfig.CommonParam(input)
        result.lstResult=DBConfig.ExecuteDataReader(param,"","")
    except  Exception as E:
        result.HasError=True
        result.Message.append(E)
    return result 
 

def GetSubItemWise(input:CardandChartInput):
    result=CommanChartFilterResult()
    try:
        param=""
        param=DBConfig.CommonParam(input)
        result.lstResult=DBConfig.ExecuteDataReader(param,"","")
    except  Exception as E:
        result.HasError=True
        result.Message.append(E)
    return result 
 

def GetItemGroupWise(input:CardandChartInput):
    result=CommanChartFilterResult()
    try:
        param=""
        param=DBConfig.CommonParam(input)
        result.lstResult=DBConfig.ExecuteDataReader(param,"","")
    except  Exception as E:
        result.HasError=True
        result.Message.append(E)
    return result 
 


def GetItemWithSubItemWise(input:CardandChartInput):
    result=CommanChartFilterResult()
    try:
        param=""
        param=DBConfig.CommonParam(input)
        result.lstResult=DBConfig.ExecuteDataReader(param,"","")
    except  Exception as E:
        result.HasError=True
        result.Message.append(E)
    return result 
 


def GetPurchasePartywise(input:CardandChartInput):
    result=CommanChartFilterResult()
    try:
        param=""
        param=DBConfig.CommonParam(input)
        result.lstResult=DBConfig.ExecuteDataReader(param,"","")
    except  Exception as E:
        result.HasError=True
        result.Message.append(E)
    return result 
 
 

def GetSalesPartyWise(input:CardandChartInput):
    result=CommanChartFilterResult()
    try:
        param=""
        param=DBConfig.CommonParam(input)
        result.lstResult=DBConfig.ExecuteDataReader(param,"","")
    except  Exception as E:
        result.HasError=True
        result.Message.append(E)
    return result 
 

def GetProductWise(input:CardandChartInput):
    result=CommanChartFilterResult()
    try:
        param=""
        param=DBConfig.CommonParam(input)
        result.lstResult=DBConfig.ExecuteDataReader(param,"","")
    except  Exception as E:
        result.HasError=True
        result.Message.append(E)
    return result 
 

def GetDesignCatalogueWise(input:CardandChartInput):
    result=CommanChartFilterResult()
    try:
        param=""
        param=DBConfig.CommonParam(input)
        result.lstResult=DBConfig.ExecuteDataReader(param,"","")
    except  Exception as E:
        result.HasError=True
        result.Message.append(E)
    return result 
 

def GetMonthWise(input:CardandChartInput):
    result=CommanChartFilterResult()
    try:
        param=""
        param=DBConfig.CommonParam(input)
        result.lstResult=DBConfig.ExecuteDataReader(param,"","")
    except  Exception as E:
        result.HasError=True
        result.Message.append(E)
    return result 
 


def GetYearWise(input:CardandChartInput):
    result=CommanChartFilterResult()
    try:
        param=""
        param=DBConfig.CommonParam(input)
        result.lstResult=DBConfig.ExecuteDataReader(param,"","")
    except  Exception as E:
        result.HasError=True
        result.Message.append(E)
    return result 
 


def GetSalesAgingWise(input:CardandChartInput):
    result=CommanChartFilterResult()
    try:
        param=""
        param=DBConfig.CommonParam(input)
        result.lstResult=DBConfig.ExecuteDataReader(param,"","")
    except  Exception as E:
        result.HasError=True
        result.Message.append(E)
    return result 
 
 

def GetModeOfSalesWise(input:CardandChartInput):
    result=CommanChartFilterResult()
    try:
        param=""
        param=DBConfig.CommonParam(input)
        result.lstResult=DBConfig.ExecuteDataReader(param,"","")
    except  Exception as E:
        result.HasError=True
        result.Message.append(E)
    return result 
 

def GetTeamAndModeOFSalesWise(input:CardandChartInput):
    result=CommanChartFilterResult()
    try:
        param=""
        param=DBConfig.CommonParam(input)
        result.lstResult=DBConfig.ExecuteDataReader(param,"","")
    except  Exception as E:
        result.HasError=True
        result.Message.append(E)
    return result 
 

def GetSalesmanWise(input:CardandChartInput):
    result=CommanChartFilterResult()
    try:
        param=""
        param=DBConfig.CommonParam(input)
        result.lstResult=DBConfig.ExecuteDataReader(param,"","")
    except  Exception as E:
        result.HasError=True
        result.Message.append(E)
    return result 

def GetCommanChart(input:CardandChartInput):
    result=CommanChartFilterResult()
    try:
        param=""
        param=DBConfig.CommonParam(input)
        if(len(param)>0):
            param+=f",@Grouping='{input.Grouping}'"
        print('param',param)
        # result.lstResult=DBConfig.ExecuteDataReader(param,'Wr_BIrpt_Sales_GetChart',"GetCommanChart")
        result.lstResult=DBConfig.ExecuteDataReader(param,"Wr_BIrpt_Sales_GetChart","")
    except  Exception as E:
        result.HasError=True
        result.Message.append(E)
    return result 