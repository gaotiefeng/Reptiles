#!/usr/bin/python3

from MysqlOrm import MysqlOrm
from MysqlConnector import MysqlConnector

table = 'fqi_admin'
filed = "user_name,email,password"
# mysqlOrm insert插入 update更新 all查询全部 first 查询一条
# data = "'qingchen1','159044350471','123456'"
# MysqlOrm().insert('fqi_admin', filed, data)
# where = "id > 0"
# res = MysqlOrm().all(table, where)
# print(res)
# where = "id > 0"
# res = MysqlOrm().first(table, where)
# print(res)
where = {'id': '2'}
data = {'user_name': 'test', 'password': '434334'}
MysqlOrm().update(table, where, data)

# val = [
#     ('Google', '21m', 'qingchen'),
#     ('Github', '1221.com', 'qingchen'),
#     ('Taobao', '1233to.com', 'qingchen')
# ]
# MysqlConnector().insert_all(table, filed, val)
