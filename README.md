#这是两个基于nmap的端口扫描脚本，扫描到的open端口以IP:port1 port2的形式存储于脚本所在路径下名为result[日期].txt的txt文件中或者result[日期].xlsx的excel文件中
#用法：
#1.修改你需要扫描的端口
#修改源文件中参数行arg='-sS -p 20,21,22,23,25,53,69,79,80,110'，把引号中的端口改为你需要扫描的端口，端口间以逗号分隔；如果是扫描端口范围，改为arg='-sS -p 1-65535'形式。
#2.规范IP文件
#存放需要扫描的IP的文件必须是txt格式，一个IP一行，文件名iplist.txt,需要和源文件放置在同一个路径下
#3.执行代码
#python portscan_txt.py
#python portscan_excel.py
