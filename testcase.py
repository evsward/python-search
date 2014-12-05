# !/usr/bin/python
# -*- coding: utf-8 -*-
import os
import logging

print '查看当前工作目录：' + os.getcwd()
testdir = raw_input('请输入一个文件夹名字以供测试：')
try:
    os.mkdir(os.path.join(os.path.abspath('.'), testdir))
except WindowsError, e:
    logging.exception(e)
dirs = map(lambda y: os.path.abspath(testdir) + '\\test' + str(y), [x for x in range(1, 11)])
for p in dirs:
    try:
        os.mkdir(p)
        print '已建立测试目录：' + p
    except WindowsError, e:
        logging.exception(e)
    for x in range(1, 10):
        testdoc = 'new141203' + str(x) + '.txt'
        testdoc01 = 'testnew141203' + str(x) + '.txt'
        with open(p + '/' + testdoc, 'w') as f:
            f.write('hey!My girl~')
        with open(p + '/' + testdoc01, 'w') as f:
            f.write('hey!My girl~')
        print '--已建立测试文件：' + testdoc
        print '--已建立测试文件：' + testdoc01
