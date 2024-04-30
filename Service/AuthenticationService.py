
# from Crypto.Cipher import AES
from DAL import DBConfig

# import pprp.crypto
from Entity.DTO.WsInput import Login
from Entity.DTO.WsResponse import LoginResult 
key="X#@q!p~!@#$%!^&}|()_-hb#"
iv="!@#$IV7890123456"
blocksize=24
s="NAts58zed8FrDT6pU7Le8w=="


# def rjindael_decrypt_gen_CBC(key, s, iv, block_size=pprp.config.DEFAULT_BLOCK_SIZE_B):
#     r = pprp.crypto.rijndael(key, block_size=block_size) 

#     i = 0
#     for block in s:

#         decrypted = r.decrypt(block)
#         print(decrypted,"decrypted")
#         decrypted = xor(decrypted, iv)  
#         iv = block

#         yield decrypted
#         i += 1

# def xor(block, iv):
#     resultList = [ (a ^ b) for (a,b) in zip(block, iv) ]
#     return bytes(resultList)

# def decryption():
#     blocksize = 16
#     sg = pprp.data_source_gen(s, blocksize) 
#     dg = rjindael_decrypt_gen_CBC(key, sg, iv, blocksize)
#     decrypted = pprp.decrypt_sink(dg, blocksize)
#     print("Decrypted data: " + str(decrypted))



# Working Code
# def fix_binary_data_length(binary_value):
#   block_length = 16
#   binary_value_length = len(binary_value)
#   length_with_padding = (
#     binary_value_length + (block_length - binary_value_length) % block_length
#   )
#   return binary_value.ljust(length_with_padding, b'0')

# def encrypt(value: str):
#   binary_iv = iv.encode('UTF-8')
#   binary_key = key.encode('UTF-8')
#   binary_value = value.encode('UTF-8')
#   cipher = AES.new(binary_key, AES.MODE_CBC, binary_iv)
#   pad="0"
#   binary_value1=lambda s:s +(16-len(s)% 16)*pad  
#   inary_value = fix_binary_data_length(binary_value)
#   encrypted_value = cipher.encrypt(inary_value)
#   print(encrypted_value)  
#   return str(encrypted_value)

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