# author: yang time:2020/5/22.
import time

#各部分公用的功能放common里

from lib.common import logger

def login():
    print("登陆")
    logger("登陆了")

def register():
    print("注册")

def witdraw():
    print("提现功能")

def transfer():
    print("转账功能")


func_dic={
    '0':['登陆',login],
    '1':['注册',register],
    '2':['提现',witdraw],
    '3':['转账',transfer],
}

def run():
    while True:
        for k in func_dic:
            print(k,func_dic[k][0])

        choice= input('请输入指令编号： ').strip()
        if choice in func_dic:
            func_dic[choice][1]()
        else:
            print("请输入：")



