import uvicorn
from fastapi import FastAPI,Depends
from fastapi.middleware.cors import CORSMiddleware
from decouple import config
from Controller import DashboardCard,DashboardChart,DashboardFilter,CommonController,Login,ScheduleController
import os
from fastapi.staticfiles import StaticFiles
from Service.jwtBearer import jwtBearer
app=FastAPI()


app.include_router(DashboardFilter.Filter,prefix='/Filter')
app.include_router(DashboardCard.Card,prefix='/Card')
app.include_router(DashboardChart.Chart,prefix='/Chart')
app.include_router(CommonController.Common,prefix='/Common')
app.include_router(Login.LoginController,prefix='/Login')
app.include_router(ScheduleController.Schedule,prefix='/Schedule')
origins=['*']
app.add_middleware(CORSMiddleware,allow_origins=origins,allow_credentials=True,allow_methods=['*'],allow_headers=['*'],)

FilePath="Utility/Logfile"
path="Utility/Image"
PDFPath="Utility/PDF"

if(os.path.exists(FilePath)):
    pass
else:
    os.makedirs(FilePath)

if(os.path.exists(path)):
    pass
else:
    os.makedirs(path)
    
if(os.path.exists(PDFPath)):
    pass
else:
    os.makedirs(PDFPath)


    
app.mount("/image", StaticFiles(directory="Utility/Image"), name="image")
app.mount("/PDF", StaticFiles(directory="Utility/PDF"), name="PDF")
app.mount("/Logfile", StaticFiles(directory="Utility/Logfile"), name="Logfile")
    
@app.post("/Demo")
def Demo():
    return{"msg":"Welcome to Fast"}