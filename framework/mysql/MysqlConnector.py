#!/usr/bin/python3

import mysql.connector

class MysqlConnector:
    host = "192.168.1.128"
    port = 3306
    user = "baijiao_collect_1"
    password = "baijiao_collect_1"
    db = "baijiao_collect_1"

    def __init__(self):
        print("mysqlConnector host =%s - db = %s", self.host, self.db)

    @staticmethod
    def connect(self):
        db = mysql.connector.connect(host=self.host,
                                     user=self.user,
                                     password=self.password,
                                     db=self.db,
                                     port=self.port
                                     )
        return db

    @staticmethod
    def close(self, db):
        db.close()


    def insert_all(self, table, filed, val=[]):
        if not val:
            val = []
        sql = 'INSERT INTO  ' + table + ' (' + filed + ' ) VALUES (%s, %s, %s)'
        db = self.connect(self)
        cursor = db.cursor()
        cursor.executemany(sql, val)
        # 数据表内容有更新，必须使用到该语句
        db.commit()
        print(cursor.rowcount, "记录插入成功。")
        self.close(self, db)
