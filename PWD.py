# passward = 'a123456'
password = 'a123456'
while True:
	pwd = input ('enter the password: ')
	if pwd == password:
		print ('you got it')
		break #break from loop
	else:
		x = 2
		while x > 0:
			print ('error, last', x, 'times')
			input ('enter the password ')
			x = x - 1
			if x <= 0:
				print ('you failed')
				raise SystemExit