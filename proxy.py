'''
Author       :Loyd zeng.yd@outlook.com
Date         :2022-11-04 11:47:49
LastEditors  :Loyd
LastEditTime :2022-11-21 15:26:37
FilePath     :/tmp/home/loyd/文档/loyd/Projects/14-Platform/platform/proxy.py
Description  :

Copyright (c) 2022 by Loyd zeng.yd@outlook.com, All Rights Reserved. 
'''

import json
import re
import socket
from base64 import b64encode

import requests

class NoneError(Exception):
    ...

def is_valid_proxy(proxy, check_url=None):

    """
    检验代理是否有效
    @param proxy: xxx.xxx.xxx:xxx
    @param check_url: 利用目标网站检查，目标网站url。默认为None， 使用代理服务器的socket检查, 但不能排除Connection closed by foreign host
    @return: True / False
    """

    is_valid = False

    if check_url:
        proxies = {"http": f"http://{proxy}", "https": f"http://{proxy}"}
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
        }
        response = None
        try:
            response = requests.get(
                check_url, headers=headers, proxies=proxies, stream=True, timeout=20
            )
            is_valid = True

        except Exception as error:
            pass

        finally:
            if response:
                response.close()

    else:
        ip, port = proxy.split(":")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sk:
            sk.settimeout(7)
            try:
                sk.connect((ip, int(port)))  # 检查代理服务器是否开着
                is_valid = True

            except Exception as error:
                print(error)

    return is_valid

def delete_proxy(proxy_dict):

    '''
    description:

    param proxy_dict {*}:
    return {*}
    '''
    
    proxy = proxy_dict.get('https')
    pattern = re.compile(r'\d+?.\d+?.\d+?.\d+?:\d+')
    ip_v4_and_port = pattern.search(proxy).group()

    # Format
    proxy_format = {
        'https': ip_v4_and_port,
        'http': ip_v4_and_port
    }

    proxy_b64 = b64encode(str(proxy_format).encode()).decode()

    requests.get(f'http://192.168.2.94:8000/delete?proxy={proxy_b64}', timeout=300)

def get_proxy():

    '''
    description: Get ip proxy.
    Example: xxx.xxx.xxx.xxx:xxx

    return {*}
    '''

    while True:
        resp = requests.get(
            url='http://192.168.2.94:8000/get',
            timeout=30
        )
        proxy = json.loads(resp.text)
        pattern = re.compile(r'\d+?.\d+?.\d+?.\d+?:\d+')
        ip_v4_and_port = pattern.search(proxy.get('https'))
        if ip_v4_and_port is None:
            print('---------ip池空')
            continue
        else:
            ip_v4_and_port = ip_v4_and_port.group()
        status = is_valid_proxy(proxy=ip_v4_and_port,check_url= 'https://www.baidu.com')
        if not status:
            delete_proxy(proxy_dict=proxy)
            continue
        return ip_v4_and_port

if __name__ == '__main__':
    print(get_proxy())
