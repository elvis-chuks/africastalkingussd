var = 100
def test():
	global var
	if var == 100:
		var = 'egg'
		print(var)
	return var

test()
print(var)