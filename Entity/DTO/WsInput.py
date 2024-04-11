from pydantic import BaseModel,Field


    

class CardandChartInput(BaseModel):
    strBranch:str | None= Field(default="")
    strCompanyID:str | None= Field(default="")
    strState:str| None= Field(default="")
    strCity:str| None= Field(default="")
    strItem:str| None= Field(default="")
    strSubItem:str| None= Field(default="")
    strItemGroup:str| None= Field(default="")
    strRegionID:str| None= Field(default="")
    strItemSubitem:str| None= Field(default="")
    strPurchaseParty:str| None= Field(default="")
    strSalesParty:str| None= Field(default="")
    strSaleman:str| None= Field(default="")
    strProduct:str| None= Field(default="")
    strDesignCatalogue:str| None= Field(default="")
    strSaleAging:str| None= Field(default="")
    strModeofSale:str| None= Field(default="")
    strTeamModeofSale:str| None= Field(default="")
    FromDate:str| None= Field(default="")
    ToDate:str| None= Field(default="")
    strMetalType:str| None= Field(default="")
    strDayBook:str| None= Field(default="")
    PageNo:int| None= Field(default=1)
    PageSize:int| None= Field(default=10)
    Search:str| None= Field(default="")
    Grouping:str| None= Field(default="")
   
   
   
class GetByID(BaseModel):
    ID:int
    vendorID:int | None= Field(default=1)
    UserID:int| None= Field(default=1)

class AddEditFilterGrid(BaseModel):
    FilterGridID:int
    FilterGrid:str
    FilterID:int
    vendorID:int | None= Field(default=1)
    UserID:int| None= Field(default=1)
    
class AddEditChartOption(BaseModel):
    ChartOptionID:int
    ChartOption:str
    ChartID:int
    vendorID:int | None= Field(default=1)
    UserID:int| None= Field(default=1)
    
    
class AddEditChartGroup(BaseModel):
    ChartGroupID:int
    ChartGroup:str
    ChartID:int
    vendorID:int | None= Field(default=1)
    UserID:int| None= Field(default=1)