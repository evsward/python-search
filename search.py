# -*- coding: utf-8 -*-
import os
import sys
import logging

logging.basicConfig(level=logging.INFO)


def search(position='.', key=sys.argv[1]):
    os.chdir(position)
    logging.debug(os.getcwd())
    result = []
    dirs = [os.path.join(os.path.abspath(position), x) for x in os.listdir(position) if os.path.isdir(x)]
    for item in dirs:
        logging.debug(item)
        # 获取子目录下的所有孙子目录的全路径，并添加到循环中
        os.chdir(item)
        logging.debug(os.getcwd())
        dirs += [os.path.join(os.path.abspath(item), x) for x in os.listdir(item) if os.path.isdir(x)]
    # 开始在文件中查询关键字
    for one in [os.path.abspath(position)] + dirs:
        logging.debug(one)
        os.chdir(one)
        result += [unicode(os.path.join(os.path.abspath(position), x), 'gbk') for x in os.listdir(one) if
                   os.path.isfile(x) and key in os.path.basename(x)]
    for r in result:
        logging.info(r)
    logging.info(len(result))


search()