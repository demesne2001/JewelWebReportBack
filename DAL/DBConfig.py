from decouple import config
import pyodbc 
from DAL import DBConfig
from enum import Enum
from Service import CommanScript
from Entity.DTO.WsInput import CardandChartInput
from Service import jwtBearer
server=config('dbconnection')
database=config("DBName")
username=config("DBUser")
password=config("DBPass")

server2=config('dbconnection2')
database2=config("DBName2")
username2=config("DBUser2")
password2=config("DBPass2")



print(server2)
version='18'
WRconnection = (
    f'DRIVER=SQL Server;SERVER={server2};DATABASE={database2};UID={username2};PWD={password2};')

# WRconnection=(f'DRIVER=ODBC Driver 18 for SQL Server;SERVER={server};DATABASE={database};UID={username};PWD={password};TrustServerCertificate=yes;Encrypt=no;Connection Timeout=30;')
class Connection(Enum):
    LiveConnection=f'DRIVER=ODBC Driver 18 for SQL Server;SERVER={server2};DATABASE={database2};UID={username2};PWD={password2};TrustServerCertificate=yes;Encrypt=no;Connection Timeout=30;'
    # LiveConnection=f'DRIVER=ODBC Driver 17 for SQL Server;SERVER={server2};DATABASE={database2};UID={username2};PWD={password2};'
    Connection=f'DRIVER=SQL Server;SERVER={server2};DATABASE={database2};UID={username2};PWD={password2};'
    # CDBConnection=f'DRIVER=ODBC Driver 18 for SQL Server;SERVER={UserDB};DATABASE={userdbname};UID={username2};PWD={password2};TrustServerCertificate=yes;Encrypt=no;Connection Timeout=30;'
    
# WRconnection = (
#     f'DRIVER=ODBC Driver 18 for SQL Server;SERVER={server};DATABASE={database};UID={username};PWD={password};TrustServerCertificate=yes;Encrypt=no;Connection Timeout=30;')


def Commandparam(input):   
    key=list[input]
    print('keys')
    print(input)
     # key=input.keys()
    # print(key)
    # for item in input:
    #     print('Keys',item.keys())
    # for i in input.kyes():
    #     print(i)
def spParam(input):
    newParam=""    
    result=""
    try:
        for i in input:
            print(i)
            if(type(i[1]) is int):
                if(i[1] > 0):              
                    newParam+=f"@{i[0]}={i[1]},"                    
            elif(type(i[1]) is str):
                if(i[1]!=""):
                    newParam+=f"@{i[0]}='{i[1]}',"                    
            elif(type(i[1]) is bool):
                if(i[1]==False or i[1]==True):
                    newParam+=f"@{i[0]}={i[1]},"                    
        # print('result=======',newParam)
        result=','.join([s for s in newParam.split(',') if s])
    except Exception as e:
        CommanScript.ErrorLog("spParam",str(input),"spParam",e)
        print(e)    
    return result

def ExecuteNonQuery(input,spname,MethodNname):    
    param=""
    param=spParam(input)  
    print(param)  
    ID=0
    drivers = [item for item in pyodbc.drivers()]
    print(drivers)    
    wconnection=pyodbc.connect(Connection.LiveConnection.value)
    # wconnection=pyodbc.connect(Connection.Connection.value)
    
    try:
        cursor=wconnection.cursor()             
        cursor.execute(f"EXEC {spname} {param}")        
        rows = cursor.fetchone() 
        print(rows)
        ID=rows[0]        
        cursor.commit()
    except Exception as e:
        CommanScript.ErrorLog("ExecuteNonQuery",input,spname,e)
        print(MethodNname + 'Error :- ',e)
        print('SQL Query',f"EXEC {spname} {param}")
        print('driver',drivers)
        cursor.rollback()   
    finally:
        cursor.close()
        wconnection.close()
    return ID

