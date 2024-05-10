from fastapi import APIRouter,Body,Depends
from Service import ScheduleService
from Entity.DTO.WsInput import SchedulechartInput,ScheduleDetailInput,ScheduleAllDetailInput,SchedulePartyDetailInput
Schedule=APIRouter()

@Schedule.post('/GetcommonChart')
def GetcommonChart(input:SchedulechartInput):
    return ScheduleService.GetChartWise(input)

@Schedule.post('/GetcommonCard')
def GetcommonChart(input:SchedulechartInput):
    return ScheduleService.GetCardWise(input)

@Schedule.post('/GetChartDetailWise')
def GetcommonChart(input:ScheduleDetailInput):
    return ScheduleService.GetChartDetailWise(input)

@Schedule.post('/GetChartAllOverDetails')
def GetChartAllOverDetails(input:ScheduleAllDetailInput):
    return ScheduleService.GetChartAllOverDetails(input)

@Schedule.post('/GetChartPartyDetails')
def GetChartPartyDetails(input:SchedulePartyDetailInput):
    return ScheduleService.GetChartPartyOverDetails(input)