from fastapi import APIRouter,Body,Depends
from Service import DashboardChartService
from Entity.DTO.WsInput import CardandChartInput,GetByID,AddEditChartOption
Chart=APIRouter()

@Chart.post('/GetBranchWise')
def GetBranchWise(input:CardandChartInput):
    return DashboardChartService.GetBranchWise(input)
 

@Chart.post('/GetStateWise')
def GetStateWise(input:CardandChartInput):
    return DashboardChartService.GetStateWise(input)
 

@Chart.post('/GetCityWise')
def GetCityWise(input:CardandChartInput):
    return DashboardChartService.GetCityWise(input)
 
 
@Chart.post('/GetRegionWise')
def GetRegionWise(input:CardandChartInput):
    return DashboardChartService.GetRegionWise(input)
 
@Chart.post('/GetItemWise')
def GetItemWise(input:CardandChartInput):
    return DashboardChartService.GetItemWise(input)
 
@Chart.post('/GetSubItemWise')
def GetSubItemWise(input:CardandChartInput):
    return DashboardChartService.GetSubItemWise(input)
 
@Chart.post('/GetItemGroupWise')
def GetItemGroupWise(input:CardandChartInput):
    return DashboardChartService.GetItemGroupWise(input)
 

@Chart.post('/GetItemWithSubItemWise')
def GetItemWithSubItemWise(input:CardandChartInput):
    return DashboardChartService.GetItemWithSubItemWise(input)
 

@Chart.post('/GetPurchasePartywise')
def GetPurchasePartywise(input:CardandChartInput):
    return DashboardChartService.GetPurchasePartywise(input)
 
 
@Chart.post('/GetSalesPartyWise')
def GetSalesPartyWise(input:CardandChartInput):
    return DashboardChartService.GetSalesPartyWise(input)
 
@Chart.post('/GetProductWise')
def GetProductWise(input:CardandChartInput):
    return DashboardChartService.GetProductWise(input)
 
@Chart.post('/GetDesignCatalogueWise')
def GetDesignCatalogueWise(input:CardandChartInput):
    return DashboardChartService.GetDesignCatalogueWise(input)
 
@Chart.post('/GetMonthWise')
def GetMonthWise(input:CardandChartInput):
    return DashboardChartService.GetMonthWise(input)
 

@Chart.post('/GetYearWise')
def GetYearWise(input:CardandChartInput):
    return DashboardChartService.GetYearWise(input)
 

@Chart.post('/GetSalesAgingWise')
def GetSalesAgingWise(input:CardandChartInput):
    return DashboardChartService.GetSalesAgingWise(input)
 
 
@Chart.post('/GetModeOfSalesWise')
def GetModeOfSalesWise(input:CardandChartInput):
    return DashboardChartService.GetModeOfSalesWise(input)
 
@Chart.post('/GetTeamAndModeOFSalesWise')
def GetTeamAndModeOFSalesWise(input:CardandChartInput):
    return DashboardChartService.GetTeamAndModeOFSalesWise(input)
 
@Chart.post('/GetSalesmanWise')
def GetSalesmanWise(input:CardandChartInput):
    return DashboardChartService.GetSalesmanWise(input)

@Chart.post('/GetCommanChart')
def GetCommanChart(input:CardandChartInput):
    return DashboardChartService.GetCommanChart(input)

@Chart.post('/GetDetailCommanChart')
def GetDetailCommanChart(input:CardandChartInput):
    return DashboardChartService.GetDetailCommanChart(input)

@Chart.post('/GetChartOptionByID')
def GetChartOptionByID(input:GetByID):
    return DashboardChartService.GetChartOptionByID(input)

@Chart.post('/ChartOptionAddEdit')
def ChartOptionAddEdit(input:AddEditChartOption):
    return DashboardChartService.ChartOptionAddEdit(input)

