#!/usr/bin/python         
# -*- coding: UTF-8 -*-
#by Larmony
#python3.x

import nmap
import os
import datetime
import time
from multiprocessing import Pool

'''定义SYN扫描函数，结果以ip:port1 port2……的形式输出'''
def syn_scan(ip):    
	arg='-sS -p 20,21,22,23,25,53,69,79,80,110,111,135' #添加需要扫描的端口
	open_port=' '
	ip_port=''
	nm=nmap.PortScanner()      #PortScanner()实例化
	try:
		print("正在扫描%s" %(ip))
		result=nm.scan(ip,arguments=arg)                 #扫描结果存储到result
		for port in result['scan'][ip]['tcp'].keys():    #从扫描结果result中提取ip和开放端口
			state=result['scan'][ip]['tcp'][port]['state']     
			if state == "open":
				open_port=open_port +' '+ str(port)
				ip_port=ip+':'+open_port
			else:
				continue
	except:
		pass
	return ip_port

'''定义IP读取函数，结果为一个IP列表'''
def get_iplist(file_name):        
	iplist=[]
	with open('./%s'%(file_name),'r') as file:
		for line in file:
			ip = line.strip('\n')
			iplist.append(ip)
	return iplist
'''定义多线程扫描函数，结果为一个ip:port port字符串'''
def multi_scan(file_name):
	iplist=get_iplist(file_name)
	result_str=''
	pool=Pool()       #Pool类实例化
	result=pool.map(syn_scan,iplist)   #多进程并发扫描，扫描结果为一个列表
	for i in result:                   #把扫描结果由列表转换为字符串，存入result_str，方便写入文件
		if len(i)==0:                  #把列表中的空元素剔除
			continue
		else:
			result_str=result_str+'\n'+i
	return result_str
'''定义写文件函数，把扫描结果写入txt'''
def write_txt(result):
    #构造文件名和存储路径
	today=datetime.date.today()   
	file_name='result%02d%02d.txt'%(today.month,today.day)  #构造result0201.txt样式的文件名
	file_path=os.getcwd()+'\\' + file_name   #构造存储路径，路径为当前文件夹
	#结果存入当前路径下的file_name.txt
	with open('./%s'%(file_name),'w') as file:     
		file.write(result)
	print('扫描结束，扫描结果存储于%s'%(file_path))
	
'''主函数'''
if __name__=="__main__": 
	start_time=time.time()
	print('扫描中……\n扫描将花费时间较长……请耐心等待……')
	result=multi_scan('iplist.txt')           #多线程扫描
	write_txt(result)                         #结果写入txt
	end_time=time.time()
	time_cost=(end_time-start_time)/60
	print('本次扫描共花费%d分钟'%(time_cost))