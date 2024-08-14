from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def decrypt_file(input_file, output_file, key):
    cipher = AES.new(key, AES.MODE_CBC)
    
    with open(input_file, 'rb') as f:
        ciphertext = f.read()
       
        
    decrypted_text =unpad(cipher.decrypt(ciphertext), AES.block_size)
    
    
    
    with open(output_file, 'wb') as f:
        f.write(decrypted_text)
 
 # Generate a random 16-byte key
key = b'mysecretpassword'


decrypt_file("encrypted.txt", "decrypted.txt", key)