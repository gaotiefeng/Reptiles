#!/usr/bin/python3
# encoding: utf-8
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from config import mysql
import mysql.connector

class MysqlConnector:

    def __init__(self):
        config = mysql.config()
        self.host = config['host']
        self.port = config['port']
        self.username = config['username']
        self.password = config['password']
        self.db = config['db']

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
