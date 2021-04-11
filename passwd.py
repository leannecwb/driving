passwd = 'a123456'
x = 3
while x >= 1 : 
	user_passwd = input('請輸入你的密碼:')
	if user_passwd == passwd :
		print ('答對了!登入成功')
		break
	else :
		x = x - 1
		print ('你的密碼輸入錯誤，你還有',x,'次機會')
if x == 0 :
	print('你已用光3次機會，請離開!')
else :
	print('恭喜你，你有猜對密碼喔!')
