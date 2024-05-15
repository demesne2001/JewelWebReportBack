from fastapi import APIRouter,Body,Depends
from Service import DynamicService
from Entity.DTO.WsInput import CommonFilter,VendorAddEditInput,VendorChartInput
from Entity.DTO.WsResponse import DynamicResult


Dynamic=APIRouter()

@Dynamic.post('/GetcommonChart')
def GetcommonChart(input:CommonFilter):
    return DynamicService.GetChartValue(input)

@Dynamic.post('/GetcommonChartDetail')
def GetcommonChartDetail(VendorID :int=0):
    return DynamicService.GetChartDetail(VendorID)

@Dynamic.post('/GetVendorDetail')
def GetVendorDetail(VendorID :int=0):
    return DynamicService.GetVendorDetailByID(VendorID)

@Dynamic.post('/VendorAddEdit')
def VendorAddEdit(input :VendorAddEditInput):
    return DynamicService.VendorAddEdit(input)

@Dynamic.post('/VendorChartAddEdit')
def VendorChartAddEdit(input :VendorChartInput):
    return DynamicService.VendorChartAddEdit(input)