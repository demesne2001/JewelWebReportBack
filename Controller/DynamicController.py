from fastapi import APIRouter,Body,Depends
from Service import DynamicService
from Entity.DTO.WsInput import CommonFilter,VendorAddEditInput,VendorChartInput,VendorPageDetDataInput,VendorchartDetailScreenInput,VendorchartDetailInput
from Entity.DTO.WsResponse import DynamicResult


Dynamic=APIRouter()

@Dynamic.post('/GetcommonChart')
def GetcommonChart(input:CommonFilter):
    return DynamicService.GetChartValue(input)

@Dynamic.post('/GetcommonDyChartDetail')
def GetcommonDyChartDetail(input:CommonFilter):
    return DynamicService.GetChartDetailValue(input)

@Dynamic.post('/GetcommonChartDetail')
def GetcommonChartDetail(input:VendorPageDetDataInput):
    return DynamicService.GetChartDetail(input)

@Dynamic.post('/GetVendorDetail')
def GetVendorDetail(VendorID :int=0):
    return DynamicService.GetVendorDetailByID(VendorID)

@Dynamic.post('/VendorAddEdit')
def VendorAddEdit(input :VendorAddEditInput):
    return DynamicService.VendorAddEdit(input)

@Dynamic.post('/VendorChartAddEdit')
def VendorChartAddEdit(input :VendorChartInput):
    return DynamicService.VendorChartAddEdit(input)

# @Dynamic.post('/VendorPageAddEdit')
# def VendorPageAddEdit(input :VendorChartInput):
#     return DynamicService.VendorChartAddEdit(input)

@Dynamic.post('/VendorPageData')
def VendorPageData(input:VendorPageDetDataInput):
    return DynamicService.VendorPageDataServiec(input)

@Dynamic.post('/VendorchartDetailScreen')
def VendorchartDetailScreen(input:VendorchartDetailScreenInput):
    return DynamicService.VendorchartDetailScreen(input)

@Dynamic.post('/CommanVendorchartDetail')
def CommanVendorchartDetail(input:VendorchartDetailInput):
    return DynamicService.GetChartDetailValue(input)