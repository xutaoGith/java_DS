from urllib.parse import quote
from demo import CollectMethod
import json
import requests
import re
import redis
import random
from proxy import *


class PublicMethod:
    def __init__(self):
        self.js_name = 'jscode_ak.js'
        self.collect_method = CollectMethod()
        self.R = redis.Redis(host='192.168.2.210', port=6379, db=4, password="")
        self.user_agent_list = [
             "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36",
            'Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; MI NOTE LTE Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/8.8.7',
            'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.0 Mobile/15E148 Safari/604.1',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Version/10.0 Mobile/14D27 Safari/602.1',
            'Mozilla/5.0 (Linux; Android 5.1.1; Nexus 5 Build/LMY48B; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.65 Mobile Safari/537.36',
            'Mozilla/5.0 (Linux; U; Android-4.0.3; en-us; Galaxy Nexus Build/IML74K) AppleWebKit/535.7 (KHTML, like Gecko) CrMo/16.0.912.75 Mobile Safari/535.7',
            'Mozilla/5.0 (Linux; U; Android-4.0.3; en-us; Xoom Build/IML77) AppleWebKit/535.7 (KHTML, like Gecko) CrMo/16.0.912.75 Safari/535.7',
            'Mozilla/5.0 (Linux;u;Android 4.2.2;zh-cn;) AppleWebKit/534.46 (KHTML,like Gecko) Version/5.1 Mobile Safari/10600.6.3',
            'Mozilla/5.0 (Linux; Android 4.0; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/59.0.3071.92',
            'Mozilla/5.0 (Linux; Android 6.0.1; SOV33 Build/35.0.D.0.326) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.91 Mobile Safari/537.36',
            'Mozilla/5.0 (Linux; Android 6.0; HUAWEI MLA-AL10 Build/HUAWEIMLA-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36',
            'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.96 Mobile Safari/537.36',
            'Mozilla/5.0 (Linux; Android 7.1.1; vivo X20A Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/5.6.1.1',
            'Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; SM-J7108 Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.9.7.977 Mobile Safari/537.36',
            'Mozilla/6.0 (Linux; Android 8.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.183 Mobile Safari/537.36'
        ]
    def processing_name(self, name):
        name1 = re.findall(r'[?|、|:|//|*|“|”|"|<|>]', name)
        if name1:
            for i in name1:
                name = name.replace(i, quote(i))
        name = name.replace('/', '————').replace('|', quote('|')).replace('\\', quote('\\'))
        return name


    def ip_proxies(self):
        r = redis.Redis(host='192.168.2.210', port=6379, db=3, password="")
        ree = redis.Redis(host='192.168.2.210', port=6379, db=2, password="")
        r2 = redis.Redis(host='192.168.2.210', port=6379, db=0, password="")
        while r.llen('IP') > 0:
            ip = r.blpop('IP')
            try:
                ip = eval(ip[1].decode().replace('http://', '').replace(' ', '').replace('http', 'HTTP').replace('s', 'S').replace('\\r\\n',''))
                cent = requests.get('https://www.baidu.com', proxies=ip, timeout=10)
                if cent.status_code == 200:
                    print(ip)
                    daili = ip
                    ree.set(json.dumps(daili),'ip')
                    ree.expire(json.dumps(daili), 700)
                    return daili
            except:
                print('-------失效的ip')

        while ree.dbsize() > 80:
            try:
                ip = eval(ree.randomkey())
                try:
                    d=eval(r2.get(json.dumps(ip)))
                    continue
                except:
                    pass

                A_ip =eval(str(ip).replace('http','HTTP').replace('s','S'))
                cent = requests.get('https://www.baidu.com', proxies=A_ip, timeout=10)
                if cent.status_code == 200:
                    print(ip)
                    daili = ip
                    return daili
            except:
                print('-------失效的ip')
                ree.delete(json.dumps(ip))
        daili = self.get_ip()
        return daili
    # 更换ip
    def get_ip(self):
        print('正在获取代理IP...')
        try:
            while True:
                # url_1 = "http://webapi.http.zhimacangku.com/getip?num=1&type=1&pro=&city=0&yys=0&port=1&pack=238257&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions="
                url_1 = 'http://tiqu.py.cn/getProxyIp?lb=1&return_type=txt&protocol=http&num=10'
                resp = requests.get(url=url_1)
                ip_list = resp.text
                if re.match(r'(?:(?:25[0-5]|2[0-4]\d|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)',
                            ip_list):
                    ip = resp.text.strip('\r\n')
                    break
            ree = redis.Redis(host='192.168.2.210', port=6379, db=2, password="")
            for ip in ip_list.split("\r\n")[:-1]:
                ip_arr = ip.split(":")
                # 代理服务器
                proxyHost = ip_arr[0]
                proxyPort = ip_arr[1]
                http = "%(host)s:%(port)s" % {
                    "host": proxyHost,
                    "port": proxyPort,
                }
                daili = {
                    "HTTP": http,
                    "HTTPS": http
                }
                print(daili)
                file = open('更换ip.txt', 'a', encoding='utf8')
                file.write(str(daili) + '\n')
                file.close()
                # r = redis.Redis(host='192.168.2.210', port=6379, db=3, password="")
                # r.lpush('IP', str(daili).replace('HTTPS','https').replace('HTTP','http'))

                ree.set(json.dumps(daili), 'ip')
                ree.expire(json.dumps(daili),360)
            return daili
        except Exception:
            pass

    # 更换token
    def change_token(self):
        while True:
            try:
                UA = random.choice(self.user_agent_list)
                USER_AGENT = UA

                # ip = get_proxy()
                # self.ip = {
                #     "http": ip,
                #     "https": ip
                # }
                self.ip = self.ip_proxies()
                # self.ip = self.get_ip()
                self.headers, self.ip = self.collect_method.get_ip(self.ip,USER_AGENT)
                return self.headers, self.ip
            except Exception as e:
                print(e)
                print('-------------------------更换token失败')

if __name__ == '__main__':
    r = redis.Redis(host='192.168.2.210', port=6379, db=0, password="")
    while True:
        t = PublicMethod()
        # ip =t.ip_proxies()
        # ip = t.get_ip()
        # continue

        headers, ip = t.change_token()
        try:
            text = requests.get('https://www.datasheets.com/en/part-details/m705-grn360-k2-v-senju-metal-industry-101908645',headers=headers,timeout=20,proxies=ip)
            text.close()
            print(text.text)
        except Exception as e:
            print(e)
        print(ip)
        if ip:
            #ip['HTTP'] = 'HTTP://'+ip['HTTP']
            #ip['HTTPS'] = 'HTTPS://' + ip['HTTPS']
            r.set(json.dumps(ip), json.dumps(headers))
            r.expire(json.dumps(ip), 90)
            # ip = eval(r.randomkey())
            # headers = eval(r.get(json.dumps(ip)))
            # while True:
            #try:
                #text = requests.get('https://www.datasheets.com/en',headers=headers,timeout=30,proxies=ip)
                #print(text.text)
            #except Exception as e:
            # print(e)