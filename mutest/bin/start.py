# # author: yang time:2020/5/22.
# #应该采用绝对导入===》sys.path====>执行文件
# import sys
# sys.path.append('F:/pycharmworkspace/mutest') #在执行文件这处理好，后边都好导入
# # import scr
# # scr.run()
#
# from core import  scr
# # scr.run()
# from core.scr import  run
# run()

#优化方案
import os
import sys
#print(__file__) #当前文件的绝对路径 F:/pycharmworkspace/mutest/bin/start.py
#print(os.path.dirname(__file__)) #F:/pycharmworkspace/mutest/bin
Base_DIR= os.path.dirname(os.path.dirname(__file__)) #F:/pycharmworkspace/mutest 成了
sys.path.append(Base_DIR)

from core import scr

if __name__ == '__main__':

    scr.run()