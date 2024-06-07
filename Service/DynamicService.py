from DAL import DBConfig
from Entity.DTO.WsInput import CommonFilter,VendorAddEditInput,AddEditVendorPageInput,AddEditDynamicChartDetailInput,ChartTpeInput
from Entity.DTO.WsInput import VendorChartInput,VendorPageDetDataInput,VendorchartDetailScreenInput,VendorchartDetailInput
from Entity.DTO.WsResponse import DynamicResult
from Service import jwtBearer



def GetChartValue(input:CommonFilter):
    result=DynamicResult()
    SpName=DBConfig.GetDynamicSpName(input.DychartID,'WR_mstVendorDynamicChart_GetchartDetail')
    if(SpName == "" or SpName == None or len(SpName)<=0):
        result.Message.append("Please contact to Support Department")
    if(len(result.Message)==0):
        try:
            param="" 
            input.DychartID=0                   
            param=DBConfig.spParam(input)        
            print('param',param)
            print('SpName',SpName)
            result.lstResult=DBConfig.CDBExecuteDataReader(param,SpName,"GetChartValue")
        except  Exception as E:                    
            result.HasError=True
            result.Message.append(str(E))
    else:
        result.HasError=True
    return result

def GetChartDetailValue(input:VendorchartDetailInput):
    result=DynamicResult()
    print('inputttt',input)
    SpName=DBConfig.GetDynamicSpName(input.DyChartDetailID,'WR_mstVendorDynamicChartDetail_GetchartDetail')
    if(SpName == "" or SpName == None or len(SpName)<=0):
        result.Message.append("Please contact to Support Department")
    if(len(result.Message)==0):
        try:
            param="" 
            input.DyChartDetailID=0                   
            param=DBConfig.spParam(input)        
            print('param',param)
            print('SpName',SpName)
            result.lstResult=DBConfig.CDBExecuteDataReader(param,SpName,"GetChartDetailValue")
        except  Exception as E:                    
            result.HasError=True
            result.Message.append(str(E))
    else:
        result.HasError=True
    return result


def GetChartDetail(input:VendorPageDetDataInput):
    result=DynamicResult()  
    if(input.PageID<=0)      :
        result.Message.append("PageNo Required.......!!")
    if(len(result.Message)==0):
        try:
            param=""
            if(input.VendorID>0):
                param=f"@VendorID={input.VendorID},"
            else:
                param=f"@VendorID={jwtBearer.CVendorID},"                
            if(input.PageID>0):
                param+=f"@PageID={input.PageID}"
            else:
                param+=f"@PageID=0"
            print(param)
            result.lstResult=DBConfig.CDBExecuteDataReader(param,"WR_mstVendorDynamicChart_GetDetailByVendorID","GetChartValue")
        except  Exception as E:                    
            result.HasError=True
            result.Message.append(str(E))
    else:
        result.HasError=True
    return result

def GetVendorDetailByID(VendorID:int):
    result=DynamicResult()        
    if(len(result.Message)==0):
        try:
            param=""
            if(VendorID>0):
                param=f"@VendorID={VendorID}"
            else:
                param=f"@VendorID={jwtBearer.CVendorID}"
            result.lstResult=DBConfig.CDBExecuteDataReader(param,"WR_MstVendor_GetByID","GetVendorDetailByID")
        except  Exception as E:                    
            result.HasError=True
            result.Message.append(str(E))
    else:
        result.HasError=True
    return result

def VendorPageDataServiec(input:VendorPageDetDataInput):
    result=DynamicResult()        
    if(len(result.Message)==0):
        try:
            print('ommmmm',input)
            param=""
            if(input.VendorID>0):
                param=f"@VendorID={input.VendorID}"
            else:
                param=f"@VendorID={jwtBearer.CVendorID}"
                
            if(input.PageID>0):
                param+=f",@PageID={input.PageID}"
            else:
                param+=f",@PageID=0"
            print('param',param)
            result.lstResult=DBConfig.CDBExecuteDataReader(param,"WR_MstVendorPage_GetData","VendorPageDataServiec")
            print('result',result)
        except  Exception as E:                    
            result.HasError=True
            result.Message.append(str(E))
    else:
        result.HasError=True
    return result

def VendorchartDetailScreen(input:VendorchartDetailScreenInput):
    result=DynamicResult()        
    if(len(result.Message)==0):
        try:
            param=""
            if(input.VendorID>0):
                param=f"@VendorID={input.VendorID}"
            else:
                param=f"@VendorID={jwtBearer.CVendorID}"
                
            if(input.DyChartID>0):
                param=f"@DyChartID={input.DyChartID}"
            else:
                param=f"@DyChartID=0"
            print(param,' ommmmm')
            result.lstResult=DBConfig.CDBExecuteDataReader(param,"WR_mstVendorDynamicChartDetail_GetData","VendorchartDetailScreen")
        except  Exception as E:                    
            result.HasError=True
            result.Message.append(str(E))
    else:
        result.HasError=True
    return result


def GetDynamicDetailChart(input:VendorchartDetailScreenInput):
    result=DynamicResult()        
    if(len(result.Message)==0):
        try:
            param=""
            if(input.VendorID>0):
                param=f"@VendorID={input.VendorID}"
            else:
                param=f"@VendorID={jwtBearer.CVendorID}"
                
            if(input.DyChartID>0):
                param=f"@DyChartID={input.DyChartID}"            
            
            result.lstResult=DBConfig.CDBExecuteDataReader(param,"WR_mstVendorDynamicChartDetail_GetDataByID","GetDynamicDetailChart")
        except  Exception as E:                    
            result.HasError=True
            result.Message.append(str(E))
    else:
        result.HasError=True
    return result