def ExecuteDataReader(param,spname,MethodNname):    
    key_value_pairs=[]
    drivers = [item for item in pyodbc.drivers()]  
    connection=pyodbc.connect(Connection.LiveConnection.value)
    # connection=pyodbc.connect(Connection.Connection.value)
    print(drivers)
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
        CommanScript.ErrorLog("ExecuteDataReader",param,spname,e)
        print(MethodNname + 'Error :- ',e)
        print('SQL Query',f"EXEC {spname} {param}")
        print('driver',drivers)
        connection.close()
    return key_value_pairs

def CDBExecuteDataReader(param,spname,MethodNname):    
    key_value_pairs=[]
    drivers = [item for item in pyodbc.drivers()]  
    if(jwtBearer.CDBConnectionstring ==""):
        connection=pyodbc.connect(Connection.LiveConnection.value)
        # connection=pyodbc.connect(Connection.Connection.value)
    else:             
        connection=pyodbc.connect(f'DRIVER=ODBC Driver 18 for SQL Server;SERVER={jwtBearer.CDBConnectionstring};DATABASE={jwtBearer.CDbName};UID={username2};PWD={password2};TrustServerCertificate=yes;Encrypt=no;Connection Timeout=30;')      
        
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
        # CommanScript.ErrorLog(MethodNname,param,spname,e)
        print('Error :- ',e)
        print('SQL Query',f"EXEC {spname} {param}")
        print('driver',drivers)
        connection.close()
    return key_value_pairs

def CDBExecuteNonQuery(input,spname,MethodNname):    
    param=""
    param=spParam(input)  
    print(param)  
    ID=0
    drivers = [item for item in pyodbc.drivers()]    
   
    if(jwtBearer.CDBConnectionstring ==""):
        wconnection=pyodbc.connect(Connection.LiveConnection.value)
    else:       
        wconnection=pyodbc.connect(f'DRIVER=ODBC Driver 18 for SQL Server;SERVER={jwtBearer.CDBConnectionstring};DATABASE={jwtBearer.CDbName};UID={username2};PWD={password2};TrustServerCertificate=yes;Encrypt=no;Connection Timeout=30;')      
    try:
        cursor=wconnection.cursor()             
        cursor.execute(f"EXEC {spname} {param}")        
        rows = cursor.fetchone() 
        print(rows)
        ID=rows[0]        
        cursor.commit()
    except Exception as e:
        # CommanScript.ErrorLog('ExecuteNonQuery',input,spname,e)
        print('Error :- ',e)
        print('SQL Query',f"EXEC {spname} {param}")
        print('driver',drivers)
        cursor.rollback()   
    finally:
        cursor.close()
        wconnection.close()
    return ID

def GetDynamicSpName(ID:str):
    if(jwtBearer.CDBConnectionstring ==""):
        wconnection=pyodbc.connect(Connection.LiveConnection.value)
    else:       
        wconnection=pyodbc.connect(f'DRIVER=ODBC Driver 18 for SQL Server;SERVER={jwtBearer.CDBConnectionstring};DATABASE={jwtBearer.CDbName};UID={username2};PWD={password2};TrustServerCertificate=yes;Encrypt=no;Connection Timeout=30;')         
    SpNameOut=""
    try:
        param=""
        param +=f"@ID={ID},@VendorID={jwtBearer.CVendorID}"
        cursor=wconnection.cursor()             
        cursor.execute(f"EXEC WR_mstVendorDynamicChart_GetchartDetail {param}") 
        rows = cursor.fetchone() 
        print(rows)
        SpNameOut=rows[0]        
        cursor.commit()
    except Exception as e:
        print('GetDynamicSpName',str(e))
        cursor.rollback()
    finally:
        cursor.close()
        wconnection.close()  
    return SpNameOut    



