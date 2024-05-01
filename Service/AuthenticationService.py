
from Crypto.Cipher import AES
from DAL import DBConfig
from io import BytesIO
import base64
import time
import jwt
# import pprp.crypto
from Entity.DTO.WsInput import Login
from Entity.DTO.WsResponse import LoginResult,AuthenticationResult 
from decouple import config

JWT_KEY=config("secret")
JWT_ALGO=config("algorithm")
ENCRYPTION_ALGORITHM_NAME = 'Rijndael'
ENCRYPTION_INIT_VECTOR = '!#@%IVAPO0SP&UHK'
ENCRYPTION_KEY = 'T@#r$t~145S^$%^&*()_+'
ENCRYPTION_KEY_BYTES = 16 

def decrypt(value):
    memory_stream_in = BytesIO()
    memory_stream_out = BytesIO()
    byte_buffer = bytearray(2048)
    result = ''
    try:
        # Write base64 decoded value to input memory stream
        memory_stream_in.write(base64.b64decode(value))
        memory_stream_in.seek(0)

        # Create symmetric algorithm (AES) with IV and key
        symmetric_algorithm = AES.new(
            GetKey(ENCRYPTION_KEY),
            AES.MODE_CBC,
            ENCRYPTION_INIT_VECTOR.encode('utf-8')
        )

        # Create crypto stream
        crypto_stream = AESStream(memory_stream_in, symmetric_algorithm)

        # Read and decrypt data
        while True:
            value_length = crypto_stream.readinto(byte_buffer)
            if value_length == 0:
                break
            memory_stream_out.write(byte_buffer[:value_length])

        # Convert decrypted data to string
        result = memory_stream_out.getvalue().decode('utf-8').rstrip('\0')
    except Exception as e:
        raise e
    finally:
        memory_stream_in.close()
        memory_stream_out.close()
    print(result,'decrption')
    return result.strip()

class AESStream:
    def __init__(self, memory_stream, cipher):
        self.memory_stream = memory_stream
        self.cipher = cipher

    def readinto(self, buffer):
        chunk = self.memory_stream.read(len(buffer))
        decrypted_chunk = self.cipher.decrypt(chunk)
        buffer[:len(decrypted_chunk)] = decrypted_chunk
        return len(decrypted_chunk)

def GetKey(key):
    result_key = key[:ENCRYPTION_KEY_BYTES] if len(key) >= ENCRYPTION_KEY_BYTES else key.ljust(ENCRYPTION_KEY_BYTES, '0')
    return result_key.encode('utf-8')


def LoginServi(input:Login):
    result=LoginResult()
    if(input.LoginID == ""):
      result.Message.append("Please enter LoginID")
    elif(input.PassWord == ""):
      result.Message.append("Enter Your Password")
    if(len(result.Message)==0):
      try:
        lstresult=[]
        param=""
        param=DBConfig.spParam(input)
        lstresult=DBConfig.ExecuteDataReader(param,"WR_mstuser_GetByID","LoginServi")
        if(len(lstresult)>0):
          for row in lstresult:
            result.UserName=row
        else:
          result.HasError=True
          result.Message.append("Enter Correct LoginID and Password")
      except Exception as E:
        result.Message.append(str(E))
        result.HasError=True
    return result
  
def Authentication(input:Login):
    result=AuthenticationResult()
    if(input.LoginID == ""):
      result.Message.append("Please enter LoginID")
    elif(input.PassWord == ""):
      result.Message.append("Enter Your Password")
    if(len(result.Message)==0):
        lstresult=[]
        param=f"@LoginID='{input.LoginID}'"        
        lstresult=DBConfig.ExecuteDataReader(param,"WR_mstuser_GetAuth","Authentication")       
        if(len(lstresult)>0):
          # for row in lstresult[0]:
            obj=lstresult[0]
            print('obj',lstresult[0]['Password'])
            if(input.PassWord==decrypt(lstresult[0]['Password'])):                
                result.Token=TokenGenrater(lstresult[0])
                result.UserName=lstresult[0]['UserName']
            else:
              result.HasError=True
              result.Message.append("Invalid Password....!")
              
        else:
            result.HasError=True
            result.Message.append("Invalid User....!")
    else:
        pass
    return result
  
def TokenGenrater(input):
      print(input,'Token Gen')
      payload={
        "UserID":input['UserID'],
        "VendorID":input['VendorID'],
        "ConnectionString":input['Connectionstring'],
        "DbName":input['DbName'],
        "expiry":time.time()+600000        
      }
      token=jwt.encode(payload,JWT_KEY,algorithm=JWT_ALGO)
      return token
    
    
