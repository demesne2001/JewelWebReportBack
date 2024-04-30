import os
import base64
import cv2 
from fastapi import APIRouter,Body,Depends
from Entity.DTO.WsInput import UploadFile,DeleteFile,GetPDfUsingImageInput,Login
from Service import CommanService,AuthenticationService,RijndaelEncryptor
Common=APIRouter()

BaseDirectory="Utility/Image/"

@Common.post('/uploadImage')
async def Create_upload(input:UploadFile):   
    data_split = input.Base64.split('base64,')    
    if(len(data_split)>1):
        encoded_data = data_split[1] 
    elif(len(data_split)==1):
        encoded_data = data_split[0]
    else:
        encoded_data=input.Base64 

    data = base64.b64decode(encoded_data)
    with open(F"{BaseDirectory}{input.LoginID}.{input.Extension}","wb") as f:
        f.write(data)
    return {'filename':F"{input.LoginID}.{input.Extension}"}

@Common.post('/DeleteFile')
async def DeleteFileByName(input:DeleteFile): 
      if(os.path.exists(BaseDirectory+input.FileName)): 
        os.remove(BaseDirectory+input.FileName)
        return {"Mesage":f"Delete File {input.FileName}"}
    
@Common.post('/GetPDFUsingImage')
async def GetPDFUsingImage(input:GetPDfUsingImageInput): 
       result= CommanService.ImageToDirectPDf(input)
       return result.__dict__
   
