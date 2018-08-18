#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:ZhangHui
@file: getLoc.py
@time: 2018/8/18
@useage: getLoc.py 客户list.txt > 结果.txt
"""
import requests,sys
from getUserAgent import getUserAgent
from time import sleep


def run(name):
    headers = getUserAgent()
    url = 'https://baike.baidu.com/wikiui/api/getcertifyinfo?lemma={}'.format(name)
    req = requests.get(url,headers=headers)
    dicts = eval(req.text)
    datas = dicts['data']
    print(datas['lemmaTitle']+'&'+
          datas['location']+'&'+
          datas['scope']+'&'+
          datas['legalPerson']+'&'+
          datas['regCapital']+'&'+
          datas['level']+'&'+
          datas['belongOrg']
          )

#run('湘潭三峰数控机床有限公司')

def Control(inputname):
    with open(inputname,'r') as f:
        for i in f.read().splitlines():
            try:
                run(i)
            except Exception as e:
                print(i)
            sleep(0.1)
if sys.argv[1]:
    Control(sys.argv[1])