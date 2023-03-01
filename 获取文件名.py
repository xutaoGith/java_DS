import os,pymysql,re

# path = 'ZHENHUAFU:/Users/EDZ/Desktop/asfd'
# datanames = os.listdir(path)
# name_list=[]
# for i in datanames:
#     path = 'ZHENHUAFU:/Users/EDZ/Desktop/asfd/'+i
#     data = os.listdir(path)
#     for k in data:
#         name_list.append(k.split('_')[0].split('.')[0])
# print(name_list)

class pdf_url_redis():
    def __init__(self):
        # 连接redis
        # 连接myusql
        self.conn = pymysql.connect(host="192.168.2.210", port=3306, user='root', passwd="root1234", db="leo", charset='utf8')
        self.cursor = self.conn.cursor()


    def get_pdf_url(self):
        path = 'd:/asdf'
        # path = 'E:/pdf_list_aa'
        datanames = os.listdir(path)
        name_list=[]
        for i in datanames:
            path = 'd:/asdf/'+i
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
                content_list = re.findall('/(\d+_{0,1}\d+).json', content)
                f.close()
            for n in content_list:
                name_list.append(n.split('_')[0])

        sql = "select * from spider_data "
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        link = []
        for i in data:
           link.append(str(i[0]))
        print(link)
        print('添加完成')

if __name__ == '__main__':
    t = pdf_url_redis()
    t.get_pdf_url()

