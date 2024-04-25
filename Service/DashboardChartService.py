from Entity.DTO.WsInput import CardandChartInput,GetByID,AddEditChartOption,ChartWiseImageInput
from DAL import DBConfig
from Entity.DTO import WsInput
from Entity.DTO.WsResponse import CommanChartFilterResult
from Service import CommanScript

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
    if(input.Grouping==""):
        result.Message.append("Required Grouping")
    elif(input.SortBy==""):
        result.Message.append("Required SortBy")
    if(len(result.Message)==0):
        try:
            param=""
            param=DBConfig.CommonParam(input)
            if(len(param)>0):
                param+=f",@Grouping='{input.Grouping}'"
            else:
                param+=f"@Grouping='{input.Grouping}'"
            param+=f",@SortBy='{input.SortBy}'"
            if(input.SortByLabel !=''):
                param+=f",@SortByLabel='{input.SortByLabel}'"
            print('param',param)
            # result.lstResult=DBConfig.ExecuteDataReader(param,'Wr_BIrpt_Sales_GetChart',"GetCommanChart")
            result.lstResult=DBConfig.ExecuteDataReader(param,"Wr_BIrpt_Sales_GetChart","GetCommanChart")
        except  Exception as E:
            CommanScript.ErrorLog("GetCommanChart",DBConfig.spParam(input),"Wr_BIrpt_Sales_GetChart",E)
            result.HasError=True
            result.Message.append(str(E))
    else:
        result.HasError=True
    return result 

def GetDetailCommanChart(input:CardandChartInput):
    result=CommanChartFilterResult()
    try:
        param=""       
        
        param+=f"@Grouping='{input.Grouping}'"
        
        # result.lstResult=DBConfig.ExecuteDataReader(param,'Wr_BIrpt_Sales_GetChart',"GetCommanChart")
        result.lstResult=DBConfig.ExecuteDataReader(param,"WR_DetailWise_Chart","GetDetailCommanChart")
    except  Exception as E:
        CommanScript.ErrorLog("GetDetailCommanChart",DBConfig.spParam(input),"WR_DetailWise_Chart",E)
        result.HasError=True
        result.Message.append(str(E))
    return result 

def GetDetailChartImage(input:ChartWiseImageInput):
    result=CommanChartFilterResult() 
    if(len(result.Message)==0):
        try:
            param=""
            param=DBConfig.spParam(input)
            result.lstResult=DBConfig.ExecuteDataReader(param,"WR_GetBarcodeImage_GetByID","GetDetailChartImage")
        except  Exception as E:
            CommanScript.ErrorLog("GetCommanChart",DBConfig.spParam(input),"Wr_BIrpt_Sales_GetChart",E)
            result.HasError=True
            result.Message.append(str(E))
    else:
        result.HasError=True
    return result     
                
def GetChartOptionByID(input:GetByID):
    result=CommanChartFilterResult()
    try:
        print(input.ID)
        result.lstResult=DBConfig.ExecuteDataReader(f"@ID={input.ID}","WR_mstChartOption_GetByID","GetChartOptionByID")
    except  Exception as E:
        CommanScript.ErrorLog("GetChartOptionByID",f"@ID={input.ID}","WR_mstChartOption_GetByID",E)
        result.HasError=True
        result.Message.append(str(E))
    return result

def ChartOptionAddEdit(input:AddEditChartOption):
    result=CommanChartFilterResult()
    if(input.ChartOption==''):
        result.Message.append("ChartOption Required")
    elif(input.ChartID<=0):
        result.Message.append("ChartID Required")
    if(len(result.Message)==0):
        try:
            ID=0
            print('serviec')
            ID=DBConfig.ExecuteNonQuery(input,"WR_mstChartOption_AddEdit","ChartOptionAddEdit")
            if(ID>0):
                result.Message.append("Chart Option Updated Sucessfully")
            elif(ID == -1):
                result.Message.append("Already Have it...!")
            elif(ID ==-5):
                result.Message.append("Contact To Backend Developer")
                result.HasError=True
            
        except  Exception as E:
            CommanScript.ErrorLog("ChartOptionAddEdit",DBConfig.spParam(input),"WR_mstChartOption_AddEdit",E)
            result.HasError=True
            result.Message.append(str(E))
    else:
        result.HasError=True
    return result

def GetChartGroupByID(input:GetByID):
    result=CommanChartFilterResult()
    try:
        print(input.ID)
        result.lstResult=DBConfig.ExecuteDataReader(f"@ID={input.ID}","WR_mstChartGroup_GetByID","GetChartGroupByID")
    except  Exception as E:
        CommanScript.ErrorLog("GetChartGroupByID",f"@ID={input.ID}","WR_mstChartGroup_GetByID",E)
        result.HasError=True
        result.Message.append(E)
    return result

def ChartGroupAddEdit(input:WsInput.AddEditChartGroup):
    result=CommanChartFilterResult()
    if(input.ChartGroup==''):
        result.Message.append("ChartGroup Required")
    elif(input.ChartID<=0):
        result.Message.append("ChartID Required")
    if(len(result.Message)==0):
        try:
            ID=0
            print('serviec')
            ID=DBConfig.ExecuteNonQuery(input,"WR_mstChartGroup_AddEdit","ChartGroupAddEdit")
            if(ID>0):
                result.Message.append("Chart Group Updated Sucessfully")
            elif(ID == -1):
                result.Message.append("Already Have it...!")
            elif(ID ==-5):
                result.Message.append("Contact To Backend Developer")
                result.HasError=True
            
        except  Exception as E:
            CommanScript.ErrorLog("ChartGroupAddEdit",DBConfig.spParam(input),"WR_mstChartGroup_AddEdit",E)
            result.HasError=True
            result.Message.append(str(E))
    else:
        result.HasError=True
    return result