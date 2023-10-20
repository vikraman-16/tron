import hashlib
str2hash="toencryptinmd5"
res=hashlib.md5(str2hash.encode())
print("the hexadecimal of hash is:",res.hexdigest())
