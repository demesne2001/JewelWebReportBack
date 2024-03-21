from Entity.DTO.WsInput import CardandChartInput
from DAL import DBConfig
from Entity.DTO.WsResponse import CommanChartFilterResult

def GetBranch(input:CardandChartInput):
    result=CommanChartFilterResult()
    try:
        param=""
        
        result.lstResult=DBConfig.ExecuteDataReader(param,"Wr_MstBranch_GetForHelp","")
    except  Exception as E:
        print(E)
        result.HasError=True
        result.Message.append(E)
    return result 


def GetState(input:CardandChartInput):
    result=CommanChartFilterResult()
    try:
        param=""
        result.lstResult=DBConfig.ExecuteDataReader(param,"Wr_mstState_GetForHelp","")
    except  Exception as E:
        result.HasError=True
        result.Message.append(E)
    return result 


def GetCity(input:CardandChartInput):
    result=CommanChartFilterResult()
    try:
        param=""        
        result.lstResult=DBConfig.ExecuteDataReader(param,"Wr_mstCity_GetForHelp","")
    except  Exception as E:
        result.HasError=True
        result.Message.append(E)
    return result 



def GetRegion(input:CardandChartInput):
    result=CommanChartFilterResult()
    try:
        param=""
        # param=DBConfig.CommonParam(input)
        result.lstResult=DBConfig.ExecuteDataReader(param,"Wr_RegionName_GetForHelp","")
    except  Exception as E:
        result.HasError=True
        result.Message.append(E)
    return result 



def GetItem(input:CardandChartInput):
    result=CommanChartFilterResult()
    try:
        param=""
        
        param +=f" @strItemGroup='{input.strItemGroup}',"      
        param +=f" @strProduct='{input.strProduct}'"
   
        result.lstResult=DBConfig.ExecuteDataReader(param,"Wr_mstitem_GetForHelp","")
    except  Exception as E:
        result.HasError=True
        result.Message.append(E)
    return result 


def GetSubItem(input:CardandChartInput):
    result=CommanChartFilterResult()
    try:
        param=""        
        result.lstResult=DBConfig.ExecuteDataReader(param,"Wr_mstSubItem_GetForHelp","")
    except  Exception as E:
        result.HasError=True
        result.Message.append(E)
    return result 


def GetItemGroup(input:CardandChartInput):
    result=CommanChartFilterResult()
    try:
        param=""
        result.lstResult=DBConfig.ExecuteDataReader(param,"Wr_mstItemGroup_GetForHelp","")
    except  Exception as E:
        result.HasError=True
        result.Message.append(E)
    return result 


def GetItemWithSubitem(input:CardandChartInput):
    result=CommanChartFilterResult()
    try:
        param=""
        if(input.PageNo>0):
            param +=f" @PageNo={input.PageNo},"
        if(input.PageSize>0):
            param +=f" @PageSize={input.PageSize},"            
        if(input.strItem!=''):
            param +=f" @strItem='{input.strItem}',"
        if(input.strItemSubitem!=''):
            param +=f" @strItemSubitem='{input.strItemSubitem}',"            
        param +=f" @Search='{input.Search}'"
        result.lstResult=DBConfig.ExecuteDataReader(param,"Wr_mstItemSub_GetForHelp","")
    except  Exception as E:
        result.HasError=True
        result.Message.append(E)
    return result 


def GetPurchaseParty(input:CardandChartInput):
    result=CommanChartFilterResult()
    try:
        param=""
        param=DBConfig.CommonParam(input)
        if(input.PageNo>0):
            param +=f" @PageNo={input.PageNo},"
        if(input.PageSize>0):
            param +=f" @PageSize={input.PageSize},"
        param +=f" @Search='{input.Search}'"
                
        result.lstResult=DBConfig.ExecuteDataReader(param,"Wr_mstDesignCatalog_GetForHelp","")
    except  Exception as E:
        result.HasError=True
        result.Message.append(E)
    return result 



def GetSalesParty(input:CardandChartInput):
    result=CommanChartFilterResult()
    try:
        param=""
        if(input.PageNo>0):
            param +=f" @PageNo={input.PageNo},"
        if(input.PageSize>0):
            param +=f" @PageSize={input.PageSize},"
        param +=f" @Search='{input.Search}'"
        result.lstResult=DBConfig.ExecuteDataReader(param,"Wr_SalesParty_GetForHelp","")
    except  Exception as E:
        result.HasError=True
        result.Message.append(E)
    return result 



def GetSaleman(input:CardandChartInput):
    result=CommanChartFilterResult()
    try:
        param=""      
        result.lstResult=DBConfig.ExecuteDataReader(param,"Wr_mstSalesman_GetForHelp","")
    except  Exception as E:
        result.HasError=True
        result.Message.append(E)
    return result 


def GetProduct(input:CardandChartInput):
    result=CommanChartFilterResult()
    try:
        param=""
        result.lstResult=DBConfig.ExecuteDataReader(param,"Wr_MstProduct_GetForHelp","")
    except  Exception as E:
        result.HasError=True
        result.Message.append(E)
    return result 


def GetDesignCatalogue(input:CardandChartInput):
    result=CommanChartFilterResult()
    try:
        param=""
        if(input.PageNo>0):
            param +=f" @PageNo={input.PageNo},"
        if(input.PageSize>0):
            param +=f" @PageSize={input.PageSize},"            
        if(input.strItem!=''):
            param +=f" @strItem='{input.strItem}',"
        if(input.strItemSubitem!=''):
            param +=f" @strItemSubitem='{input.strItemSubitem}',"            
        param +=f" @Search='{input.Search}'"
        
        result.lstResult=DBConfig.ExecuteDataReader(param,"Wr_mstDesignCatalog_GetForHelp","")
    except  Exception as E:
        result.HasError=True
        result.Message.append(E)
    return result 


def GetModeSale(input:CardandChartInput):
    result=CommanChartFilterResult()
    try:
        param=""
        # param=DBConfig.CommonParam(input)
        result.lstResult=DBConfig.ExecuteDataReader(param,"Wr_mstChallanGenerateType_GetForHelp","")
    except  Exception as E:
        result.HasError=True
        result.Message.append(E)
    return result 



def GetTeamModeofSale(input:CardandChartInput):
    result=CommanChartFilterResult()
    try:
        param=""
        param=DBConfig.CommonParam(input)
        result.lstResult=DBConfig.ExecuteDataReader(param,"","")
    except  Exception as E:
        result.HasError=True
        result.Message.append(E)
    return result 



def GetDayBook(input:CardandChartInput):
    result=CommanChartFilterResult()
    try:
        param=""
        param=DBConfig.CommonParam(input)
        result.lstResult=DBConfig.ExecuteDataReader(param,"","")
    except  Exception as E:
        result.HasError=True
        result.Message.append(E)
    return result 


def GetMetalType(input:CardandChartInput):
    result=CommanChartFilterResult()
    try:
        param=""
        param=DBConfig.CommonParam(input)
        result.lstResult=DBConfig.ExecuteDataReader(param,"","")
    except  Exception as E:
        result.HasError=True
        result.Message.append(E)
    return result 

def GetSalesAging(input:CardandChartInput):
    result=CommanChartFilterResult()
    try:
        param=""        
        result.lstResult=DBConfig.ExecuteDataReader(param,"Wr_BIrpt_SalesSalesAging_GetForHelp","")
    except  Exception as E:
        result.HasError=True
        result.Message.append(E)
    return result 