# def ExecuteDataReader(param,spname,MethodNname,Result2):
#     key_value_pairs=[]
#     drivers = [item for item in pyodbc.drivers()]    
#     connection=pyodbc.connect(DBConfig.WRconnection)
#     try:
#         cursor=connection.cursor()        
#         cursor.execute(f"EXEC {spname} {param}")
#         columns = [column[0] for column in cursor.description]
#         rows = cursor.fetchall()        
#         for row in rows:
#             key_value_pairs.append(dict(zip(columns, row)))
            
#         while True:
#             Result2=cursor.fetchall()
#             if cursor.nextset()==False:
#                 break
#         cursor.close()
#         connection.close()
#     except Exception as e:
#         print(MethodNname + 'Error :- ',e)
#         print('SQL Query',f"EXEC {spname} {param}")
#         print('driver',drivers)
#         connection.close()
#     return key_value_pairs

# def ExecuteDataReader(param,spname,MethodNname,Connections):
    # key_value_pairs=[]
    # drivers = [item for item in pyodbc.drivers()]    
    # connection=pyodbc.connect(DBConfig.WRconnection)
    # try:
    #     cursor=connection.cursor()        
    #     cursor.execute(f"EXEC {spname} {param}")
    #     columns = [column[0] for column in cursor.description]
    #     rows = cursor.fetchall()        
    #     for row in rows:
    #         key_value_pairs.append(dict(zip(columns, row)))
    #     cursor.close()
    #     connection.close()
    # except Exception as e:
    #     print(MethodNname + 'Error :- ',e)
    #     print('SQL Query',f"EXEC {spname} {param}")
    #     print('driver',drivers)
    #     connection.close()
    # return key_value_pairs

def  CommonParam(input:CardandChartInput):
    param=""
    if(input.strBranch!=''):
        param +=f" @strBranchID='{input.strBranch}',"
    if(input.strTeamModeofSale!=''):
        param +=f" @strTeamModeofSale='{input.strTeamModeofSale}',"  
    if(input.strCity!=''):
        param +=f" @strCity='{input.strCity}',"
    if(input.strDayBook!=''):
        param +=f" @strDayBookID='{input.strDayBook}',"
    if(input.strDesignCatalogue!=''):
        param +=f" @strDesignCatalogue='{input.strDesignCatalogue}',"
    if(input.FromDate!=''):
        param +=f" @FromDate='{input.FromDate}',"
    if(input.ToDate!=''):
        param +=f" @ToDate='{input.ToDate}',"
    if(input.strItem!=''):
        param +=f" @strItemID='{input.strItem}',"
    if(input.strSubItem!=''):
        param +=f" @strSubItemID='{input.strSubItem}',"
    if(input.strItemGroup!=''):
        param +=f" @strItemGroupID='{input.strItemGroup}',"
    if(input.strItemSubitem!=''):
        param +=f" @strItemSubitemID='{input.strItemSubitem}',"
    if(input.strMetalType!=''):
        param +=f" @strMetalType='{input.strMetalType}',"
    if(input.strModeofSale!=''):
        param +=f" @strModeofSale='{input.strModeofSale}',"
    if(input.strPurchaseParty!=''):
        param +=f" @strPurchaseParty='{input.strPurchaseParty}',"
    if(input.strProduct!=''):
        param +=f" @strProductID='{input.strProduct}',"
    if(input.strSaleman!=''):
        param +=f" @strSalemanID='{input.strSaleman}',"
    if(input.strSaleAging!=''):
        param +=f" @strSaleAging='{input.strSaleAging}',"
    if(input.strSalesParty!=''):
        param +=f" @strSalesParty='{input.strSalesParty}'," 
    if(input.strRegionID!=''):
        param +=f" @strRegionID='{input.strRegionID}',"         
    if(input.strMonth!=''):
        param +=f" @strMonth='{input.strMonth}',"
    if(input.strFinYear!=''):
        param +=f" @strFinYear='{input.strFinYear}',"  
    if(input.strState!=''):
        param +=f" @strState='{input.strState}'"
    else:
        param = param[:len(param)-1]
    
    return param