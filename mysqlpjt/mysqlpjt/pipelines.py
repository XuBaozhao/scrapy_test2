# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class MysqlpjtPipeline(object):
    def __init__(self):
        #刚开始连接对应数据库
        self.conn=pymysql.connect(host="127.0.0.1",user="root",passwd="root",db="mypydb")
    def process_item(self, item, spider):
        #将获取到的name和keywd分别赋给变量name和变量key
        name=item["name"][0]
        key=item["keywd"][0]
        #构造对应的sql语句
        sql="insert into mytb(title,keywd)VALUES ('"+name+"','"+key+"')"
        #通过query实现执行对应的sql语句
        self.conn.query(sql)
        return item
    def close_spider(self,spider):
        self.conn.close()
