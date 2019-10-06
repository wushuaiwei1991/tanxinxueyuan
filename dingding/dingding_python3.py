#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import json
import sys
import os

headers = {'Content-Type': 'application/json;charset=utf-8'}
api_url = 'https://oapi.dingtalk.com/robot/send?access_token=f37969de387e49df897814c3a3084d25305d577cefb1cdcc67a754dadf0b3226'

def msg(text):
    json_text = {
     "msgtype": "text",
        "at": {
            "atMobiles": [
                
            ],
            "isAtAll": True
        },
        "text": {
            "content": text
        }    
    } 
    request = requests.post(api_url,json.dumps(json_text),headers=headers)
    print(request.text) 
     
if __name__ == '__main__':
    text = sys.argv[1]
    msg(text)