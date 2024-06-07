from fastapi import APIRouter,Body,Depends
from Service import MinStockService
# from Entity.DTO.WsInput import SchedulechartInput,ScheduleDetailInput,ScheduleAllDetailInput,SchedulePartyDetailInput
MinStock=APIRouter()