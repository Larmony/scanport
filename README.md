这是两个端口扫描工具，txt文件夹下程序的扫描结果以'<ip : openport openport>'的形式存储为txt文件，excel文件夹下的程序扫描结果以'<ip openport  openport>'形式存储为excel文件
### 用法：
#### 1.修改你需要扫描的端口  
修改程序中修改代码文件中arg='-sS -p 20,21,22,23,25,53,69,79,80,110'，把引号中的端口改为你需要扫描的端口，端口间以逗号分隔；如果是扫描端口范围，改为arg='-sS -p 1-65535'形式。
#### 2.规范IP文件  
存放需要扫描的IP的文件必须是txt格式，一个IP一行，文件名iplist.txt,需要和源文件放置在同一个路径下
#### 3.执行：
'<python portscan_excel.py>'  
或者  
'<python portscan_excel.py>'
