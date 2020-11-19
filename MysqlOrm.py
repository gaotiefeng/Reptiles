#!/usr/bin/python3

import pymysql

class MysqlOrm:
    host = "192.168.1.128"
    port = 3306
    username = "baijiao_collect_1"
    password = "baijiao_collect_1"
    db = "baijiao_collect_1"
    type = 'insert'

    def __init__(self):
        print("mysqlOrm host =" + self.host + " - db =" + self.db)

    @staticmethod
    def connect(self):
        db = pymysql.connect(self.host, self.username, self.password, self.db)

        return db

    @staticmethod
    def close(self, db):
        db.close()

    def first(self, table, where):
        # SQL 查询语句
        sql = 'SELECT * FROM ' + table + ' WHERE ' + where

        self.type = 'first'
        return self.query_one(sql)

    def all(self, table, where):
        # SQL 查询语句
        sql = 'SELECT * FROM ' + table + ' WHERE ' + where

        self.type = 'all'
        return self.query_all(sql)

    def insert(self, table, filed, params):
        # 使用预处理语句创建表
        sql = 'INSERT INTO  ' + table + ' (' + filed + ' ) VALUES ( ' + params + ')'

        self.type = 'insert'
        return self.execute_sql(sql)

    def update(self, table, where, data):
        # 更新数据
        filed_data = self.filed_data(data)

        where_val = self.where_and(where)

        sql = 'UPDATE ' + table + ' SET ' + filed_data + ' WHERE ' + where_val

        self.type = 'update'
        return self.execute_sql(sql)

    def where_and(self, where):
        # 字典处理where k=>v 转化str
        where_str = ''
        for k in where:
            where_str += ' ' + k + '=' + "'" + where[k] + "' " + 'AND'

        where_val = where_str.rstrip('AND')
        return where_val

    def filed_data(self, data):
        # update字典处理k=>v转化str
        field_val = ''
        for k in data:
            field_val += k + '=' + "'" + data[k] + "'" + ','

        val = field_val.rstrip(',')
        return val

    # 查询
    def query_one(self, sql):
        db = self.connect(self)
        cursor = db.cursor()
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchone()
        except:
            print(self.type+"异常 sql= "+sql)
        self.close(self, db)
        return results

    # 查询全部
    def query_all(self, sql):
        print(self.type+"类型 sql= "+sql)
        db = self.connect(self)
        cursor = db.cursor()
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
        except:
            print(self.type+"异常 sql= "+sql)

        self.close(self, db)
        return results

    # 执行
    def execute_sql(self, sql):
        print(self.type+"类型 sql= "+sql)
        db = self.connect(self)
        cursor = db.cursor()
        msg = True
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 提交修改
            db.commit()
        except:
            print(self.type+"异常 sql= "+sql)
            # 发生错误时回滚
            db.rollback()
            msg = False

        self.close(self, db)
        return msg

