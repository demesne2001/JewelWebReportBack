from fastapi import APIRouter,Body,Depends
from Service import StockToSalesService
from Entity.DTO.WsInput import StockToSalesInput
StockToSales=APIRouter()


@StockToSales.post('/GetStockToSalesChart')
def GetStockToSalesChart(input:StockToSalesInput):
    return StockToSalesService.GetStockToSalesChart(input)