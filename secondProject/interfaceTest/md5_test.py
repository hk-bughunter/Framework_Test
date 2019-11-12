import hashlib
m=hashlib.md5()
print(m)
str="123456"
m.update(str.encode())
encodestr=m.hexdigest()
print(encodestr)