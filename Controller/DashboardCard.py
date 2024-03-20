from fastapi import APIRouter,Body,Depends
from Service import DashboardCardService
from Entity.DTO.WsInput import CardandChartInput
Card=APIRouter()

@Card.post('/GetSalesEfficiencyCard')
def GetSalesEfficiencyCard(input:CardandChartInput):
    return DashboardCardService.GetSalesEfficiencyCard(input)

@Card.post('/GetReturnTrendCard')
def GetReturnTrendCard(input:CardandChartInput):
    return DashboardCardService.GetReturnTrendCard(input) 
 
@Card.post('/GetSalesWeightCard')   
def GetSalesWeightCard(input:CardandChartInput):
    return DashboardCardService.GetSalesWeightCard(input)
 
@Card.post('/GetCollectionCard')
def GetCollectionCard(input:CardandChartInput):
    return DashboardCardService.GetCollectionCard(input)
 
@Card.post('/GetStockAnalysisCard')
def GetStockAnalysisCard(input:CardandChartInput):
    return DashboardCardService.GetStockAnalysisCard(input)
 
