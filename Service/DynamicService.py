from DAL import DBConfig
from Entity.DTO.WsInput import CommonFilter,VendorAddEditInput,VendorChartInput,VendorPageDetDataInput
from Entity.DTO.WsResponse import DynamicResult
from Service import jwtBearer



def GetChartValue(input:CommonFilter):
    result=DynamicResult()
    SpName=DBConfig.GetDynamicSpName(input.DychartID)
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


def GetChartDetail(input:VendorPageDetDataInput):
    result=DynamicResult()        
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
            param=""
            if(input.VendorID>0):
                param=f"@VendorID={input.VendorID}"
            else:
                param=f"@VendorID={jwtBearer.CVendorID}"
                
            if(input.PageID>0):
                param=f"@PageID={input.PageID}"
            else:
                param=f"@PageID=0"
            result.lstResult=DBConfig.CDBExecuteDataReader(param,"WR_MstVendorPage_GetData","VendorPageDataServiec")
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
        if(item.RowCHartcount == rowcount and item.RowNo==RowNo):
            RowNo=0
            rowcount=0
        elif(item.RowCHartcount != rowcount ):
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


    