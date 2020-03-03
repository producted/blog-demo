#encoding: utf-8

import pymysql.cursors

def get_connection():
    return pymysql.connect(host='rm-bp1yl67ctc7v32a0c8o.mysql.rds.aliyuncs.com',
                            user='hhdev',
                            password='ZZHH51dev',
                            db='test_nacos',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)


