#!/usr/bin/python         
# -*- coding: UTF-8 -*-
#by Larmony
#python3.x

import nmap
import os
import datetime
import time
import pandas
from multiprocessing import Pool

'''定义SYN扫描函数，结果以ip:port1 port2……的形式输出'''
def syn_scan(ip):    
	arg='-sS -p 20,21,22,23,25,53,69,79,80,110'
	open_port=' '
	ip_port=[ip]
	nm=nmap.PortScanner()      #PortScanner()实例化
	try:
		print("正在扫描%s" %(ip))
		result=nm.scan(ip,arguments=arg)                 #扫描结果存储到result
		for port in result['scan'][ip]['tcp'].keys():    #从扫描结果result中提取ip和开放端口
			state=result['scan'][ip]['tcp'][port]['state']     
			if state == "open":
				open_port=ip_port.append(str(port))
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
'''定义多线程扫描函数，结果为一个[IP,port]列表'''
def multi_scan(file_name):
	iplist=get_iplist(flie_name)
	pool=Pool()       #Pool类实例化
	result=pool.map(syn_scan,iplist)   #多进程并发扫描，扫描结果为一个列表
	for i in range(len(result)-1, -1, -1):
			if len(result[i])==1:
				result.remove(result[i])      #把列表中的只有IP没有端口的元素剔除
			else:
				pass
	return(result)
'''定义写文件函数，把扫描结果写入excel'''
def write_xlsx(result):
    #构造文件名和存储路径
	today=datetime.date.today()   
	file_name='result%02d%02d.xlsx'%(today.month,today.day)  #构造result0201.txt样式的文件名
	file_path=os.getcwd()+'\\' + file_name   #构造存储路径，路径为当前文件夹
	#结果存入当前路径下的file_name.xlsx
	header_list=['ip']
	for i in range(len(result)-1):
		i=str(i+1)
		header_list.append('port%s'%(i))
	result_df=pandas.DataFrame(data=result)
	with pandas.ExcelWriter(path=file_path) as file:
		result_df.to_excel(excel_writer=file,sheet_name='Sheet1',header=header_list,index=False)
	print('扫描结束，扫描结果存储于%s'%(file_path))
	
'''主函数'''
if __name__=="__main__": 
	start_time=time.time()
	print('扫描中……\n预计扫描将花费30~60分钟……请耐心等待……')
	result=multi_scan('iplist.txt')           #多线程扫描
	write_xlsx(result)                  #结果写入xlsx
	end_time=time.time()
	time_cost=(end_time-start_time)/60
	print('本次扫描共花费%d分钟'%(time_cost))