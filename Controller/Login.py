import os
from fastapi import APIRouter,Body,Depends
from Entity.DTO.WsInput import UploadFile,DeleteFile,GetPDfUsingImageInput,Login
from Service import AuthenticationService
LoginController=APIRouter()

@LoginController.post('/login')
async def login(input:Login): 
       result=AuthenticationService.Authentication(input)
       return result