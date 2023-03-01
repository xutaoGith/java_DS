# -*- coding: utf-8 -*
import time, re
import urllib.request
import redis, json
from lxml import etree
import ssl
from urllib.parse import quote
import os
import os.path
from parsel import Selector
# from jiami import AES_Encrypt
from multiprocessing import Process, Queue
import requests
import pymysql
from demo import CollectMethod


class req_content(Process):
    def __init__(self, link_list):
        super().__init__()
        self.link_list = link_list
        self.collect = CollectMethod()
        self.headers = ''
        self.ip = ''
        self.cur = ''
        self.conn = ''
        # 状态
        self.status = ''
        self.etree = ''
        self.file = ''

    # 更换token
    def change_token(self):
        while True:
            try:
                while True:
                    self.ip = self.collect.ip_proxies()
                    print(self.ip)
                    headercontent = self.collect.getheadercontent(self.ip)
                    token = self.collect.isOk(headercontent, self.ip)
                    if token:
                        try:
                            url = "https://www.datasheets.com/ckly-was-is-go-theere-my-Iewes-neede-worth-And-h?d=www.datasheets.com"
                            header = {
                                "content-type": "text/plain; charset=utf-8",
                                "cookie": headercontent,
                                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36"
                            }
                            data = {
                                "solution": {
                                    "interrogation": self.collect.getPParam()
                                },
                                "version": "stable",
                                "old_token": None, "error": None, "performance": {"interrogation": 234}}
                            response = requests.post(url=url, headers=header, json=data, proxies=self.ip, verify=False,
                                                     timeout=60).json()
                            reese84 = response['token']
                            self.headers = {
                                "cookie": headercontent + "reese84=" + reese84,
                                "referer": 'https://www.datasheets.com/api/taxonomies/breadcrumb?taxonomyPath=Semiconductor|Communication|Protocols%20and%20Networks',
                                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36"
                            }
                            break
                        except Exception as e:
                            print(e)
                if token:
                    break
            except Exception as e:
                print(e)


    # 访问url
    def visit_url(self, url):
        R = redis.Redis(host='192.168.2.210', port=6379, db=0, password='')
        while True:
            r = 5
            respone = ''
            xq_context = False
            while r > 0:
                r -= 1
                try:
                    context = ssl._create_unverified_context()
                    proxys = urllib.request.ProxyHandler(self.ip)
                    opener = urllib.request.build_opener(proxys)
                    urllib.request.install_opener(opener)
                    response = urllib.request.Request(url.replace(' ', '%20'), headers=self.headers)
                    response = urllib.request.urlopen(response, context=context,timeout=20)
                    respone = response.read()
                except Exception as e:
                    if '404' in str(e):
                        return ''
                    # print(e)
                    continue
                if 'NAME="robots"' in respone.decode() or 'Request unsuccessful. Incapsula incident' in respone.decode():
                    print('-------------------------访问失败，重新访问，剩余次数：', r)
                    xq_context = False
                else:
                    xq_context = True
                    break
            if not xq_context:
                while True:

                    if R.dbsize() > 0:
                        print('------------------------过期ip，重新获取ip', self.ip)
                        print('------------------------失败url', url)
                        R.delete(json.dumps(self.ip))
                        self.ip = eval(R.randomkey())
                        self.headers = eval(R.get(json.dumps(self.ip)))
                        break
                continue
            else:
                return respone

    def processing_name(self, name):
        name1 = re.findall(r'[?|、|:|//|*|“|”|"|<|>]', name)
        if name1:
            for i in name1:
                name = name.replace(i, quote(i))
        name = name.replace('/', '————').replace('|', quote('|')).replace('\\', quote('\\'))
        return name

    def xq_fangq(self, visit_url, url_list):
        try:
            visit_url = etree.HTML(visit_url)
            context = visit_url.xpath('//*[@id="__NEXT_DATA__"]')[0].text
            file_path = '/home/icisee/software/leo/数据采集/ds_pdf_download_list/' + str(
                time.strftime("%Y%m%d")) + '/' + self.processing_name(url_list) + '.json'
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, 'w') as f:
                f.write(context)
                f.close()

            for item in visit_url.xpath('//*[@id="table-scroll"]/tbody/tr'):
                name = item.xpath('td[2]/a/text()')[0]
                url = 'https://www.datasheets.com' + item.xpath('td[2]/a/@href')[0]

                xq_respone = self.visit_url(url)
                if xq_respone:
                    xq_respone = etree.HTML(xq_respone)
                    context = xq_respone.xpath('//*[@id="__NEXT_DATA__"]')[0].text
                    file_path = '/home/icisee/software/leo/数据采集/ds_pdf_download/' + str(
                        time.strftime("%Y%m%d")) + '/' + self.processing_name(name) + '.json'
                    os.makedirs(os.path.dirname(file_path), exist_ok=True)
                    with open(file_path, 'w') as f:
                        f.write(context)
                        f.close()

                    item = []
                    item.append(name)  # 给item属性赋值
                    item.append(url)
                    pdf_url = ''
                    pdf_url = xq_respone.xpath('//*[@id="datasheet"]/section/div/div[2]/a/@href')[0]
                    if not pdf_url:
                        pdf_url = xq_respone.xpath('//*[@id="datasheet"]/section/div/div[1]/a/@href')[0]
                    item.append(pdf_url)

                    try:
                        sql = "insert into ds_pdf_download_spider_copy1(mpn,url,pdf_url) values('%s','%s','%s')" % (
                            item[0], item[1], item[2])
                        self.cur.execute(sql)
                        self.conn.commit()
                        print('-------------------------查询 ' + url + ' 成功')
                        print('-------------------------存储 ' + name + ' 成功')
                    except Exception as e:

                        print('-------------------------查询 ' + url + ' 失败',e)
                        pass

                else:
                    file = open('查询失败详情404.txt', 'a', encoding='utf8')
                    file.write(str(url) + '\n')
                    file.close()
                    print('-------------------------查询 ' + url + ' 失败')

        except Exception as e:
            file = open('查询失败详情.txt', 'a', encoding='utf8')
            file.write(str(url) + '\n')
            file.close()
            print('-------------------------查询 ' + url + ' 失败')
            print('-------------------------存储 ' + name + ' 失败')


    # 循环pdf链接下载
    def run(self):
        self.conn = pymysql.connect(host='192.168.2.210', port=3306, user='root', passwd='root1234', db='leo',
                                    charset='utf8')
        self.cur = self.conn.cursor()
        # self.change_token()
        R = redis.Redis(host='192.168.2.210', port=6379, db=0, password='')
        while True:
            if R.dbsize() > 0:
                self.ip = eval(R.randomkey())
                self.headers = eval(R.get(json.dumps(self.ip)))
                break
        while True:
            if self.link_list.qsize() > 0:
                time.sleep(1)
                url_list = []
                url = self.link_list.get()
                url_list.append(url.split('&mpn_id=')[0])
                url_list.append(url.split('&mpn_id=')[1])
                print('开始查询：', url)
                try:
                    visit_url = self.visit_url(url_list[0])
                    if visit_url:
                        p = re.findall('&p=(\d+)&', url_list[0])[0]
                        self.xq_fangq(visit_url, url_list[1])
                        if p == '1':
                            table = re.findall('total_items":(\d+),', str(visit_url))[0]
                            if int(table) > 500:
                                table = 500

                            total = int(table)
                            Number = int(25)
                            if total % Number > 0:
                                page = total // Number + 1
                            else:
                                page = total // Number

                            for i in range(1, page + 1):
                                if i != 1:
                                    id = url_list[1] + '_' + str(i)
                                    url = re.sub('&p=\d+&', '&p=' + str(i) + '&', url_list[0])
                                    # 翻页url
                                    fe_respone = self.visit_url(url)
                                    if fe_respone:
                                        self.xq_fangq(fe_respone, id)
                                    else:
                                        file = open('查询失败列表404.txt', 'a', encoding='utf8')
                                        file.write(str(url_list[0]) + '\n')
                                        file.close()
                                        print('查询失败：', url)
                        sql = "insert into ds_pdf_download_list(url) values('%s')" % (url_list[0])
                        self.cur.execute(sql)
                        self.conn.commit()
                    else:
                        file = open('查询失败列表404.txt', 'a', encoding='utf8')
                        file.write(str(url_list[0]) + '\n')
                        file.close()
                        print('查询失败：', url)
                except Exception as e:
                    file = open('查询失败列表.txt', 'a', encoding='utf8')
                    file.write(str(url_list[0]) + '\n')
                    file.close()
                    print('查询失败：', url)


