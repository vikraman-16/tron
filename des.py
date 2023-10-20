import pyDes

key=b'abcdefgh'
cipher =pyDes.des(key, pyDes.ECB, padmode=pyDes.PAD_PKCS5)

message ="HELLO, DES!"

encrypt_text=cipher.encrypt(message)
print("Encrypted message:",encrypt_text)

decrypt_text=cipher.decrypt(encrypt_text)
print("Decrypted message:",decrypt_text.decode('utf-8'))
