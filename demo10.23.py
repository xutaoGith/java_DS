from clickhouse_driver import Client
import time

host_name = '192.168.2.212'
client = Client(host = host_name,
                # database = 'test6',
                user = 'default',
                password = 'clickhouse398180',
                port=9000)

time_start = time.perf_counter()
f = open(r'D:\日志\10.26-50w.txt',mode='a+',encoding='utf-8')
print("select id,pdfpath from ic_web.ic_material_1_all ORDER BY id ASC limit 500000;")
# query_ck_sql = "select id,pdfpath from ic_web.ic_material_1_all where pdf2 is null or pdf2 = '' ORDER BY id ASC limit 1;"
query_ck_sql = "select id,pdfpath from ic_web.ic_material_1_all where (pdf2 is null or pdf2 = '') and id > 94195105  ORDER BY id ASC limit 500000;"
res = client.execute(query_ck_sql)
for row in res:
    a,b = row
    # print(f"主表id为：{a}")
    # print(b)
    b = b.replace("?hkey=EF798316E3902B6ED9A73243A3159BB0","")
    # print(b)
    time_start1 = time.perf_counter()
    query_ck_sql1 = f"select mpn_id from finn.all_pdf_links_all where pdf_link = '{b}';"
    res2 = client.execute(query_ck_sql1)
    # print(res2)
    if not res2:
        pass
    else:
        for rows in res2[0]:
            # print(rows)
            if not rows:
                pass
            else:
                query_ck_sql2 = f"alter table ic_web.ic_material_1_local ON ClUSTER icisee_cluster_replication update pdf2 = '{rows}' where id = {a};"
                # query_ck_sql2 = f"INSERT into test6.replicaTest9(id,name) values({a},'{b}');"
                print(f"正在更新id为:{a},其在finn表的mpnid为{rows}")
                f.write(f"正在更新id为:{a},其在finn表的mpnid为{rows}\n")
                client.execute(query_ck_sql2)
                time_end1 = time.perf_counter()
                time_sum1 = time_end1 - time_start1
                print(f"本条提交用时为："+"%.2f" % time_sum1)


time_end = time.perf_counter()

time_sum = time_end - time_start
print(f"用时为：{time_sum}秒")