class linke_c(Process):
    def __init__(self, link_list):
        super().__init__()
        self.link_list = link_list
        self.startt = ''
        self.end = ''
        self.conn = ''
        self.cur = ''

    def run(self):
        r = redis.Redis(host='192.168.2.210', port=6379, db=2)
        while True:
            cs = r.llen('pdf_url')
            if self.link_list.qsize() == 0:
                conn = pymysql.connect(host='192.168.2.210', port=3306, user='root', passwd='root1234', db='leo',
                                       charset='utf8')
                cur = conn.cursor()
                sql = "SELECT * from spider_data WHERE url not in (SELECT url from ds_pdf_download_list) limit 0,50000"
                cur.execute(sql)
                result = cur.fetchall()
                if result:
                    print('-------------------------查询完毕')
                    # redis
                    for i in result:
                        url = i[1] + '&mpn_id=' + str(i[0])
                        r.lpush('pdf_url', url)
                        # print(i[1])
                else:
                    break
                # 取值
                for key in range(0, r.llen('pdf_url')):
                    size = r.blpop('pdf_url')
                    self.link_list.put(size[1].decode())
                print('-------------------------查询完毕')


if __name__ == '__main__':
    link_list = Queue(1000000)
    for i in range(1):
        tb = linke_c(link_list)
        tb.start()

    for i in range(20):
        t = req_content(link_list)
        t.start()
