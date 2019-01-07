country = input('請問你是哪國人: ')	# declare一個cariable叫country
age = input('請你輸入年齡: ')
age = int(age)	# casting 型別轉換
if country == '台灣':
	if age >= 18:	# 雙層if 如果country不是台灣 就不會進來這一等級的if
		print('你可以考駕照')
	else:	# if 的延伸功能
		print('你還不能考駕照')