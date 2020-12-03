#!/usr/bin/python3
# encoding: utf-8
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import pymysql
from config import mysql

class MysqlOrm:
    type = 'insert'

    def __init__(self):
        config = mysql.config()
        self.host = config['host']
        self.port = config['port']
        self.username = config['username']
        self.password = config['password']
        self.db = config['db']

        print("mysqlOrm host =" + self.host + " - db =" + self.db)

    @staticmethod
    def connect(self):
        db = pymysql.connect(self.host, self.username, self.password, self.db)

        return db

    @staticmethod
    def close(self, db):
        db.close()

    # 查询一条数据
    """ @params where 字典类型
        @params table 表名
        @params filed 字段名称
    """
    def first(self, table, filed, where):

        where = self.where_and(where)
        # SQL 查询语句
        if not where:
            sql = 'SELECT ' + filed + ' FROM ' + table + ' limit 1'
        else:
            sql = 'SELECT ' + filed + ' FROM ' + table + ' WHERE ' + where + ' limit 1'

        self.type = 'first'
        return self.query_one(sql)

    # 查询所有条数据
    def all(self, table, where):
        where = self.where_and(where)
        # SQL 查询语句
        if not where:
            sql = 'SELECT * FROM ' + table
        else:
            sql = 'SELECT * FROM ' + table + ' WHERE ' + where

        self.type = 'all'
        return self.query_all(sql)

    # 插入一条数据
    def insert(self, table, data):
        filed, val = self.filed_data_str(data)
        # 使用预处理语句创建表
        sql = 'INSERT INTO  ' + table + ' (' + filed + ' ) VALUES ( ' + val + ')'

        self.type = 'insert'
        return self.execute_sql(sql)

    # 更新数据
    def update(self, table, where, data):
        # 更新数据
        filed_data = self.filed_data(data)

        where_val = self.where_and(where)

        sql = 'UPDATE ' + table + ' SET ' + filed_data + ' WHERE ' + where_val

        self.type = 'update'
        return self.execute_sql(sql)

    # 处理where and
    def where_and(self, where):
        # 字典处理where k=>v 转化str
        where_str = ''
        for k in where:
            where_str += ' ' + k + '=' + "'" + str(where[k]) + "' " + 'AND'

        where_val = where_str.rstrip('AND')
        return where_val

    # 更新数据处理
    def filed_data(self, data):
        # update字典处理k=>v转化str
        field_val = ''
        for k in data:
            field_val += k + '=' + "'" + str(data[k]) + "'" + ','

        val = field_val.rstrip(',')
        return val

    # 插入一条数据 数据处理
    def filed_data_str(self, data):
        # insert字典处理k=>v转化str
        field = ''
        field_val = ''
        for k in data:
            field += k + ','
            field_val += "'" + str(data[k]) + "'" + ','
        field = field.rstrip(',')
        val = field_val.rstrip(',')
        return field, val

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

