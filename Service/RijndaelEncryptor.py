# from Crypto.Cipher import AES
# import base64
 
# class RijndaelEncryptor(object):
#     """
#     Encrypts text using Rijndael 128 in CBC mode and using PKCS7 padding
#     """
    
#     def __init__(self, k=16):
#         self.k = k    #sets block size of 16 for padding, NOT FOR CIPHER
 
#     def _pkcs7decode(self, text):
#         """
#         Remove PKCS7 padding from text
#         """
#         val = text[-1]
#         if val > self.k:
#             raise ValueError('Input is not padded or padding is corrupt')
#         l = len(text) - val
#         return (text[:l]).decode(encoding="UTF-8")
 
#     def _pkcs7encode(self, text):
#         """
#         Add PKCS7 padding to text
#         """
#         l = len(text)
#         val = self.k - (l % self.k)
#         return text + bytearray([val] * val).decode(encoding="UTF-8")
 
#     def encrypt( text):
#         input_key="ompatelqwertyuio77887890"
#         input_iv="ompatelqwertyuio778878"
#         """
#         Encrypt method
#         Both Keys and IVs need to be 16 characters encoded in base64.
#         """
#         # Create aes object
#         print('input_key',input_key,len(input_key))
#         key = base64.b64decode(input_key)
#         print('keyppp',key,len(key))
#         iv = base64.b64decode(input_iv)
#         aes = AES.new(key, AES.MODE_CBC, iv)
#         # Pad text and encrypt
#         pad_text =RijndaelEncryptor._pkcs7encode(text)
#         cipher_text = aes.encrypt(pad_text)
#         print('cipher_text',cipher_text)
#         # print('Encryption',base64.b64encode(cipher_text))
#         # Encode to base64 and return
#         return cipher_text
#         # return base64.b64encode(cipher_text)
 
#     def decrypt(text):
#         """
#         Decrypt method
#         Both Keys and IVs need to be 16 characters encoded in base64.
#         """
#         # Create aes object
#         input_key="X#@q!p~!@#$%!^&}|()_-hb#"
#         input_iv="!@#$IV7890123456"
#         key = base64.b64decode(input_key)
#         iv = base64.b64decode(input_iv)
#         aes = AES.new(key, AES.MODE_CBC, iv)
#         # Decode from base64 and decrypt
#         decode_text = base64.b64decode(text)
#         pad_text = aes.decrypt(decode_text)
#         # Unpad text and return
#         return RijndaelEncryptor._pkcs7decode(pad_text)