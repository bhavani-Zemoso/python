import hashlib
md5 = hashlib.md5()

md5.update(b'Python rocks!')
print (md5.digest())
print (md5.hexdigest())