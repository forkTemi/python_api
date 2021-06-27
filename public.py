# coding:utf-8
'''
   program: public.py
   author: temi
'''

import sys
import os
import time


def oscmd(cmd):
    runcmd = os.popen(cmd).readlines()
    rtl = []
    for i in runcmd:
        rtl.append(i.strip())
    return rtl


def run_machine(node):
    rtl = oscmd('machine start {0}|grep -E "alreay Running|{1}"'.format(node, node))
    return rtl


def cpu_stat():
    f = open('/proc/stat')
    lines = f.readlines();
    f.close()
    for line in lines:
        line = line.lstrip()
        counters = line.split()
        if len(counters) < 5:
            continue
        if counters[0].startswith('cpu'):
            break
    total = 0
    for i in range(1, len(counters)):
        total = total + int(counters[i])
    idle = int(counters[4])
    return {'total': total, 'idle': idle}

def cpu_info():
    f = open('/proc/stat')
    lines = f.readlines();
    f.close()
    for line in lines:
        line = line.lstrip()

def cpu_used():
    counters1 = cpu_stat()
    time.sleep(0.1)
    counters2 = cpu_stat()
    idle = counters2['idle'] - counters1['idle']
    total = counters2['total'] - counters1['total']
    return {'code':1,'msg':round(100 - (idle * 100 / total),2),'data':'ok'}


def meminfo():
    res = {'total': 0, 'free': 0, 'buffers': 0, 'cached': 0}
    f = open('/proc/meminfo')
    lines = f.readlines()
    f.close()
    i = 0
    for line in lines:
        if i == 4:
            break
        line = line.lstrip()
        memItem = line.lower().split()
        if memItem[0] == 'memtotal:':
            res['total'] = int(memItem[1])
            i = i + 1
            continue
        elif memItem[0] == 'memfree:':
            res['free'] = int(memItem[1])
            i = i + 1
            continue
        elif memItem[0] == 'buffers:':
            res['buffers'] = int(memItem[1])
            i = i + 1
            continue
        elif memItem[0] == 'cached:':
            res['cached'] = int(memItem[1])
            i = i + 1
            continue
    return res

def men_used():
    counters = meminfo()
    used = counters['total'] - counters['free'] - counters['buffers'] - counters['cached']
    total = counters['total']
    return {'code':1,'msg':round(used * 100 / total,2),'data':'ok'}

def cpu_count():
    f = open('/proc/cpuinfo')
    lines = f.readlines();
    f.close()
    i = 0
    for line in lines:
        line = line.lstrip()
        if 'processor' in line:
            i = i + 1
    return {'code':1,'msg':i,'data':'ok'}

def total_mem():
    return {'code':1,'msg':int(meminfo().get('total')/1024/1024),'data':'ok'}


if __name__ == '__main__':
    print(cpu_count())
