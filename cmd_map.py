# coding:utf-8

from public import *

#定义参数对应函数
func_dict = {
    "cpu_count": cpu_count,
    "men_used": men_used,
    "cpu_used": cpu_used,
    "total_mem": total_mem

}

def func_None():
    return {'code':0,'msg':'cannot find func','data':'cannot find func'}


def execute_fun(x , y = []):
    return func_dict.get(x ,func_None)()