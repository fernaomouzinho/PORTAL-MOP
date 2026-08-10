import hashlib

def getjustnewid(table_name):
	result = table_name.objects.last()
	if result:
		newid = result.id + 1
	else:
		newid = 1
	return newid
	
def hash_md5(strhash):
	hashed = hashlib.md5(strhash.encode())
	return hashed.hexdigest()