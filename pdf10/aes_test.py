# AES-GCM decryption example 
from Crypto.Cipher import AES 
key = b"16bytekey1234567"  # 16-byte key 
iv = b"12byteiv1234"      # 12-byte IV 
cipher = AES.new(key, AES.MODE_GCM, iv) 
encrypted = cipher.encrypt(b"secret") 
decipher = AES.new(key, AES.MODE_GCM, iv) 
decrypted = decipher.decrypt(encrypted) 
print(f"Decrypted: {decrypted}") 
