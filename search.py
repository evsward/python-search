# -*- coding: utf-8 -*-
import os
import sys
import logging

logging.basicConfig(level=logging.INFO)


def search(position='.', key=sys.argv[1]):
    os.chdir(position)
    logging.debug(os.getcwd())
    result = []
    dirs = map(lambda y: os.path.join(os.path.abspath(position), y),
               [x for x in os.listdir(position) if os.path.isdir(x)])
    for item in dirs:
        logging.debug(item)
        # 获取子目录下的所有孙子目录的全路径，并添加到循环中
        os.chdir(item)
        logging.debug(os.getcwd())
        dirs += map(lambda y: os.path.join(os.path.abspath(item), y),
                    [x for x in os.listdir(item) if os.path.isdir(x)])
    # 开始在文件中查询关键字
    for one in [os.path.abspath(position)] + dirs:
        logging.debug(one)
        os.chdir(one)
        result += map(lambda y: unicode(os.path.join(os.path.abspath(position), y), 'gbk'),
                      [x for x in os.listdir(one) if os.path.isfile(x) and key in os.path.basename(x)])
    logging.info(len(result))
    for r in result:
        logging.info(r)


search()