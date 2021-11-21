from hello import add


def test():
	passed = 0
	
	# add positive
	result = add(5, 10)
	assert result == 15
	passed += 1
	
	# add negative
	result = add(5, -10)
	assert result == -5
	passed += 1
	
	# add zero
	result = add(5, 0)
	assert result == 5
	passed += 1

if __name__ == "__main__":
	try: test()
	except AssertionError as e:
		print(f"Failed: Failed some tests")
		raise e
	
	print("Success: Passed all tests")
