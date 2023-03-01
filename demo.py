import random
import re
import json
import redis
import requests
import execjs

requests.packages.urllib3.disable_warnings()




class CollectMethod(object):
    def __init__(self):
        self.js_name = 'jscode_ak.js'
        user_agent_list = [
            # "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36",
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
            "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
            "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
            "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
            "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
            "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        ]
        language = ['jscode_ak.js', 'jscode_ak_en_US.js', 'jscode_ak_en.js', 'jscode_ak_zh-cn.js']
        self.js_name = random.choice(language)
        self.js_name = 'jscode_ak_SJC.js'
        self.User = random.choice(user_agent_list)
        self.ip1 = "117.94.180.194:4231"
        self.ip = {'HTTP': self.ip1, 'HTTPS': self.ip1}

    def verify_ip(self):
        print('正在获取代理IP...')
        try:
            while True:
                url_1 = "http://webapi.http.zhimacangku.com/getip?num=1&type=1&pro=&city=0&yys=0&port=1&pack=182607&ts=0&ys=0&cs=0&lb=0&sb=0&pb=4&mr=1&regions="
                resp = requests.getresp = requests.get(url=url_1)
                ip = resp.text
                if re.match(r'(?:(?:25[0-5]|2[0-4]\d|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)',
                            ip):
                    ip = resp.text
                    break
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
            r = redis.Redis(host='192.168.2.102', port=6379, db=3, password="")
            r.lpush('IP', str(daili).replace('HTTPS', 'https').replace('HTTP', 'http'))
            return daili
        except Exception:
            pass

    # 获取p参数
    def getPParam(self):
        with open(self.js_name, mode="r") as f:
            content = f.read()
            obj = execjs.compile(content)
            result = obj.call("func")
            return result

    # 获取cookie
    def getheadercontent(self):

        while True:
            print('正在获取cookie...')
            url = "https://www.datasheets.com/en/search?q=audio"
            headers = {
                "Host": "www.datasheets.com",
                "Connection": "keep-alive",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": self.User,
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "Sec-Fetch-Site": "none",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-User": "?1",
                "Sec-Fetch-Dest": "document",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "zh-CN,zh;q=0.9"
            }
            response = requests.get(url=url, headers=headers, proxies=self.ip, verify=False, timeout=20)
            response.close()
            incap = ''.join(response.cookies.get_dict()).split('v')[0]
            ak_bmsc = ''
            if incap[:2] == 'ak':
                incap = incap.split('sc')[-1]
                ak_bmsc = 'ak_bmsc=' + response.cookies.get('ak_bmsc') + ";"
                # self.js_name = 'jscode_ak.js'
            headercontent = "visid_incap_2460745=" + response.cookies.get(
                "visid_incap_2460745") + ";" + incap + '=' + response.cookies.get(incap) + ";" + ak_bmsc
            token = self.isOk(headercontent)
            if token:
                break
        return headercontent

    headercontent = ''

    # 获取加密数字
    def num(self):
        print('正在获取加密数字...')
        try:
            headers = {
            "Host": "www.datasheets.com",
            "Connection": "keep-alive",
            "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"101\", \"Google Chrome\";v=\"101\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": self.User,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-User": "?1",
            "Sec-Fetch-Dest": "document",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9"
        }
            url = "https://www.datasheets.com/_Incapsula_Resource?SWJIYLWA=5074a744e2e3d891814e9a2dace20bd4,719d34d31c8e3a6e6fffd425f7e032f3"
            response_js = requests.get(url, proxies=self.ip, headers=headers, verify=False, timeout=10).text
            execobj = execjs.compile('''
                            function doing(str){
                                var z; 
                                for (var i = 0; i < str.length; i += 2) {
                                        z += String.fromCharCode(parseInt(str.substring(i, i + 2), 16));
                                    }
                                return z;
                            }
                            ''')
            result = re.search('b="(.*?)";', response_js)
            encodeJS = execobj.call("doing", result.group(1))[9:]
            target = ""
            for i in re.findall('catch.{11}\{(.*?)\}', encodeJS):
                target = i
            encodeJS = str(encodeJS).replace(target, "")
            keyword = re.findall("([\d\w]{9})\)\,\!\[\]", encodeJS)[0]
            replaceJs = re.findall(keyword + "=(.*?);", encodeJS)[0]
            encodeJS = encodeJS.replace(replaceJs, replaceJs + ";globalObject=" + keyword + ";")
            headerjs = open("header.js", mode="r").read()
            # open("change.js", mode="w", encoding="utf-8").write(headerjs + encodeJS)
            execobj = execjs.compile("function work(){" + headerjs + encodeJS + "return globalObject}")
            print('获取加密数字成功')
            return execobj.call("work")
        except Exception as e:
            pass
        return None

    # 服务器tokens回验
    def isOk(self, headercontent):
        print('正在验证服务器tokens...')
        SWHANEDL = self.num()
        if SWHANEDL:
            url = "https://www.datasheets.com/_Incapsula_Resource?SWHANEDL=" + SWHANEDL
            headers = {
            "authority": "www.datasheets.com",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-CN,zh;q=0.9",
            "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"101\", \"Google Chrome\";v=\"101\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "none",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": self.User,
                "Cookie": headercontent
        }

            try:
                response = requests.get(url, headers=headers, proxies=self.ip, verify=False, timeout=10)
                if (response.text == "window.location.reload(true);"):
                    print("回传验证成功！")
                    return True
            except:
                pass
        return False

    def get_ip(self, ip,user):

        self.ip = ip
        self.User = user

        headercontent = self.getheadercontent()
            # token = self.isOk(headercontent)

        url = "https://www.datasheets.com/ckly-was-is-go-theere-my-Iewes-neede-worth-And-h?d=www.datasheets.com"
        header = {
            "authority": "www.datasheets.com",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-CN,zh;q=0.9",
            "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"101\", \"Google Chrome\";v=\"101\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "none",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "content-type": "text/plain; charset=utf-8",
            "cookie": headercontent,
            "user-agent": self.User
        }
        data = {
            "solution": {
                "interrogation": self.getPParam()
            },
            "version": "stable",
            "old_token": None, "error": None, "performance": {"interrogation": 270}}
        chisu = 0
        while chisu <= 3:
            chisu = chisu + 1
            try:
                response = requests.post(url=url, headers=header, json=data, proxies=self.ip, timeout=190,
                                         verify=False).json()
                if response['token']:
                    break
            except:
                pass
        reese84 = response['token']
        self.headers = {
            "cookie": headercontent + "reese84=" + reese84,
            "referer": 'https://www.datasheets.com/api/taxonomies/breadcrumb?taxonomyPath=Semiconductor|Communication|Protocols%20and%20Networks',
            "user-agent": self.User
        }
        print('-------------------------更换token成功')
        print('-------------------------登录账号')
        head1 = self.headers
        head = self.headers
        head1['Accept'] = "application/json, text/plain, */*"
        head1['Content-Type'] = "application/json"

        url = "https://www.datasheets.com/api/account/token"
        data = {"email": "leo@ylc-tel.com", "password": "tqj5201314"}
        requestQ = requests.post(url, data=json.dumps(data), proxies=ip, headers=head1, verify=False,timeout=20).json()
        head['cookie'] = head['cookie'] + ';ident=' + '{"tokens":' + json.dumps(requestQ) + '}'.replace('{',
                                                                                                             '%7B').replace(
            '"', '%22').replace(':', '%3A').replace(',', '%2C').replace(' ', '').replace('}', '%7D') + ';'
        return head, self.ip


if __name__ == '__main__':

    t = CollectMethod()
    ip = t.verify_ip()
    # ip1 = '113.128.11.37:4264'
    # ip = {'HTTP': ip1, 'HTTPS': ip1}
    headers, ip = t.get_ip(ip)

    for i in range(1, 10):
        context = requests.get(
            url='https://www.datasheets.com/en/part-details/cd74hct299ee4-texas-instruments-21574480',
            headers=headers, verify=False, proxies=ip, timeout=20).text
        print(context)
