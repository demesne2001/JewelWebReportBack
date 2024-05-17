from pydantic import BaseModel,Field


class UploadFile(BaseModel):
    Base64:str
    Extension:str
    LoginID:str    
class DeleteFile(BaseModel):
    FileName:str
    
class GetPDfUsingImageInput(BaseModel):
    ImageLst:list
    FileName:str
    
class ChartWiseImageInput(BaseModel):
    strBranch :str | None= Field(default="")
    strState :str | None= Field(default="")
    strCity :str | None= Field(default="")
    strRegionID :str | None= Field(default="")
    strSubItem :str | None= Field(default="")
    strItem :str | None= Field(default="")
    strItemGroup :str | None= Field(default="")
    strItemSubitem :str | None= Field(default="")
    strDesignCodeID :str | None= Field(default="")
    strSalesParty :str | None= Field(default="")
    strSaleman :str | None= Field(default="")
    strProduct :str | None= Field(default="")
    strDesignCatalog :str | None= Field(default="")
    strSaleAging :str | None= Field(default="")
    strMonth :str | None= Field(default="")
    strFinYear :str | None= Field(default="")
    PageNo: int | None= Field(default=1)
    PageSize: int | None= Field(default=20)
    
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
    strDesignCodeID:str| None= Field(default="")
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
    SortBy:str|None= Field(default="wt")
    SortByLabel:str|None= Field(default="")
    Search:str| None= Field(default="")
    Grouping:str| None= Field(default="")
    strMonth:str| None= Field(default="")
    strFinYear:str| None= Field(default="")
    Unity:str| None=Field(default="G")
   
   
   
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
    
class Login(BaseModel):
    LoginID:str
    PassWord:str
    
class SchedulechartInput(BaseModel):
    FromDate:str
    Todate:str
    strBranchID:str
    Unit:str
    Mode:int
    
class ScheduleDetailInput(BaseModel):
    TravellingTeamID:int
    Mode:int 

class ScheduleAllDetailInput(BaseModel):
    TravellingTeamID:int | None= Field(default=0)
    
class SchedulePartyDetailInput(BaseModel):
    ScheduleID:int
    Mode:int 
    
class CommonFilter(BaseModel):
    strBranchID:str | None= Field(default="")
    strCompanyID:str | None= Field(default="")
    strStateID:str| None= Field(default="")
    strCityID:str| None= Field(default="")
    strItemID:str| None= Field(default="")
    strSubItemID:str| None= Field(default="")
    strItemGroupID:str| None= Field(default="")
    strRegionID:str| None= Field(default="")
    strItemSubitemID:str| None= Field(default="")
    strPurchasePartyID:str| None= Field(default="")
    strSalesPartyID:str| None= Field(default="")
    strSalemanID:str| None= Field(default="")
    strProductID:str| None= Field(default="")
    strDesignCodeID:str| None= Field(default="")
    strDesignCatalogueID:str| None= Field(default="")
    strSaleAging:str| None= Field(default="")
    strModeofSale:str| None= Field(default="")
    strTeamModeofSale:str| None= Field(default="")
    FromDate:str| None= Field(default="")
    ToDate:str| None= Field(default="")
    strMetalType:str| None= Field(default="")
    strDayBookID:str| None= Field(default="")
    strMonth:str| None= Field(default="")
    strFinYear:str| None= Field(default="")
    Unity:str| None=Field(default="G")
    DychartID:int| None=Field(default=0)
    
    
class VendorAddEditInput(BaseModel):
    VendorID:int| None=Field(default=0)
    VendorName:str
    VendorStaticIP:str
    VendorDBName:str
    PageName:str
    
class VendorChartAddEdit(BaseModel):
    DychartID:int| None=Field(default=0)
    VendorID:int
    RowNo:int
    RowCHartcount:int
    RSrno:int
    ChartLabel:str
    XLabel:str
    Ylabel:str
    SpName:str
    Chartoption:str
    
class VendorChartInput(BaseModel):
    lstChartDetail : list[VendorChartAddEdit]
    
class VendorPageDetDataInput(BaseModel):
    VendorID:int | None=Field(default=0)
    PageID:int | None=Field(default=0)