def GetChartType(input:ChartTpeInput):
    result=DynamicResult()        
    if(len(result.Message)==0):
        try:
            param=f"@ID={input.ID}"            
            result.lstResult=DBConfig.CDBExecuteDataReader(param,"WR_mstchartType_GetByYAxis","GetChartType")
        except  Exception as E:                    
            result.HasError=True
            result.Message.append(str(E))
    else:
        result.HasError=True
    return result


def VendorAddEdit(input:VendorAddEditInput):
    result=DynamicResult()        
    if(len(result.Message)==0):
        try:            
            ID=0
            ID=DBConfig.CDBExecuteNonQuery(input,"WR_mstVendor_AddEdit","VendorAddEdit")
            if(ID>0):
                result.Message.append("Vendor Detail Fill Sucessfully")
            else:
                result.HasError=True
                result.Message.append("Something Went Wrong.....")
        except  Exception as E:                    
            result.HasError=True
            result.Message.append(str(E))
    else:
        result.HasError=True
    return result

def AddEditVendorPage(input:AddEditVendorPageInput):
    result=DynamicResult()
    if(input.VendorID<=0):
        result.Message.append('select Vendor...!')
    elif(input.PageName==""):
        result.Message.append('Please Enter Page Name')
        
    if(len(result.Message)==0):
        try:            
            ID=0
            ID=DBConfig.CDBExecuteNonQuery(input,"WR_mstVendorPage_AddEdit","AddEditVendorPage")
            if(ID>0):
                result.Message.append("Vendor Page Fill Sucessfully")
            elif(ID==-1):
                result.Message.append("Page name is already exists .......!")
            else:
                result.HasError=True
                result.Message.append("Something Went Wrong.....")
        except  Exception as E:                    
            result.HasError=True
            result.Message.append(str(E))
    else:
        result.HasError=True
    return result


def VendorChartAddEdit(input:VendorChartInput):
    result=DynamicResult() 
    rowcount=0       
    RowNo=0
    counter=0
    input.lstChartDetail.sort(key=lambda x: x.RowNo, reverse=True)
    for item in input.lstChartDetail:
        rowcount+=1        
        if(rowcount ==1):
            RowNo=item.RowNo
        if(item.RowChartCount == rowcount and item.RowNo==RowNo):
            RowNo=0
            rowcount=0
        elif(item.RowChartCount != rowcount ):
            if(counter < len(input.lstChartDetail)-1): 
                index=counter+1
                print('*********',index)
                obj= input.lstChartDetail[counter+1]
                print('=====>',obj)
                if( obj.RowNo != RowNo):                 
                    result.Message.append("Please Enter Valid Row and Chart Size")
            else:
                result.Message.append("Please Enter Valid Row and Chart Size")
        counter+=1
    if(len(result.Message)==0):
        try:            
            ID=0
            for item in input.lstChartDetail:                
                ID=DBConfig.CDBExecuteNonQuery(item,"WR_mstVendorDynamicChart_AddEdit","VendorAddEdit")
            if(ID>0):
                result.Message.append("Vendor Detail Fill Sucessfully")
            else:
                result.HasError=True
                result.Message.append("Something Went Wrong.....")
        except  Exception as E:                    
            result.HasError=True
            result.Message.append(str(E))
    else:
        result.HasError=True
    return result

def AddEditDynamicChartDetail(input:AddEditDynamicChartDetailInput):
    result=DynamicResult()
    input.lstChartDetail.sort(key=lambda x: x.SrNo, reverse=True)
    if(len(input.lstChartDetail)>0):
        if(input.lstChartDetail[0].TotalChart== len(input.lstChartDetail)):
            for item in input.lstChartDetail:
                if(item.ChartName==""):
                    result.Message.append("Please Enter ChartName ") 
                elif(item.ChartOption==""):
                    result.Message.append("Please Enter ChartOption ")
                elif(item.DefaultChart==""):
                    result.Message.append("Please Enter DefaultChart ")
                elif(item.SpName==""):
                    result.Message.append("Please Enter SpName ")
                elif(item.TotalChart==0):
                    result.Message.append("Please Enter TotalChart ")
                elif(item.DyChartID==0):
                    result.Message.append("Please Enter Parent Chart")
                elif(item.XLabel==""):
                    result.Message.append("Please Enter XLabel ")
                elif(item.XLabelID==""):
                    result.Message.append("Please Enter XLabelID")
                elif(item.YLabel==""):
                    result.Message.append("Please Enter YLabel ")                
        else:
            result.Message.append("Please Enter Valid Row ")    
    else:
        result.Message.append("Please Enter Chart Data")    
    if(len(result.Message)==0):
        try:            
            ID=0
            for item in input.lstChartDetail:                
                ID=DBConfig.CDBExecuteNonQuery(item,"WR_mstVendorDynamicChartDetail_AddEdit","AddEditDynamicChartDetail")
            if(ID>0):
                result.Message.append("Detail Chart Fill Sucessfully")            
            else:
                result.HasError=True
                result.Message.append("Something Went Wrong.....")
        except  Exception as E:                    
            result.HasError=True
            result.Message.append(str(E))
    else:
        result.HasError=True
    return result

    
def UtilityUserPassWordUpdate(VendorID):
    result=DynamicResult()
    lstUser=[]
    