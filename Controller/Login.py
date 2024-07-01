import os
from fastapi import APIRouter,Body,Depends,HTTPException
from Entity.DTO.WsInput import UploadFile,DeleteFile,GetPDfUsingImageInput,Login,UserAddEditInput,GetUserInput
from Service import AuthenticationService
LoginController=APIRouter()

@LoginController.post('/login')
async def login(input:Login): 
       result=AuthenticationService.Authentication(input)
       return result

@LoginController.post("/encrypt")
async def encrypt_value(value: str):
    try:
        encrypted_value = AuthenticationService.encryptPass(value)
        return {"encrypted_value": encrypted_value}
    except HTTPException as e:
        raise e
    
    
@LoginController.post("/AddEditUser")
async def AddEditUser(input: UserAddEditInput):
    try:        
        return AuthenticationService.AddEditUser(input)
    except HTTPException as e:
        raise e
@LoginController.post("/GetUserData")
async def GetUserData(input: GetUserInput):
    try:        
        return AuthenticationService.GetUserData(input)
    except HTTPException as e:
        raise e
    
    
@LoginController.post("/Decrpt")
async def Decrpt(input: UserAddEditInput):
    try:
        encrypted_value = AuthenticationService.decryptPass(input.Password)
        return {"encrypted_value": encrypted_value}
    except HTTPException as e:
        raise e