# author: yang time:2020/5/22.
# from core import scr #在执行文件这处理好，后边都好导入
#不要导入start.py，这是违反规定的
#只是mutst被写死了
import os
BASE_DIR=os.path.dirname(os.path.dirname(__file__))
LOG_PATH=r'%s/log/user.log' %BASE_DIR