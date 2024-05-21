import os
from fastapi import APIRouter,Body,Depends,HTTPException
from Entity.DTO.WsInput import UploadFile,DeleteFile,GetPDfUsingImageInput,Login,UserAddEditInput
from Service import AuthenticationService
LoginController=APIRouter()

@LoginController.post('/login')
async def login(input:Login): 
       result=AuthenticationService.Authentication(input)
       return result

@LoginController.post("/encrypt")
async def encrypt_value(value: str):
    try:
        encrypted_value = AuthenticationService.encrypt(value.encode())
        return {"encrypted_value": encrypted_value}
    except HTTPException as e:
        raise e
    
    
@LoginController.post("/AddEditUser")
async def AddEditUser(input: UserAddEditInput):
    try:        
        return AuthenticationService.AddEditUser(input)
    except HTTPException as e:
        raise e
    
    
@LoginController.post("/Decrpt")
async def Decrpt(input: UserAddEditInput):
    try:
        encrypted_value = AuthenticationService.decryptPass(input.Password)
        return {"encrypted_value": encrypted_value}
    except HTTPException as e:
        raise e