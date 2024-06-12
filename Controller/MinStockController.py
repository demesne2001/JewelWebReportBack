from fastapi import APIRouter,Body,Depends
from Service import MinStockService
from Entity.DTO.WsInput import StockToSalesInput,MinSubitemDeatil
# from Entity.DTO.WsInput import SchedulechartInput,ScheduleDetailInput,ScheduleAllDetailInput,SchedulePartyDetailInput
MinStock=APIRouter()



@MinStock.post('/GetMinStockChart')
def GetMinStockChart(input:StockToSalesInput):
    return MinStockService.GetMinStockChart(input)

@MinStock.post('/GetMinStockChartDeatil')
def GetMinStockChartDeatil(input:MinSubitemDeatil):
    return MinStockService.GetMinStockDeatilChart(input)