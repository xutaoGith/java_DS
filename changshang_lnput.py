import pymysql
import os
from clickhouse_driver import Client
import time
import re
import json

# 对mysql厂商建立链接
host = '192.168.2.210'  # 数据库的ip地址
user = 'root'  # 数据库的账号
password = 'root1234'  # 数据库的密码
port = 3306  # mysql数据库通用端口号
mysql = pymysql.connect (host=host, user=user, password=password, port=port,database='leo')
#新建mysql厂商查询页面
cursormysql = mysql.cursor()
#编写sql
sql =  'select id,changshang,leimu,mpn,mpnlink,pdfpath,createtime,qita from changshang'
#4.执行sql
cursormysql.execute(sql)
#5.查看结果
#用于返回mysql多条数据
results = cursormysql.fetchall()
#连接clickhouse
host = '192.168.2.212'
port = 9000
user = 'leo'
password = 'leo12345'
databse = 'finn'
time_start = time.perf_counter()
client = Client(host=host,port=port,user=user,password=password)
id = client.execute("""select max(id) from finn.all_files where""")[0][0]
for i in results:
    print(i)
    l = []
    id = id+1
    mpn=i[4]
    supplier=i[2]
    source = '官网'
    path = '192.168.2.210--leo--changshang'
    author = 'leo'
    pdfpath=i[6]
    mpnurl=i[5]
    a = i[5].split('/')[0:3]
    b = '/'.join(a)
    changshangurl=b
    status = '未处理'
    l.append((id,mpn,supplier,source,path,author,pdfpath,status,mpnurl,changshangurl))
    print(l)
    #client.execute("insert into finn.all_files(id,mpn,supplier,source,path,author,pdfpath,status,mpnurl,supplierurl) values",l)
#关闭mysql查询
cursormysql.close()
#关闭mysql数据库
mysql.close()