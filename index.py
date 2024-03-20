import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from decouple import config
from Controller import DashboardCard,DashboardChart,DashboardFilter
app=FastAPI()


app.include_router(DashboardFilter.Filter,prefix='/Filter')
app.include_router(DashboardCard.Card,prefix='/Card')
app.include_router(DashboardChart.Chart,prefix='/Chart')
origins=['*']
app.add_middleware(CORSMiddleware,allow_origins=origins,allow_credentials=True,allow_methods=['*'],allow_headers=['*'],)

@app.post("/Demo")
def Demo():
    return{"msg":"Welcome to Fast"}