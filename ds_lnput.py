import os
from clickhouse_driver import Client
import time
import re
import json

host = '192.168.2.212'
port = 9000
user = 'leo'
password = 'leo12345'
databse = 'finn'
time_start = time.perf_counter()
client = Client(host=host, port=port, user=user, password=password)
id = 106967668
print('获取所有日期文件夹')
for f, d_list, n in os.walk('D:\shuju'):  # 获取所有日期文件夹
    for d in d_list:  # 循环日期文件夹
        if int(d) >= 20221020:
            print("开始解析%s日期文件夹" % d)
            datadict_list = []
            for filename in os.walk(os.path.join(f, d)):  # 获取当前日期下所有json文件
                for wj in filename[2]:
                    print('开始解析%s日期' % d, '文件夹下——型号：%s' % wj)
                    path = os.path.join(filename[0], wj)
                    with open(path, encoding='utf-8') as file:
                        id = id + 1
                        try:
                            items = json.load(file)
                            pdfpath = items["props"]["pageProps"]["pageData"]["partdetails"]["summary"]['datasheet']
                            if not pdfpath:
                                pdfpath = ''
                            datadict_list.append({
                                'id': id,
                                'mpn': items["props"]["pageProps"]["pageData"]["partdetails"]["summary"]['partNumber'].replace("'","\\'"),
                                'supplier': items["props"]["pageProps"]["pageData"]["partdetails"]["summary"]['mfr'].replace("'","\\'"),
                                'source': 'ds',
                                'type': '详情信息',
                                'type2': '单个型号',
                                'createtime': time.strftime('%Y-%m-%d %H:%M:%S'),
                                'path': path.replace("'","\\'"),
                                'author': 'leo',
                                'relatedparts': json.dumps(items["props"]["pageProps"]["pageData"]["relatedParts"]).replace("'","\\'"),
                                'pdfpath': pdfpath.replace("'","\\'"),
                                'status': '未处理',
                                'mpnurl': 'https://www.datasheets.com/en/part-details/' + items["query"]['slug'].replace("'","\\'")
                            })
                            file.close()
                        except:
                            datadict_list.append({
                                'id': id,
                                'mpn': '',
                                'supplier': '',
                                'source': 'ds',
                                'type': '',
                                'type2': '',
                                'createtime': time.strftime('%Y-%m-%d %H:%M:%S'),
                                'path': path,
                                'author': 'leo',
                                'relatedparts': '',
                                'pdfpath': '',
                                'status': '未处理',
                                'mpnurl': '',
                            })
                        file.close()

                    sql = "insert into finn.all_files "
                    sum1 = 0
                    if datadict_list.__len__()==50000:
                        for datadict in datadict_list:
                            result = datadict
                            names = ["%s" % x for x in result.keys()]
                            names = ','.join(names)
                            if sum1 == 0:
                                sql = sql + "(%s) values " % names
                            values = ["'%s'" % x if isinstance(x, str) else "{}".format(x) for x in result.values()]
                            values = ",".join(values)
                            sql = sql + "(%s)," % (values)
                            sum1 = sum1 + 1
                        sql_str = sql[0:-1]
                        client.execute(sql_str)
                        datadict_list = []
