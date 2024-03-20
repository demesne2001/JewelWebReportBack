from decouple import config
import pyodbc 
from DAL import DBConfig
from enum import Enum
from Entity.DTO.WsInput import CardandChartInput
server=config('dbconnection')
database=config("DBName")
username=config("DBUser")
password=config("DBPass")


print(server)
version='18'
WRconnection = (
    f'DRIVER=SQL Server;SERVER={server};DATABASE={database};UID={username};PWD={password};')

class Connection(Enum):
    LiveConnection=(f'DRIVER=ODBC Driver 18 for SQL Server;SERVER={server};DATABASE={database};UID={username};PWD={password};TrustServerCertificate=yes;Encrypt=no;Connection Timeout=30;')
    Connection=(f'DRIVER=SQL Server;SERVER={server};DATABASE={database};UID={username};PWD={password};')
    
# WRconnection = (
#     f'DRIVER=ODBC Driver 18 for SQL Server;SERVER={server};DATABASE={database};UID={username};PWD={password};TrustServerCertificate=yes;Encrypt=no;Connection Timeout=30;')


def Commandparam(input):
    # key=input.keys()
    # print(key)
    # for item in input:
    #     print('Keys',item.keys())
    # for i in input.kyes():
    #     print(i)
    key=list[input]
    print('keys')
    print(input)
    

def ExecuteDataReader(param,spname,MethodNname):
    key_value_pairs=[]
    drivers = [item for item in pyodbc.drivers()]    
    connection=pyodbc.connect(DBConfig.WRconnection)
    try:
        cursor=connection.cursor()        
        cursor.execute(f"EXEC {spname} {param}")
        columns = [column[0] for column in cursor.description]
        rows = cursor.fetchall()        
        for row in rows:
            key_value_pairs.append(dict(zip(columns, row)))
        cursor.close()
        connection.close()
    except Exception as e:
        print(MethodNname + 'Error :- ',e)
        print('SQL Query',f"EXEC {spname} {param}")
        print('driver',drivers)
        connection.close()
    return key_value_pairs

def ExecuteDataReader(param,spname,MethodNname,Result2):
    key_value_pairs=[]
    drivers = [item for item in pyodbc.drivers()]    
    connection=pyodbc.connect(DBConfig.WRconnection)
    try:
        cursor=connection.cursor()        
        cursor.execute(f"EXEC {spname} {param}")
        columns = [column[0] for column in cursor.description]
        rows = cursor.fetchall()        
        for row in rows:
            key_value_pairs.append(dict(zip(columns, row)))
            
        while True:
            Result2=cursor.fetchall()
            if cursor.nextset()==False:
                break
        cursor.close()
        connection.close()
    except Exception as e:
        print(MethodNname + 'Error :- ',e)
        print('SQL Query',f"EXEC {spname} {param}")
        print('driver',drivers)
        connection.close()
    return key_value_pairs

def ExecuteDataReader(param,spname,MethodNname,Connections):
    key_value_pairs=[]
    drivers = [item for item in pyodbc.drivers()]    
    connection=pyodbc.connect(DBConfig.WRconnection)
    try:
        cursor=connection.cursor()        
        cursor.execute(f"EXEC {spname} {param}")
        columns = [column[0] for column in cursor.description]
        rows = cursor.fetchall()        
        for row in rows:
            key_value_pairs.append(dict(zip(columns, row)))
        cursor.close()
        connection.close()
    except Exception as e:
        print(MethodNname + 'Error :- ',e)
        print('SQL Query',f"EXEC {spname} {param}")
        print('driver',drivers)
        connection.close()
    return key_value_pairs

def CommonParam(input:CardandChartInput):
    param=""
    if(input.strBranch!=''):
        param +=f" @strBranch='{input.strBranch}',"
    if(input.strTeamModeofSale!=''):
        param +=f" @strTeamModeofSale='{input.strTeamModeofSale}',"  
    if(input.strCity!=''):
        param +=f" @strCity='{input.strCity}',"
    if(input.strDayBook!=''):
        param +=f" @strDayBook='{input.strDayBook}',"
    if(input.strDesignCatalogue!=''):
        param +=f" @strDesignCatalogue='{input.strDesignCatalogue}',"
    if(input.FromDate!=''):
        param +=f" @FromDate='{input.FromDate}',"
    if(input.ToDate!=''):
        param +=f" @ToDate='{input.ToDate}',"
    if(input.strItem!=''):
        param +=f" @strItem='{input.strItem}',"
    if(input.strItemGroup!=''):
        param +=f" @strItemGroup='{input.strItemGroup}',"
    if(input.strItemSubitem!=''):
        param +=f" @strItemSubitem='{input.strItemSubitem}',"
    if(input.strMetalType!=''):
        param +=f" @strMetalType='{input.strMetalType}',"
    if(input.strModeofSale!=''):
        param +=f" @strModeofSale='{input.strModeofSale}',"
    if(input.strPurchaseParty!=''):
        param +=f" @strPurchaseParty='{input.strPurchaseParty}',"
    if(input.strProduct!=''):
        param +=f" @strProduct='{input.strProduct}',"
    if(input.strSaleman!=''):
        param +=f" @strSaleman='{input.strSaleman}',"
    if(input.strSaleAging!=''):
        param +=f" @strSaleAging='{input.strSaleAging}',"
    if(input.strSalesParty!=''):
        param +=f" @strSalesParty='{input.strSalesParty}',"        
    if(input.strState!=''):
        param +=f" @strState='{input.strState}',"
    else:
        param = param[:len(param)-1]
    
    return param