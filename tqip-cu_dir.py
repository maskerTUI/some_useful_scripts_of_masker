#! /usr/bin/env python3
#author:masker
#2022.8.1
#这是一个提取ip然后去重的小脚本
#import the module
import re
import os

# opening and reading file the file
with open('ip.txt','r',encoding='utf-8')as fh:
	fstring = fh.readlines()
	
pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')

lst=[]

# extracting the IP addresses
for line in fstring:
	match = pattern.search(line)
	if match is not None:
		f = open('ip_only.txt','a',encoding='utf-8')
		f.writelines(match[0])
		f.writelines('\n')
		f.close()
#		lst.append(match[0])
	else:
		lst.append(None)
		
#display ip
#print(lst)

def remove_duplicates():
	f_read = open(r'ip_only.txt','r',encoding='utf-8')
	f_write = open(r'ip_only_clear.txt','a',encoding='utf-8')
	data=set()
	for a in [a.strip('\n') for a in list(f_read)]:
		if a not in data:
			f_write.write(a+'\n')
			data.add(a)
	f_read.close()
	f_write.close()
	
remove_duplicates()

#如果需要留着文本统计频率的可以注释掉下一行
os.remove('ip_only.txt')

print('finish!')
	