from fastapi import APIRouter,Body,Depends
from Service import ScheduleService
from Entity.DTO.WsInput import SchedulechartInput
Schedule=APIRouter()

@Schedule.post('/GetcommonChart')
def GetcommonChart(input:SchedulechartInput):
    return ScheduleService.GetChartWise(input)

@Schedule.post('/GetcommonCard')
def GetcommonChart(input:SchedulechartInput):
    return ScheduleService.GetCardWise(input)