from pydantic import BaseModel,Field


    

class CardandChartInput(BaseModel):
    strBranch:str
    strState:str
    strCity:str
    strItem:str
    strSubItem:str
    strItemGroup:str
    strItemSubitem:str
    strPurchaseParty:str
    strSalesParty:str
    strSaleman:str
    strProduct:str
    strDesignCatalogue:str
    strSaleAging:str
    strModeofSale:str
    strTeamModeofSale:str
    FromDate:str
    ToDate:str
    strMetalType:str
    strDayBook:str
    PageNo:int
    PageSize:int
    Search:str
    Grouping:str
   