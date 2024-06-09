password = 'a123456'
x = 3
while True:
	pwd = input ('please enter the password: ')
	if pwd == password:
		print ('you got it')
		break
	else:
		x = x - 1
		print ('error, you got', x, 'times')
		if x == 0:
			print ('you failed')
			break
