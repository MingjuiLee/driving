country = input('請問你是哪國人: ')	# declare一個cariable叫country
age = input('請你輸入年齡: ')
age = int(age)	# casting 型別轉換
if country == '台灣':
	if age >= 18:	# 雙層if 如果country不是台灣 就不會進來這一等級的if
		print('你可以考駕照')
	else:	# if 的延伸功能
		print('你還不能考駕照')
elif country == '美國':	# elif是根源於if 所以同屬上面的if大架構
	if age >= 16:
		print('你可以考駕照')
	else:
		print('你還不能考駕照')
else:	# 使用else 否則 告訴使用者 只能輸入台灣跟美國
	print('你只能輸入 台灣/美國')
# 共三條路線