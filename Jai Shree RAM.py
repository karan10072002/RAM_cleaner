import os
import time
import random

def size_any(data_size):
    try:
        if data_size>=1000 and data_size<=1000000-1:
            data_size/=1000        
            data_size=str(round(data_size,2))+' KB'
        elif data_size>=1000000 and data_size<=1000000000-1:
            data_size/=1000000
            round(data_size,2)
            data_size=str(round(data_size,2))+' MB'        
        elif data_size>=1000000000:
            data_size/=1000000000
            round(data_size,2)
            data_size=str(round(data_size,2))+' GB'
    except:
        pass
    return data_size
# print(size_any('-'))

ram_use=0
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

# print((ram_use)/((10**6)*8))
# print(new_list)


with open(r'D:\basic ram usage.txt','r+') as gg:
	basic=gg.read()
d
basic=eval(basic)

all_killed=[]
for tasks in new_list:
	if tasks not in basic and 'python.exe' not in tasks and 'svchost.exe' not in tasks and 'tasklist.exe' not in tasks and 'cmd.exe' not in tasks and 'py.exe' not in tasks and 'Taskmgr.exe' not in tasks:
		os.system('taskkill /f /im {} /t'.format(tasks))
		all_killed.append(tasks)

print('\n\n\tsucessfully released RAM: fully optimized\n\n')
print('Processes worked upon: \n')
for hh in all_killed:
	print(" ",hh)
input('\nPress Enter to exit this terminal.')
