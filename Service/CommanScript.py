from datetime import datetime,date
from Entity.DTO import WsResponse
import os
Count=1

FilePath="Utility/Logfile/"

def ErrorLog(MethodName,input,SpName,Error):
    try:
        if(os.path.exists(FilePath+str(date.today()))):
            pass
        else:
            os.makedirs(FilePath+str(date.today()))
        result=WsResponse.ErrorLog()
        result.ErrorDate=str(datetime.now())
        result.ErrorMethod=str(MethodName)
        result.ErrorException=str(Error)
        result.ErrorParam=str(input)
        result.ErrorSpNAme=str(SpName)
        FileName=f"{FilePath+str(date.today())}/ErrorLog({Count}).txt"
        ErrorFile=open(FileName,"w")
        ErrorFile.write(str(result))
        ErrorFile.close()
        Count+=1
    except Exception as E:
        print(str(E))
        
    
    