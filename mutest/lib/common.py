# author: yang time:2020/5/22.
from conf import settings
import time
def logger(msg):
    with open(settings.LOG_PATH, mode ='at',encoding='utf-8')as f:
        f.write('%s %s\n' %(time.strftime('%Y-%m-%d %H:%M:%S'),msg))