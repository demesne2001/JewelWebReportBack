from fastapi import APIRouter,Body,Depends
from Service import DashboardFilterService
from Entity.DTO.WsInput import CardandChartInput,GetByID,AddEditFilterGrid
Filter=APIRouter()

@Filter.post('/GetBranch')
def GetBranch(input:CardandChartInput):
    return DashboardFilterService.GetBranch(input)

@Filter.post('/GetState')
def GetState(input:CardandChartInput):
    return DashboardFilterService.GetState(input)

@Filter.post('/GetCity')
def GetCity(input:CardandChartInput):
    return DashboardFilterService.GetCity(input)


@Filter.post('/GetRegion')
def GetRegion(input:CardandChartInput):
    return DashboardFilterService.GetRegion(input)


@Filter.post('/GetItem')
def GetItem(input:CardandChartInput):
    return DashboardFilterService.GetItem(input)

@Filter.post('/GetSubItem')
def GetSubItem(input:CardandChartInput):
    return DashboardFilterService.GetSubItem(input)

@Filter.post('/GetItemGroup')
def GetItemGroup(input:CardandChartInput):
    return DashboardFilterService.GetItemGroup(input)

@Filter.post('/GetItemWithSubitem')
def GetItemWithSubitem(input:CardandChartInput):
    return DashboardFilterService.GetItemWithSubitem(input)

@Filter.post('/GetPurchaseParty')
def GetPurchaseParty(input:CardandChartInput):
    return DashboardFilterService.GetPurchaseParty(input)


@Filter.post('/GetSalesParty')
def GetSalesParty(input:CardandChartInput):
    return DashboardFilterService.GetSalesParty(input)


@Filter.post('/GetSaleman')
def GetSaleman(input:CardandChartInput):
    return DashboardFilterService.GetSaleman(input)

@Filter.post('/GetProduct')
def GetProduct(input:CardandChartInput):
    return DashboardFilterService.GetProduct(input)

@Filter.post('/GetDesignCatalogue')
def GetDesignCatalogue(input:CardandChartInput):
    return DashboardFilterService.GetDesignCatalogue(input)

@Filter.post('/GetModeSale')
def GetModeSale(input:CardandChartInput):
    return DashboardFilterService.GetModeSale(input)


@Filter.post('/GetTeamModeofSale')
def GetTeamModeofSale(input:CardandChartInput):
    return DashboardFilterService.GetTeamModeofSale(input)


@Filter.post('/GetDayBook')
def GetDayBook(input:CardandChartInput):
    return DashboardFilterService.GetDayBook(input)

@Filter.post('/GetMetalType')
def GetMetalType(input:CardandChartInput):
    return DashboardFilterService.GetMetalType(input)

@Filter.post('/GetSalesAging')
def GetSalesAging(input:CardandChartInput):
    return DashboardFilterService.GetSalesAging(input)

@Filter.post('/GetFilterGridByID')
def GetFilterGridByID(input:GetByID):
    return DashboardFilterService.GetFilterGridByID(input)

@Filter.post('/FilterGridAddEdit')
def FilterGridAddEdit(input:AddEditFilterGrid):
    return DashboardFilterService.FilterGridAddEdit(input)

@Filter.post('/GetMonth')
def GetMonth(input:CardandChartInput):
    return DashboardFilterService.GetMonth(input)

@Filter.post('/GetDefaultScreenData')
def GetDefaultScreenData():
    return DashboardFilterService.GetDefaultScreenData()