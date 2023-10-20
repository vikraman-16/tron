import hashlib
print("Enter the data")
data=input()
hash_object= hashlib.sha256()
hash_object.update(data.encode('utf-8'))
hash_hex=hash_object.hexdigest()
print(f"The sha 256 hash of {data} is {hash_hex}" )
