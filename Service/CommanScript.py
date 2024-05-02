from datetime import datetime,date
from Entity.DTO import WsResponse
import os
import json
Count=1

FilePath="Utility/Logfile/"

def ErrorLog(MethodName:str,input:str,SpName:str,Error:str):    
    result=WsResponse.ErrorLog()   
    if(MethodName ==""):
        MethodName=str(datetime.now())
    try:
        if(os.path.exists(FilePath+str(date.today()))):
            pass
        else:
            os.makedirs(FilePath+str(date.today()))
        
        print(MethodName,'log') 
        print(str(datetime.now()))
        result.ErrorMethod=str(MethodName).strip()
        result.ErrorDate=str(datetime.now())
        result.ErrorException=str(Error)
        result.ErrorParam=str(input)
        result.ErrorSpNAme=str(SpName)
        FileName=f"{FilePath+str(date.today())}/ErrorLog_{MethodName}.txt"
        jsonResult=json.dumps(result.__dict__)
        ErrorFile=open(FileName,"w")
        
        ErrorFile.write(jsonResult)
        ErrorFile.close()
        
    except Exception as E:
        print(str(E))
    
        
        
    
    