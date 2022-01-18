import os

new=os.popen('tasklist')
new_list=[]
for i in new:
	if 'Image Name' not in i and '===============' not in i:
		i=i.split('    ')
		raw_size=i[-1]
		raw_size=raw_size.replace(',','')
		raw_size=raw_size.replace(' K','')
		raw_size=raw_size.replace('\n','')
		raw_size=raw_size.replace(' ','')
		# print(raw_size)
		try:
			raw_size=int(raw_size)
			ram_use+=raw_size
		except:
			# print('failed for: ',raw_size)
			pass
		if i[0] not in new_list:
			new_list.append(i[0])


with open(r"D:\basic ram usage.txt", "w") as ff:
	ff.write(str(new_list))