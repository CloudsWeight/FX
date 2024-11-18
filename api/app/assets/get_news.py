import json
def test():
	print(f'{json.dumps([{"TEST":42},{"TEST":43}])}')

if __name__ == "__main__":
	try:
		test()
	except:
		pass
