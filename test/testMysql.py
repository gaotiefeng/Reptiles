import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import time
from framework.mysql import MysqlOrm as sql

class testMysql:

    def __init__(self):
        self.table = 'user'

    # first
    def first(self):
        where = {'id': 2}
        filed = '*'
        result = sql.MysqlOrm().first(self.table, filed, where)
        print(result)

    # 插入一条数据
    def insert(self):
        localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        data = {'name': '1', 'password': '2', 'created_at': localtime}
        result = sql.MysqlOrm().insert(self.table, data)
        print(result)

    # 更新一条数据
    def update(self):
        localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        data = {'name': '12332', 'password': '223223', 'created_at': localtime}
        where = {'id': 1}
        result = sql.MysqlOrm().update(self.table, where, data)
        print(result)

    # 查询所有
    def all(self):
        where = {}
        result = sql.MysqlOrm().all(self.table, where)
        print(result)














