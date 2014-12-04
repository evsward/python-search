python-search
=============

### A little procedure of finding the file's absolute path which matches the keyword.

#### 简介
##### 编写一个search(s)的函数：
		1、在当前目录以及子目录下查找文件名包含字符串s的文件
		2、打印路径
##### 调用方法
		D:\Python27\workspace\python-search>python search.py test
		DEBUG:root:D:\Python27\workspace\python-search
		DEBUG:root:D:\Python27\workspace\python-search
		INFO:root:1
		INFO:root:D:\Python27\workspace\python-search\testcase.py

#### 思路
		1、获得要查询目录以及所有其子目录的路径
		2、查找这些路径下的文件，对关键字进行匹配

#### 备注
		logging.basicConfig(level=logging.INFO)
		改为
		logging.basicConfig(level=logging.DEBUG)
		即可看到调试信息，仿照java的log4j的配置。
		
		调用方法
		search函数中利用sys.argv[1]获取命令行参数
		下标从1开始
		
		lambda表达式，与Scala的=>一致。